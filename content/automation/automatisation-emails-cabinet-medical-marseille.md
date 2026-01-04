---
title: "Automatisation des Emails pour un Cabinet Médical : -15h par Semaine"
date: 2026-01-03
description: "Comment un cabinet médical de 3 praticiens a automatisé 80% de sa gestion d'emails grâce à Gmail Filters, Google Apps Script et Zapier."
client: "Cabinet médical - 13006 Marseille"
technologies: ["Gmail API", "Google Apps Script", "Zapier", "Google Sheets"]
resultats:
  - valeur: "15h"
    label: "Économisées par semaine"
  - valeur: "80%"
    label: "Emails traités auto"
  - valeur: "12€"
    label: "Coût mensuel"
---

## 🎯 Le Contexte

**Dr. Sophie L.** (nom anonymisé), médecin généraliste à Marseille 13006, gère un cabinet avec 2 autres praticiens. Comme beaucoup de professionnels de santé, elle croule sous les **emails administratifs** qui n'ont rien à voir avec le médical.

### La Problématique Initiale

> "J'ai créé mon cabinet il y a 3 ans. Au début, 20 emails par jour, gérable. Maintenant, c'est 150 emails quotidiens : demandes de RDV, résultats de labo, confirmations pharmacie, factures, spam... Je passe 3 heures par jour juste à trier mes mails. C'est du temps que je ne consacre pas aux patients."

**Temps perdu** : **15 heures par semaine** (3h par jour × 5 jours)  
**Tâches répétitives** :
- Transférer les demandes de RDV à la secrétaire
- Classer les résultats de labo par patient
- Archiver les factures fournisseurs
- Supprimer les emails promotionnels
- Répondre aux questions récurrentes (horaires, tarifs, etc.)

**Impact métier** :
- Temps médical cannibalisé par l'admin
- Stress quotidien ("inbox à 387 non lus")
- Emails importants noyés dans la masse

**Points de friction** :
- Utilise Gmail (pas Outlook)
- Emails reçus sur 3 adresses différentes (cabinet, perso, urgences)
- Pas de budget pour logiciel médical complet (type Doctolib intégré)
- Besoin de solution compatible téléphone (iPhone)

## 🔧 La Solution Technique

Au lieu d'un CRM médical à 200€/mois, j'ai créé une **solution d'automatisation par filtrage intelligent** basée sur Gmail.

### Architecture

```
Gmail (Réception)
  ↓
Filtres Gmail (Tri automatique)
  ↓
Google Apps Script (Actions automatiques)
  ↓
Zapier (Intégrations tierces)
  ↓
Résultat : Inbox à 20 emails/jour au lieu de 150
```

**Workflow final** :

1. **Email reçu** → Gmail l'analyse via filtres
2. **Selon l'expéditeur/sujet** :
   - Demande RDV → Transférée auto à secrétaire + label "RDV"
   - Résultat labo → Archivé dans Drive par patient + notification SMS
   - Facture fournisseur → Envoyée à la comptable + Google Sheets
   - Email promo → Supprimé automatiquement
   - Email patient → Reste dans inbox (traité manuellement)
3. **Inbox finale** : Seulement les emails vraiment importants

### Technologies Utilisées

- **Gmail Filters** : Tri automatique (gratuit, natif Gmail)
- **Google Apps Script** : Automatisations avancées (JavaScript pour Google Workspace)
- **Zapier** : Connecter Gmail à d'autres services (SMS, Sheets, etc.)
- **Google Drive** : Stockage automatique des pièces jointes
- **Google Sheets** : Tableau de bord des factures

**Pourquoi cette stack ?**
- **100% Cloud** : Accessible depuis n'importe où (cabinet, maison, téléphone)
- **Gratuit à 95%** : Seul Zapier coûte 12€/mois (plan Starter)
- **Pas d'installation** : Tout fonctionne dans le navigateur
- **RGPD-compliant** : Google Workspace certifié santé

### Fonctionnalités Clés

#### 1. Tri Automatique des Emails

**Filtres Gmail créés** (35 au total) :

| Type d'Email | Expéditeur/Mots-clés | Action Automatique |
|--------------|---------------------|-------------------|
| Demande RDV | "rendez-vous", "consultation" | → Label "RDV" + Transfert secrétaire |
| Résultat labo | `laboratoire@*.fr` | → Label "Labo" + Archive + Notif |
| Ordonnance digitale | "DocAvenue", "MédiClick" | → Label "Ordonnances" |
| Facture | "facture", "devis", ".pdf" | → Label "Compta" + Sheets |
| Promo/Spam | "promo", "offre", "casino" | → Suppression auto |
| CPAM/Sécu | `@ameli.fr`, `@assure...` | → Label "CPAM" + Important |

**Création d'un filtre type** :
```
De : *laboratoire*
Contient : "résultat" OU "analyse"
Action :
  - Appliquer le libellé : Labo/[NomPatient]
  - Transférer à : archivage@cabinet-sophie.fr
  - Marquer comme lu
  - Ignorer la boîte de réception
```

#### 2. Extraction Automatique des Pièces Jointes

**Script Google Apps Script** (s'exécute toutes les heures) :

```javascript
function archiveLabResults() {
  // Cherche les emails avec label "Labo" et pièce jointe
  var threads = GmailApp.search('label:Labo has:attachment newer_than:1d');
  
  threads.forEach(function(thread) {
    var messages = thread.getMessages();
    
    messages.forEach(function(message) {
      var attachments = message.getAttachments();
      var subject = message.getSubject();
      
      // Extrait le nom du patient du sujet (format: "Résultats - DUPONT Jean")
      var patientName = extractPatientName(subject);
      
      // Crée/trouve le dossier dans Drive
      var folder = getOrCreatePatientFolder(patientName);
      
      // Sauvegarde les pièces jointes
      attachments.forEach(function(attachment) {
        folder.createFile(attachment);
      });
      
      // Envoie une notification SMS au médecin via Zapier webhook
      notifyDoctor(patientName, "Résultats labo reçus");
      
      // Archive l'email
      thread.moveToArchive();
    });
  });
}

function extractPatientName(subject) {
  // Regex pour extraire "NOM Prénom" du sujet
  var match = subject.match(/([A-Z]+)\s+([A-Z][a-z]+)/);
  return match ? match[0] : "Inconnu";
}

function getOrCreatePatientFolder(patientName) {
  var rootFolder = DriveApp.getFolderById('ID_DOSSIER_PATIENTS');
  var folders = rootFolder.getFoldersByName(patientName);
  
  if (folders.hasNext()) {
    return folders.next();
  } else {
    return rootFolder.createFolder(patientName);
  }
}

function notifyDoctor(patient, message) {
  // Webhook Zapier qui envoie SMS
  var url = 'https://hooks.zapier.com/hooks/catch/XXXXX/';
  var payload = {
    patient: patient,
    message: message
  };
  
  UrlFetchApp.fetch(url, {
    method: 'post',
    contentType: 'application/json',
    payload: JSON.stringify(payload)
  });
}
```

**Ce script** :
- Tourne automatiquement toutes les heures (trigger Apps Script)
- Trouve les emails "Labo" reçus dans les dernières 24h
- Extrait les PDF joints
- Les range dans Drive : `/Patients/DUPONT Jean/Résultats Labo/`
- Envoie un SMS au médecin : "Résultats labo reçus pour DUPONT Jean"

#### 3. Tableau de Bord des Factures

**Zapier automation** :

```
Trigger : Nouvel email Gmail avec label "Compta"
   ↓
Action 1 : Extraire la pièce jointe PDF
   ↓
Action 2 : Envoyer PDF à la comptable par email
   ↓
Action 3 : Ajouter ligne dans Google Sheets "Factures 2026"
   - Colonnes : Date | Fournisseur | Montant | Statut | Lien PDF
```

**Google Sheets résultant** :

| Date | Fournisseur | Montant | Statut | PDF |
|------|------------|---------|--------|-----|
| 03/01/26 | Matériel Médical Pro | 450€ | À payer | [Lien] |
| 02/01/26 | EDF | 120€ | Payé | [Lien] |

**Avantage** : La comptable a une vue d'ensemble sans fouiller les emails.

#### 4. Réponses Automatiques (Canned Responses)

Pour les questions récurrentes, **Gmail Canned Responses** :

**Question** : "Quels sont vos horaires ?"  
**Réponse auto** :
```
Bonjour,

Nos horaires de consultation :
- Lundi à Vendredi : 9h - 12h30 / 14h - 18h
- Samedi : 9h - 12h (urgences uniquement)

Pour prendre RDV : 04 XX XX XX XX ou via Doctolib.

Cordialement,
Cabinet Dr. Sophie L.
```

**Configuration** :
- Gmail → Paramètres → Avancé → Activer "Réponses standardisées"
- Créer 10 réponses types (horaires, tarifs, secteur 1/2, CMU, etc.)
- Utilisation : 2 clics au lieu de retaper 50 fois

---

## 📊 Résultats Mesurables

### Avant / Après (6 mois d'utilisation)

| Métrique | Avant | Après | Gain |
|----------|-------|-------|------|
| Emails reçus/jour | 150 | 150 | - |
| Emails inbox/jour | 150 | **20** | **-87%** |
| Temps tri emails | 3h/jour | 20 min/jour | **-87%** |
| Temps hebdo total | 15h | **1h40** | **13h20 gagnées** |
| Emails manqués/mois | 5-8 | **0** | **100%** |
| Stress "inbox" | 😰 | 😌 | Inestimable |

**ROI Financier** :

Si Dr. Sophie valorise son temps à **80€/h** (tarif consultation) :
- **13,3h × 80€ = 1 064€ économisés par semaine**
- **4 256€ par mois**
- **51 072€ par an**

**Coût de la solution** :
- Développement initial : 12h de travail (900€ facturé)
- Coût mensuel : 12€ (Zapier)
- **ROI atteint en 1 semaine**

### Bénéfices Non Mesurables

- **Sérénité mentale** : Plus de panique "inbox saturée"
- **Réactivité** : Résultats labo archivés avant même que le médecin les voie
- **Professionnalisme** : Réponses instantanées aux patients
- **Mobilité** : Tout fonctionne sur iPhone

---

## 🗣️ Retour du Client

> "C'est magique. Avant, j'ouvrais ma boîte mail avec appréhension. Maintenant, je sais que seuls les emails vraiment importants sont là. Les résultats de labo sont classés automatiquement, les factures vont directement à ma comptable... J'ai récupéré 13 heures par semaine. C'est presque une après-midi de consultations en plus !"  
> — Dr. Sophie L., 6 mois après mise en place

**Chiffre clé inattendu** : 
Le cabinet a pu **prendre 8 patients supplémentaires par semaine** grâce au temps libéré. Soit **+2 500€ de CA mensuel** en plus des économies de temps admin.

---

## 🎓 Ce Que Vous Pouvez Retenir

**Applicable à** :
- Professions libérales (médecins, avocats, architectes, kinés)
- TPE avec volume email élevé (>50/jour)
- Toute activité avec emails répétitifs et prévisibles
- Entrepreneurs submergés par l'admin

**Points clés** :

1. **Gmail gratuit >> CRM payant** pour beaucoup de cas d'usage
2. **Automatiser ne veut pas dire "tout robot"** : On automatise le triable, on garde l'humain pour le reste
3. **Zapier = connecteur universel** : Gmail → SMS, Sheets, Slack, WhatsApp, etc.
4. **Le temps admin n'est PAS une fatalité**

### Autres Cas d'Usage Similaires

Cette solution a été adaptée pour :
- **Cabinet d'avocat** : Tri automatique affaires par client
- **Agence immobilière** : Demandes de visite → CRM automatique
- **Formateur indépendant** : Demandes de devis → Google Sheets → Relance auto

---

## 🚀 Envie d'Aller Plus Loin ?

**Extensions possibles** :
- **OCR sur factures** : Extraction auto du montant/fournisseur (Google Cloud Vision API)
- **IA de classification** : GPT-4 classe les emails ambigus
- **Intégration agenda** : RDV détectés → Ajout auto dans Google Calendar
- **Webhook Slack** : Notification équipe médicale sur canal dédié

**Coût supplémentaire** : Quasi nul (APIs Google gratuites jusqu'à 1000 requêtes/jour)

---

**Professionnel libéral submergé par les emails ?**  
[Contactez-moi](/contact) pour un **audit gratuit** de votre boîte mail. Je vous dirai précisément :
- Quels % d'emails sont automatisables
- Quelle solution technique adopter (Gmail, Outlook, autre)
- Le temps que vous pourriez gagner par semaine
- Un devis si vous voulez que je l'implémente

**Vous êtes développeur ?** Le code complet (Apps Script + config Zapier) est disponible sur demande pour inspiration.

---

*Note RGPD* : Cette solution respecte le RGPD et le secret médical. Les données patients restent dans Google Workspace (certifié HDS - Hébergeur de Données de Santé). Aucune donnée n'est partagée avec Zapier (seules métadonnées : "email reçu" sans contenu médical).
