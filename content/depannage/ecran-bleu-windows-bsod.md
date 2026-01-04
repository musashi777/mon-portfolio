---
title: "Écran Bleu Windows (BSOD) : Diagnostic et Résolution en 8 Étapes"
date: 2026-01-03
description: "Votre PC affiche un écran bleu et redémarre ? Découvrez comment identifier la cause exacte (matériel, pilote, système) et résoudre définitivement le problème."
tags: ["Windows", "Écran Bleu", "BSOD", "Crash", "Blue Screen"]
---

## 🔍 Le Problème

L'**écran bleu de la mort** (BSOD - Blue Screen of Death) est le cauchemar de tout utilisateur Windows. Votre PC plante brutalement, affiche un écran bleu avec un code d'erreur cryptique, et redémarre. Parfois ça arrive une fois par mois, parfois 10 fois par jour.

**Symptômes typiques** :
- Écran bleu soudain avec message "Votre PC a rencontré un problème"
- Code d'erreur du type : `CRITICAL_PROCESS_DIED`, `MEMORY_MANAGEMENT`, `DRIVER_IRQL_NOT_LESS_OR_EQUAL`
- Redémarrage automatique (parfois trop rapide pour lire le message)
- Peut survenir : au démarrage, en utilisation normale, pendant un jeu, aléatoirement

## ⚙️ Diagnostic : Identifier la Cause

Les écrans bleus ont **toujours** une cause précise. Il faut la trouver.

### Étape 1 : Lire le Code d'Erreur

Si l'écran bleu passe trop vite :

1. **Désactiver le redémarrage automatique** :
   - Clic droit sur "Ce PC" → Propriétés → Paramètres système avancés
   - Onglet "Avancé" → Démarrage et récupération → Paramètres
   - **Décochez** "Redémarrer automatiquement"
   - Validez

2. **Provoquer le crash** (si reproductible) :
   - Lancez l'action qui cause le BSOD
   - Notez le **code d'erreur** (ex: `MEMORY_MANAGEMENT`)
   - Prenez une photo avec votre téléphone

### Étape 2 : Analyser les Fichiers Dump

Windows crée un fichier de "crash dump" à chaque BSOD. Il contient la cause exacte.

**Télécharger BlueScreenView** (gratuit) :

1. Allez sur [nirsoft.net/utils/blue_screen_view.html](https://www.nirsoft.net/utils/blue_screen_view.html)
2. Téléchargez et décompressez
3. Lancez `BlueScreenView.exe`

**Analyser le dump** :

- Vous voyez tous vos écrans bleus récents
- Colonne **"Caused By Driver"** = le coupable !
- Exemples :
  - `ntoskrnl.exe` → Problème système Windows ou RAM
  - `nvlddmkm.sys` → Pilote carte graphique NVIDIA
  - `atikmdag.sys` → Pilote carte graphique AMD
  - `Netwtw10.sys` → Pilote WiFi Intel

**Notez le fichier incriminé** - on va le corriger.

---

## ✅ Solutions par Type de Cause

### Cas 1 : Pilote Défectueux (70% des BSOD)

**Code typique** : `DRIVER_IRQL_NOT_LESS_OR_EQUAL`, `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED`  
**Fichier** : `.sys` (driver) autre que `ntoskrnl.exe`

**Difficulté** : 🟡 Intermédiaire  
**Impact** : ⭐⭐⭐⭐⭐ Résout 70% des cas

#### Solution A : Mettre à Jour le Pilote

1. **Identifier le type de pilote** :
   - Carte graphique : `nvlddmkm.sys` (NVIDIA), `atikmdag.sys` (AMD), `igdkmd64.sys` (Intel)
   - WiFi/Réseau : `Netwtw*.sys`, `rt*.sys`
   - Autre : Cherchez le nom du fichier sur Google

2. **Télécharger le pilote officiel** :
   - **NVIDIA** : [https://www.nvidia.com/Download/index.aspx](https://www.nvidia.com/Download/index.aspx)
   - **AMD** : [https://www.amd.com/support](https://www.amd.com/support)
   - **Intel WiFi** : [https://downloadcenter.intel.com](https://downloadcenter.intel.com)

3. **Installer en "mode sans échec"** (plus sûr) :
   - Redémarrez en maintenant `Shift` + clic sur "Redémarrer"
   - Dépannage → Options avancées → Paramètres de démarrage → Redémarrer
   - Appuyez sur `4` ou `F4` (Mode sans échec)
   - Installez le nouveau pilote
   - Redémarrez normalement

#### Solution B : Revenir à un Ancien Pilote

Si le problème a commencé après une mise à jour Windows/pilote :

1. **Gestionnaire de périphériques** :
   - `Win + X` → Gestionnaire de périphériques
2. **Localiser le périphérique problématique**
3. **Clic droit → Propriétés → Pilote → Revenir à la version précédente**
4. Redémarrez

#### Solution C : Désinstaller Temporairement

En dernier recours :

1. Mode sans échec (voir ci-dessus)
2. Gestionnaire de périphériques → Désinstaller le périphérique problématique
3. Redémarrez (Windows réinstallera un pilote générique)
4. Si le BSOD disparaît = le pilote était en cause

---

### Cas 2 : Problème de RAM (15% des BSOD)

**Code typique** : `MEMORY_MANAGEMENT`, `PAGE_FAULT_IN_NONPAGED_AREA`, `KMODE_EXCEPTION_NOT_HANDLED`  
**Fichier** : Souvent `ntoskrnl.exe`

**Difficulté** : 🟡 Intermédiaire  
**Impact** : ⭐⭐⭐⭐ Très efficace si c'est la RAM

#### Test de la RAM

**Méthode 1 : Windows Memory Diagnostic** (intégré)

1. Appuyez sur `Win + R`
2. Tapez `mdsched.exe` et validez
3. Choisissez "Redémarrer maintenant et vérifier"
4. Le PC redémarre et teste la RAM (10-20 min)
5. Résultat affiché au redémarrage

**Méthode 2 : MemTest86** (plus fiable)

1. Téléchargez sur [memtest.org](https://www.memtest.org)
2. Créez une clé USB bootable
3. Démarrez dessus
4. Laissez tourner **au moins 2 passes** (peut prendre 2-6h)
5. Si **1 seule erreur** détectée = RAM défectueuse

#### Si RAM Défectueuse

**Option A : Identifier la barrette coupable**

1. Éteignez le PC
2. Enlevez toutes les barrettes sauf une
3. Démarrez et utilisez normalement 1-2 jours
4. Si BSOD → Cette barrette est coupable
5. Si OK → Testez la suivante

**Option B : Remplacer la RAM**

- Notez le type de RAM : `Win + Pause` → Système → RAM
- Achetez une barrette compatible (même DDR4/DDR5, même fréquence)
- Coût : 30-60€ pour 8 Go

⚠️ **RAM sous garantie ?** Si PC < 2 ans, contactez le fabricant.

---

### Cas 3 : Disque Dur Défaillant (10% des BSOD)

**Code typique** : `CRITICAL_PROCESS_DIED`, `UNEXPECTED_STORE_EXCEPTION`

**Difficulté** : 🟢 Facile (diagnostic) / 🔴 Avancé (remplacement)  
**Impact** : ⭐⭐⭐⭐⭐ Critique si disque en panne

#### Test du Disque

**Méthode 1 : CrystalDiskInfo** (gratuit)

1. Téléchargez sur [crystalmark.info](https://crystalmark.info/en/software/crystaldiskinfo/)
2. Installez et lancez
3. Regardez l'**état de santé** :
   - 🟢 **Bon** : OK
   - 🟡 **Attention** : Sauvegardez vos données !
   - 🔴 **Bad** : Remplacez IMMÉDIATEMENT

**Méthode 2 : CHKDSK** (Windows)

1. Ouvrez PowerShell en Admin
2. Tapez :
   ```powershell
   chkdsk C: /F /R
   ```
3. Confirmez le redémarrage
4. Laissez la vérification se faire (30 min - 3h)

#### Si Disque Défaillant

**Urgence** :

1. **Sauvegardez VOS DONNÉES** (USB externe, Cloud)
2. **Remplacez le disque** :
   - HDD → SSD : Énorme gain de performance
   - SSD défaillant → Nouveau SSD
3. **Réinstallez Windows** sur le nouveau disque

**Coût** : SSD 500 Go = 40-60€

---

### Cas 4 : Surchauffe (3% des BSOD)

**Code typique** : Aléatoire, surtout pendant les jeux ou tâches lourdes

**Difficulté** : 🟡 Intermédiaire  
**Impact** : ⭐⭐⭐ Efficace si c'est la cause

#### Surveiller la Température

**HWMonitor** (gratuit) :

1. Téléchargez sur [cpuid.com/softwares/hwmonitor.html](https://www.cpuid.com/softwares/hwmonitor.html)
2. Lancez et regardez les températures :
   - **CPU** : <80°C en charge = OK / >90°C = Trop chaud
   - **GPU** : <85°C en jeu = OK / >95°C = Trop chaud

#### Si Surchauffe

**Solution rapide** :

1. **Nettoyer les ventilateurs** :
   - Éteignez le PC
   - Ouvrez le boîtier
   - Bombe à air comprimé (10€ en magasin)
   - Soufflez sur les ventilateurs CPU, GPU, alimentation

2. **Améliorer la ventilation** :
   - Enlevez le PC du sol (sur le bureau)
   - Éloignez-le des murs (10 cm minimum)
   - Ouvrez le panneau latéral temporairement

**Solution long terme** :

- Changer la pâte thermique du CPU (si PC > 3 ans)
- Ajouter des ventilateurs boîtier (10€/pièce)

---

### Cas 5 : Logiciel Incompatible (2% des BSOD)

**Code typique** : Variable  
**Coupable** : Antivirus tiers, VPN, RGB software, overclocking

**Difficulté** : 🟢 Facile  
**Impact** : ⭐⭐⭐ Efficace si logiciel récent

#### Désinstaller les Suspects

**Antivirus tiers** :
- Avast, AVG, Norton, McAfee peuvent causer des BSOD
- Désinstallez et utilisez Windows Defender (intégré et excellent)

**Logiciels d'overclocking** :
- MSI Afterburner, EVGA Precision
- Désactivez ou désinstallez

**RGB Control** :
- Corsair iCUE, ASUS Aura, etc.
- Mettez à jour ou désinstallez

---

## 🎯 Plan d'Action Complet

Si vous ne savez pas par où commencer :

### Semaine 1 : Diagnostic

1. ✅ Activer l'affichage de l'écran bleu (désactiver reboot auto)
2. ✅ Installer BlueScreenView
3. ✅ Identifier le fichier .sys coupable
4. ✅ Tester la RAM (MemTest86)
5. ✅ Tester le disque (CrystalDiskInfo)

### Semaine 2 : Corrections

6. ✅ Mettre à jour TOUS les pilotes (carte graphique, WiFi, chipset)
7. ✅ Nettoyer le PC (poussière)
8. ✅ Mettre à jour le BIOS (si > 2 ans)

### Si ça Persiste

9. ⬜ Réinstallation propre de Windows (solution ultime)

---

## 💡 Prévention

- **Mettez à jour Windows** régulièrement (mais testez les pilotes après)
- **Ne laissez pas la poussière s'accumuler** (nettoyage tous les 6 mois)
- **Utilisez un onduleur** (protège des coupures électriques)
- **Évitez l'overclocking** si vous n'êtes pas expert

---

## ⚠️ Quand Faire Appel à un Pro ?

Contactez un technicien si :
- Les BSOD sont **quotidiens** et aléatoires
- Vous avez **remplacé RAM + testé disque** sans succès
- Le code d'erreur pointe vers `ntoskrnl.exe` mais RAM OK
- Vous n'êtes **pas à l'aise** avec l'ouverture du PC

---

**BSOD impossible à résoudre ?** Envoyez-moi une photo de l'écran bleu et le fichier BlueScreenView via **[mon diagnostic gratuit](/diagnostic)**.  
Je vous dirai **exactement** quelle pièce/pilote est en cause et comment le corriger. Réponse sous 4h !
