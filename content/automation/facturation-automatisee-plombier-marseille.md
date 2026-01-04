---
title: "Comment j'ai Automatisé la Facturation d'un Plombier Marseillais avec Python"
date: 2026-01-03
description: "Un plombier perdait 8h par mois à créer des factures manuellement. Découvrez comment un script Python et Google Sheets lui ont fait gagner 96h par an."
client: "Artisan plombier - 13008 Marseille"
technologies: ["Python", "Google Sheets API", "Gmail API", "PDF"]
resultats:
  - valeur: "8h"
    label: "Économisées par mois"
  - valeur: "3 min"
    label: "Temps de facturation"
  - valeur: "0€"
    label: "Coût mensuel"
---

## 🎯 Le Contexte

**Marc** (prénom modifié), plombier indépendant à Marseille 13008, me contacte en septembre 2025. Il a une bonne clientèle, beaucoup d'interventions, mais un problème récurrent : **la facturation lui prend un temps fou**.

### La Problématique Initiale

> "Je passe mes soirées à faire mes factures. J'ouvre Word, je remplis le template, je sauvegarde en PDF, j'envoie par mail... Pour 40 factures par mois, ça me bouffe 8 heures ! Et je fais régulièrement des erreurs de calcul."

**Temps perdu** : 8 heures par mois (12 minutes par facture en moyenne)  
**Tâches répétitives** : 
- Créer le document Word à partir d'un template
- Remplir manuellement les informations client
- Calculer les totaux (HT, TVA, TTC)
- Exporter en PDF
- Rédiger et envoyer l'email

**Impact métier** : 
- Fatigue administrative en fin de journée
- Erreurs de calcul occasionnelles
- Retards d'envoi → retards de paiement

## 🔧 La Solution Technique

Au lieu d'un logiciel de facturation payant (Henrri, Freebe à 20-30€/mois), j'ai créé une **solution sur mesure gratuite** basée sur les outils qu'il utilisait déjà.

### Architecture

```
Google Sheets (Saisie) 
    ↓
Script Python (Traitement)
    ↓
Génération PDF (facture)
    ↓
Envoi automatique par Gmail
```

**Workflow final** :
1. Marc remplit une ligne dans Google Sheets (2 min)
2. Il clique sur un bouton "Générer facture"
3. Le script Python :
   - Récupère les données (API Google Sheets)
   - Calcule automatiquement les totaux
   - Génère un PDF professionnel
   - Envoie la facture par email au client
   - Archive dans Google Drive
4. **Temps total : 3 minutes** (au lieu de 12)

### Technologies Utilisées

- **Python 3.11** : Langage principal pour l'automatisation
- **Google Sheets API** : Récupération des données de facturation
- **ReportLab (bibliothèque Python)** : Génération de PDF personnalisés
- **Gmail API** : Envoi automatique des emails avec pièce jointe
- **Google Apps Script** : Bouton personnalisé dans Sheets pour lancer le processus

### Fonctionnalités Clés

1. **Template PDF professionnel** : Logo, mentions légales, numéro SIRET, auto-calculé
2. **Numérotation automatique** : Incrémentation automatique du numéro de facture (F2025-001, F2025-002, etc.)
3. **Email personnalisé** : Message adapté selon le type de client (particulier vs professionnel)
4. **Archivage automatique** : Chaque PDF sauvegardé dans un dossier Drive organisé par année et mois
5. **Calcul TVA intelligent** : Détection automatique selon le statut (micro-entrepreneur exonéré ou non)

## 📊 Résultats Mesurables

| Métrique | Avant | Après | Gain |
|----------|-------|-------|------|
| Temps par facture | 12 minutes | 3 minutes | **-75%** |
| Temps mensuel | 8 heures | 2 heures | **-75%** |
| Temps annuel | 96 heures | 24 heures | **72h gagnées** |
| Erreurs de calcul | 2-3/mois | 0 | **100%** |
| Coût logiciel | 0€ (Word) | 0€ (gratuit) | **0€** |
| Délai d'envoi | 24-48h | Immédiat | **Instantané** |

**ROI Financier** :  
Si Marc valorise son temps à 40€/h (tarif horaire plombier), il économise **2 880€ par an** en temps admin.

## 💻 Extrait de Code

Voici une version simplifiée de la logique principale :

```python
import gspread
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from google.oauth2.service_account import Credentials
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def generer_facture(client_nom, prestations, montant_ht):
    """
    Génère une facture PDF
    """
    # Calculs automatiques
    tva_taux = 0.20
    montant_tva = montant_ht * tva_taux
    montant_ttc = montant_ht + montant_tva
    
    # Numéro de facture auto-incrémenté
    numero_facture = obtenir_prochain_numero()
    
    # Création du PDF
    pdf_filename = f"Facture_{numero_facture}_{client_nom}.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    
    # Header avec logo
    c.drawString(50, 800, "Marc Plomberie - Marseille")
    c.drawString(50, 780, f"Facture N° {numero_facture}")
    
    # Informations client
    c.drawString(50, 700, f"Client: {client_nom}")
    
    # Détail prestations (simplifié ici)
    c.drawString(50, 650, f"Prestations: {prestations}")
    
    # Totaux
    c.drawString(400, 300, f"Total HT: {montant_ht:.2f} €")
    c.drawString(400, 280, f"TVA (20%): {montant_tva:.2f} €")
    c.drawString(400, 260, f"Total TTC: {montant_ttc:.2f} €")
    
    c.save()
    return pdf_filename

def envoyer_facture_par_email(destinataire, pdf_path):
    """
    Envoie la facture par Gmail
    """
    # Utilisation de l'API Gmail
    # (Code simplifié - la vraie implémentation utilise OAuth2)
    message = f"""
    Bonjour,
    
    Veuillez trouver ci-joint votre facture pour l'intervention du {date}.
    
    Merci pour votre confiance !
    Marc - Marc Plomberie
    """
    # Envoi via Gmail API...
    print(f"Facture envoyée à {destinataire}")

# Déclenchement depuis Google Sheets
def traiter_ligne_sheets(ligne_id):
    # Connexion Google Sheets
    gc = gspread.service_account(filename='credentials.json')
    sheet = gc.open("Factures").sheet1
    
    # Récupération des données
    row = sheet.row_values(ligne_id)
    client_nom = row[1]
    client_email = row[2]
    prestations = row[3]
    montant_ht = float(row[4])
    
    # Génération et envoi
    pdf = generer_facture(client_nom, prestations, montant_ht)
    envoyer_facture_par_email(client_email, pdf)
    
    # Marquer comme "Envoyée" dans Sheets
    sheet.update_cell(ligne_id, 6, "✅ Envoyée")

```

**Note** : Il s'agit d'une version éducative simplifiée. Le script réel gère aussi :
- Les mentions légales automatiques
- Les pénalités de retard
- Les conditions de paiement
- Le multi-devise (rares clients pros)

## 🗣️ Retour du Client

> "Franchement, je ne pensais pas qu'un truc pareil était possible sans payer un abonnement. Maintenant je fais mes factures le soir en 30 minutes au lieu de 2h. Et mes clients reçoivent leur facture tout de suite, donc je suis payé plus vite. C'est vraiment un game-changer."  
> — Marc, plombier (3 mois après mise en place)

**Bénéfices collatéraux** (non anticipés) :
- Meilleure image professionnelle (emails et PDF plus propres)
- Paiements plus rapides (envoi immédiat au lieu de J+2)
- Traçabilité parfaite (tout archivé et retrouvable en 10 secondes)

## 🎓 Ce Que Vous Pouvez Retenir

**Applicable à** : 
- Artisans (électriciens, peintres, menuisiers)
- Professions libérales (formateurs, consultants)
- Auto-entrepreneurs avec facturation récurrente
- TPE qui génèrent 20+ factures par mois

**Points clés** :
1. **Pas besoin d'un logiciel SaaS payant** si vos besoins sont simples et que vous avez accès à un dev
2. **Google Sheets est un excellent front-end** pour les non-tech
3. **L'automatisation ne doit pas être complexe** - ici c'est <200 lignes de code
4. **Le ROI est immédiat** - dès le premier mois, c'est rentable

**Coût total de la solution** :
- Développement initial : 8h de travail (facturé à prix ami car cas d'étude)
- Coût mensuel : 0€ (tout gratuit : Google APIs, Python, Gmail)
- Maintenance : 0€ (Marc m'appelle si bug, mais rien depuis 4 mois)

## 🚀 Envie d'Aller Plus Loin ?

Cette solution peut être adaptée à **votre métier** avec :
- Devis automatiques (pas que factures)
- Relances de paiement automatiques
- Synchronisation avec votre banque
- Génération de statistiques mensuelles

---

**Intéressé par une solution similaire pour votre activité ?**  
[Contactez-moi](/contact) pour un **audit gratuit** de vos processus répétitifs. Je vous dirai ce qui est automatisable et le temps que vous pourriez gagner.

**Vous êtes développeur ?** Le code complet (anonymisé) est disponible sur demande pour inspiration.
