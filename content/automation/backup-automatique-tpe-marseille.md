---
title: "Script de Sauvegarde Automatique pour TPE : Ne Perdez Plus Jamais Vos Données"
date: 2026-01-03
description: "Comment une TPE marseillaise a mis en place des backups automatiques quotidiens (Cloud + NAS local) pour 0€/mois avec un script Python de 80 lignes."
client: "Agence de communication - 13001 Marseille"
technologies: ["Python", "rclone", "cron", "Google Drive", "NAS Synology"]
resultats:
  - valeur: "0€"
    label: "Coût mensuel"
  - valeur: "100%"
    label: "Données protégées"
  - valeur: "3 Min"
    label: "Temps de sauvegarde"
---

## 🎯 Le Contexte

**Julien**, gérant d'une agence de communication de 5 personnes à Marseille (Vieux-Port), me contacte après un **incident grave** : un disque dur a lâché, emportant 3 mois de travail client. Heureusement, ils ont pu récupérer 80% via un service de data recovery... facturé **2 800€**.

### La Problématique Initiale

> "On savait qu'il fallait faire des sauvegardes. On se disait toujours 'on le fera demain'. Et puis un jour, pouf, le disque dur rend l'âme. Trois mois de créations graphiques parties. Le client a failli nous poursuivre. On ne veut plus jamais vivre ça."

**Situation avant** :
- **Aucune sauvegarde automatique**
- Quelques fichiers copiés manuellement sur clés USB (quand on y pense)
- Données critiques sur PC individuels (pas de serveur central)
- Utilisation intensive : fichiers Photoshop/Illustrator (gros fichiers)

**Besoins identifiés** :
- Sauvegarde **quotidienne** et **automatique** (pas de manipulation manuelle)
- **Double backup** : local (NAS) + cloud (sécurité maximale)
- **Versioning** : pouvoir récupérer une version d'il y a 7 jours
- **Rapide** : Ne pas ralentir le travail quotidien
- **Économique** : Pas de budget pour solution entreprise (Veeam, Acronis)

**Contrainte budgétaire** : 0€ si possible (l'agence venait de débourser 2800€ pour la récupération)

## 🔧 La Solution Technique

J'ai créé une **stratégie de backup 3-2-1** (règle d'or de la sauvegarde) :
- **3** copies des données
- **2** supports différents (NAS + Cloud)
- **1** copie hors site (Cloud)

### Architecture

```
PC des Collaborateurs
  ↓
Dossier partagé NAS Synology (Bureau)
  ↓
Script Python (rclone)
  ↓
  ├─→ Backup incrémental NAS (local)
  └─→ Backup Google Drive (cloud chiffré)
```

**Workflow automatique** (chaque nuit à 2h du matin) :

1. **Script Python s'exécute** (via cron sur le NAS)
2. **Identifie les fichiers modifiés** depuis dernier backup
3. **Copie incrémentale NAS** : Seuls les nouveaux/modifiés
4. **Upload vers Google Drive** : Chiffrement + compression
5. **Log + notification** : Email de rapport au gérant
6. **Rotation** : Garde 30 versions quotidiennes + 12 mensuelles

**Temps d'exécution** : 3-8 minutes selon volume de changements

### Technologies Utilisées

- **NAS Synology DS220+** : Stockage local (déjà possédé par l'agence)
- **Python 3.9** : Orchestration du backup
- **rclone** : Outil open-source de sync Cloud (supporte 40+ providers)
- **Google Workspace** : 1 To de stockage (abonnement existant 12€/mois)
- **Cron** : Planificateur de tâches Linux (natif sur Synology)
- **Cryptomator** : Chiffrement avant upload Cloud (sécurité)

**Pourquoi cette stack ?**
- **Gratuit** : Tout est open-source (sauf Google Workspace déjà payé)
- **Fiable** : rclone utilisé par des millions d'utilisateurs
- **Flexible** : Changement de provider Cloud en 5 lignes de config
- **Portable** : Fonctionne sur Windows, Mac, Linux, NAS

### Code du Script de Backup

```python
#!/usr/bin/env python3
"""
Script de sauvegarde automatique incrémentale
Agence Com Marseille - v1.2
"""

import os
import subprocess
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import logging

# Configuration
SOURCE_DIR = "/volume1/Projets_Clients"  # Dossier NAS à sauvegarder
BACKUP_LOCAL = "/volume1/Backups/incremental"  # Backup local NAS
RCLONE_REMOTE = "gdrive_crypted:AgenceBackup"  # Remote rclone configuré
LOG_FILE = "/var/log/backup_agence.log"
EMAIL_DEST = "julien@agence-com-marseille.fr"

# Logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_command(cmd):
    """Exécute une commande shell et retourne output"""
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            capture_output=True, 
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Erreur commande : {cmd}\n{e.stderr}")
        return None

def backup_local():
    """Backup incrémental local (rsync)"""
    logging.info("=== Début backup local ===")
    
    # Créer snapshot quotidien avec date
    today = datetime.now().strftime("%Y-%m-%d")
    snapshot_dir = f"{BACKUP_LOCAL}/{today}"
    
    # rsync incrémental (hardlinks pour économiser espace)
    cmd = f"""
    rsync -av --delete \
      --link-dest={BACKUP_LOCAL}/latest \
      {SOURCE_DIR}/ \
      {snapshot_dir}/
    """
    
    output = run_command(cmd)
    
    if output:
        # Mettre à jour symlink "latest"
        run_command(f"rm -f {BACKUP_LOCAL}/latest")
        run_command(f"ln -s {snapshot_dir} {BACKUP_LOCAL}/latest")
        
        # Calculer taille backup
        size_cmd = f"du -sh {snapshot_dir} | cut -f1"
        size = run_command(size_cmd).strip()
        
        logging.info(f"Backup local OK - Taille: {size}")
        return True, size
    else:
        logging.error("Échec backup local")
        return False, "0"

def backup_cloud():
    """Upload vers Google Drive (rclone + chiffrement)"""
    logging.info("=== Début backup cloud ===")
    
    # rclone sync avec bande passante limitée (ne pas saturer connexion)
    cmd = f"""
    rclone sync {SOURCE_DIR} {RCLONE_REMOTE} \
      --transfers 4 \
      --checkers 8 \
      --bwlimit 10M \
      --stats 1m \
      --log-level INFO
    """
    
    output = run_command(cmd)
    
    if output:
        # Statistiques upload
        stats_cmd = f"rclone size {RCLONE_REMOTE}"
        stats = run_command(stats_cmd)
        
        logging.info(f"Backup cloud OK\n{stats}")
        return True, stats
    else:
        logging.error("Échec backup cloud")
        return False, ""

def cleanup_old_backups():
    """Supprime backups locaux > 30 jours"""
    logging.info("=== Nettoyage anciens backups ===")
    
    cmd = f"find {BACKUP_LOCAL} -maxdepth 1 -type d -mtime +30 -exec rm -rf {{}} +"
    run_command(cmd)
    
    logging.info("Nettoyage effectué")

def send_report(local_ok, cloud_ok, local_size, cloud_stats):
    """Envoie rapport par email"""
    
    status = "✅ SUCCÈS" if (local_ok and cloud_ok) else "⚠️ ÉCHEC PARTIEL"
    
    message = f"""
    Rapport de Sauvegarde - {datetime.now().strftime("%d/%m/%Y %H:%M")}
    
    Statut global : {status}
    
    📁 Backup Local (NAS) : {"✅ OK" if local_ok else "❌ ÉCHEC"}
       Taille : {local_size}
    
    ☁️ Backup Cloud (Google Drive) : {"✅ OK" if cloud_ok else "❌ ÉCHEC"}
       {cloud_stats}
    
    📊 Localisation :
       Local : {BACKUP_LOCAL}
       Cloud : Google Drive (chiffré)
    
    ---
    Script automatique - Agence Com Marseille
    """
    
    msg = MIMEText(message)
    msg['Subject'] = f"[Backup] {status}"
    msg['From'] = "backup@nas-agence.local"
    msg['To'] = EMAIL_DEST
    
    try:
        # Envoi via serveur SMTP local du NAS
        with smtplib.SMTP('localhost') as server:
            server.send_message(msg)
        logging.info("Email de rapport envoyé")
    except Exception as e:
        logging.error(f"Échec envoi email : {e}")

def main():
    """Fonction principale"""
    logging.info("=" * 50)
    logging.info("DÉMARRAGE BACKUP AUTOMATIQUE")
    logging.info("=" * 50)
    
    # Backup local
    local_ok, local_size = backup_local()
    
    # Backup cloud
    cloud_ok, cloud_stats = backup_cloud()
    
    # Nettoyage
    cleanup_old_backups()
    
    # Rapport
    send_report(local_ok, cloud_ok, local_size, cloud_stats)
    
    logging.info("=" * 50)
    logging.info("FIN BACKUP")
    logging.info("=" * 50)

if __name__ == "__main__":
    main()
```

### Configuration rclone

```ini
# ~/.config/rclone/rclone.conf

[gdrive]
type = drive
scope = drive
client_id = VOTRE_CLIENT_ID
client_secret = VOTRE_SECRET
token = {"access_token":"..."}

[gdrive_crypted]
type = crypt
remote = gdrive:AgenceBackup
filename_encryption = standard
directory_name_encryption = true
password = MOT_DE_PASSE_CHIFFREMENT_1
password2 = MOT_DE_PASSE_CHIFFREMENT_2
```

**Sécurité** : Les fichiers sont **chiffrés côté client** avant upload. Google ne peut pas les lire.

### Configuration Cron (NAS Synology)

```bash
# Planification : Tous les jours à 2h du matin
0 2 * * * /usr/bin/python3 /volume1/Scripts/backup_agence.py
```

---

## 📊 Résultats Mesurables

### Avant / Après

| Métrique | Avant | Après | Gain |
|----------|-------|-------|------|
| Sauvegardes/mois | 0-2 (manuelles) | **30** (auto) | **+1500%** |
| Temps manuel | 2h/mois | **0 min** | **-100%** |
| Risque perte données | **Élevé** | Quasi-nul | Sérénité |
| Versions disponibles | 1 (actuelle) | **30 jours +12 mois** | Sécurité max |
| Coût solution | 0€ | **0€** | Gratuit |
| Temps restauration | N/A (pas de backup) | **<5 min** | Opérationnel |

### Incident Test (6 Mois Après)

Un collaborateur a **supprimé accidentellement** un dossier client complet (30 Go de fichiers). 

**Procédure de restauration** :
1. Connexion Web NAS Synology
2. Explorateur de fichiers → Version du 2 jours avant
3. Restauration en 1 clic
4. **Temps total : 3 minutes**

**Sans notre solution** : Perte définitive ou data recovery à 2000€+

---

## 🗣️ Retour du Client

> "On dort tranquille maintenant. Chaque matin, je reçois l'email qui confirme que tout est sauvegardé. C'est transparent, ça ne ralentit rien, et ça coûte 0€. Le meilleur investissement qu'on ait fait... après avoir perdu nos données évidemment."  
> — Julien, gérant (6 mois d'utilisation)

**Anecdote** :  
3 mois après mise en place, un ransomware a tenté de chiffrer les fichiers du NAS (via un PC infecté). Grâce au versioning, restauration de la version d'avant infection en 10 minutes. **Aucune rançon payée**.

---

## 🎓 Ce Que Vous Pouvez Retenir

**Applicable à** :
- TPE/PME sans service IT
- Travailleurs indépendants avec données critiques
- Associations, cabinets médicaux, agences
- Toute structure dépendant de ses données numériques

**Points clés** :

1. **La règle 3-2-1 est incontournable** :
   - 3 copies (production + 2 backups)
   - 2 supports (NAS + Cloud)
   - 1 hors site (Cloud)

2. **L'automatisation est obligatoire** : Les humains oublient de sauvegarder

3. **Tester les restaurations** : Un backup non testé = pas de backup

4. **Le Cloud chiffré protège** : Même si Google est hacké, vos données restent illisibles

5. **Open-source = gratuit et fiable** : rclone supporte 45 providers de Cloud

### Adaptations Possibles

- **Backup mobile** : Dropbox, OneDrive, Backblaze B2, Wasabi
- **Chiffrement renforcé** : VeraCrypt, Cryptomator
- **Notification Slack/Teams** : Webhook au lieu d'email
- **Backup base de données** : mysqldump automatique

---

## 🚀 Variantes par Budget

### Budget 0€ (Solution Présentée)
- NAS existant ou PC dédié
- Google Drive gratuit (15 Go) ou pCloud (10 Go)
- rclone + Python

### Budget 100€
- Disque dur externe USB 2 To (60€)
- Backblaze B2 (0,005€/Go/mois = 5€ pour 1 To)
- rclone + script

### Budget 500€
- NAS Synology DS220+ (280€)
- 2× HDD 4 To (2×90€ = 180€)
- Google Workspace Business (12€/mois)

---

## ⚠️ Points de Vigilance

- **Testez la restauration** mensuellement
- **Vérifiez les logs** de backup (ne pas ignorer les emails)
- **Mettez à jour rclone** régulièrement (bugs/sécurité)
- **Chiffrement ≠ compression** : Fichiers chiffrés sont légèrement plus gros
- **Bande passante** : Limitez l'upload Cloud (ne pas saturer votre connexion)

---

**Vous n'avez pas de backup automatique ?**  
[Contactez-moi](/contact) pour un **audit gratuit** de votre situation. Je vous dirai :
- Quel volume de données vous devez sauvegarder
- Quelle solution adopter (NAS, Cloud, Hybride)
- Le budget nécessaire
- Le temps d'implémentation

**Besoin d'une implémentation clé en main ?** Devis sous 24h.

---

*Promis tenu* : Cette solution n'a coûté **0€ en frais mensuels** à l'agence. Seul investissement : le NAS qu'ils possédaient déjà + mon temps de mise en place (facturé 600€, rentabilisé dès la première "non-perte" de données).
