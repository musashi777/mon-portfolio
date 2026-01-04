# 🚀 Guide de la Nouvelle Architecture du Site

## 📋 Vue d'Ensemble

Votre site a été restructuré selon la stratégie "Cocons Sémantiques" pour maximiser le SEO et la conversion **avant** votre création d'entreprise.

### Nouvelles Sections Créées

| Section | URL | Objectif | Public |
|---------|-----|----------|--------|
| **Dépannage** | `/depannage` | Guides pratiques résolution problèmes | B2C (particuliers) |
| **Automation** | `/automation` | Études de cas automatisation/IA | B2B (artisans, TPE) |
| **Marseille** | `/marseille` | Actualités tech locales | Local SEO |
| **Diagnostic** | `/diagnostic` | Page de capture avec formulaire | Conversion |

---

## 🎨 Layouts Personnalisés

Chaque section a son propre design et Call-to-Action (CTA) :

### 1. Layout Dépannage (`/layouts/depannage/single.html`)
- **Badge bleu** : "Guide de Dépannage"
- **Temps de lecture** affiché
- **CTA** : "Diagnostic Gratuit" (vers `/diagnostic`)
- **Design** : Pédagogique, rassurant

### 2. Layout Automation (`/layouts/automation/single.html`)
- **Badge dégradé violet-rose** : "Étude de Cas - Automatisation"
- **Résultats chiffrés** en tête d'article (si définis dans front matter)
- **CTA** : "Parlons de votre projet" (vers `/contact`)
- **Design** : Professionnel, tech

### 3. Layout Marseille (`/layouts/marseille/single.html`)
- **Badge orange-rouge** : "Marseille Tech"
- **Quartiers affichés** automatiquement
- **Système d'alerte urgence** (si `urgent: true`)
- **Design** : News, actualité

### 4. Layout Diagnostic (`/layouts/diagnostic/single.html`)
- **Full-width** (pas de sidebar)
- **Section réassurance** (certifications, stats)
- **FAQ intégrée** (détails dépliables)
- **Iframe Tally.so** prête à l'emploi

---

## ✍️ Comment Créer un Nouvel Article

### Méthode 1 : Utiliser les Archetypes (Recommandé)

```bash
# Pour un guide de dépannage
hugo new depannage/nom-du-probleme.md --kind depannage

# Pour une étude de cas automation
hugo new automation/nom-du-cas.md --kind automation

# Pour une actualité Marseille
hugo new marseille/nom-actualite.md --kind marseille
```

Les archetypes (`/archetypes/*.md`) génèrent automatiquement la structure complète !

### Méthode 2 : Copier un Exemple

Vous avez 3 exemples complets dans :
- `/content/depannage/pc-lent-demarrage-windows-11.md`
- `/content/automation/facturation-automatisee-plombier-marseille.md`
- `/content/marseille/test-debit-fibre-marseille-13008.md`

Copiez-les et modifiez le contenu.

---

## 🎯 Front Matter Important

### Pour Dépannage
```yaml
---
title: "Titre du problème"
date: 2026-01-03
description: "Résumé SEO"
tags: ["Windows", "Réseau", etc.]
---
```

### Pour Automation
```yaml
---
title: "Titre du cas"
date: 2026-01-03
description: "Résumé"
client: "Type d'entreprise"
technologies: ["Python", "API", "Excel"]
resultats:
  - valeur: "10h"
    label: "Économisées par semaine"
  - valeur: "100%"
    label: "Automatisation"
---
```

### Pour Marseille
```yaml
---
title: "Titre de l'actu"
date: 2026-01-03
description: "Résumé"
quartier: ["Bonneveine", "13008"]
urgent: false  # true si info urgente
---
```

---

## 📝 Configuration Tally.so (Page Diagnostic)

### Étape 1 : Créer le Formulaire sur Tally.so

1. Aller sur [tally.so](https://tally.so) (gratuit)
2. Créer un formulaire avec ces champs :
   - **Type d'appareil** : Choix multiple (PC, Mac, iPhone, Android, Réseau)
   - **Symptôme** : Choix multiple (Lent, Ne démarre pas, Virus, Écran bleu, WiFi)
   - **Description** : Texte long
   - **Photos** : Upload de fichier (Tally le permet nativement !)
   - **Nom** : Texte court
   - **Email** : Email
   - **Téléphone (optionnel)** : Téléphone

3. **Logique conditionnelle** (optionnelle) :
   - Si "PC" → Demander "Windows ou Linux ?"
   - Si "Virus" → Ajouter question "Avez-vous un antivirus ?"

### Étape 2 : Récupérer le Code d'Intégration

1. Cliquez sur "Share" dans Tally
2. Choisissez "Embed"
3. Copiez le code iframe

### Étape 3 : Intégrer dans Hugo

Ouvrez `/content/diagnostic.md` et remplacez :

```html
<iframe 
  src="https://tally.so/embed/YOUR_FORM_ID?alignLeft=1&hideTitle=1&transparentBackground=1" 
  ...
```

Par votre iframe Tally (remplacez `YOUR_FORM_ID`).

**Options recommandées** :
- `?alignLeft=1` : Alignement à gauche
- `&hideTitle=1` : Cache le titre Tally (vous en avez déjà un dans Hugo)
- `&transparentBackground=1` : Fond transparent pour intégration fluide

---

## 🎨 Navigation Menu

Le menu (`/hugo.toml`) contient maintenant :

1. Projets
2. **Dépannage** (nouveau)
3. **Automation** (nouveau)
4. **Marseille** (nouveau)
5. Blog (ancien contenu)
6. Certifications
7. À Propos
8. Contact
9. **🔧 Diagnostic Gratuit** (nouveau, avec emoji pour visibilité)

---

## 📊 Stratégie de Contenu Recommandée

### Phase 1 : Fondations (Semaine 1-2)

**Créer 3 articles piliers** :

1. **Dépannage** : "Guide Complet du Diagnostic PC - 50 Problèmes Résolus"
   - Arbre de décision interactif
   - CTA tous les 3 problèmes vers `/diagnostic`

2. **Automation** : "J'ai Automatisé [Tâche] d'un [Métier] à Marseille"
   - Code source (GitHub Gist)
   - Vidéo démo (Loom gratuit)

3. **Marseille** : "Guide Technique du Télétravail à Marseille"
   - Tests débit par quartier
   - Carte interactive (Google My Maps)

### Phase 2 : Amplification (Semaine 3-4)

**Partager stratégiquement** :
- LinkedIn : Articles automation (B2B)
- Facebook : Articles Marseille dans groupes locaux
- Site perso : Liens internes entre sections

**Recueillir diagnostics** :
- Répondre sous 4h (engagement tenu = confiance)
- Garder les emails pour newsletter future

### Phase 3 : Basculement Commercial (Après création entreprise)

**Modifier CTAs** :
- Dépannage → "Prendre RDV sur Marseille"
- Automation → "Demande de devis"
- Diagnostic → Ajout tarifs indicatifs

**Activer** :
- Google Business Profile
- Bouton WhatsApp flottant
- Calendly pour prises de RDV

---

## 🔧 Commandes Hugo Utiles

```bash
# Créer un article dépannage
hugo new depannage/mon-article.md --kind depannage

# Créer un article automation
hugo new automation/mon-cas.md --kind automation

# Créer un article Marseille
hugo new marseille/mon-actu.md --kind marseille

# Lancer le serveur local
hugo server -D

# Build pour production
hugo --minify
```

---

## 📈 Tracking & Optimisation

### À Installer (Gratuit)

1. **Google Analytics 4** : Suivre le trafic
2. **Google Search Console** : Suivre les positions SEO
3. **Tally Analytics** : Suivre les soumissions de diagnostic

### KPIs à Surveiller

- **Trafic organique** : Utilisateurs venant de Google
- **Pages vues par section** : Dépannage vs Automation vs Marseille
- **Taux de conversion diagnostic** : % visiteurs qui remplissent le formulaire
- **Temps passé** : >2 min = engagement
- **Mots-clés acquis** : Suivre positions dans Search Console

---

## 🎯 Prochaines Étapes Recommandées

### Court Terme (Cette Semaine)

1. ✅ **Configurer Tally.so** et intégrer l'iframe
2. ✅ **Acheter votre nom de domaine** (important pour SEO)
3. ✅ **Créer 3 articles piliers** (1 par section)

### Moyen Terme (Ce Mois)

4. ⬜ **Publier 2 articles par semaine**
5. ⬜ **Partager dans groupes Facebook/LinkedIn locaux**
6. ⬜ **Répondre aux diagnostics sous 4h** (tenir promesse)
7. ⬜ **Créer Google Business Profile** (même avant Kbis, en "services")

### Long Terme (3 Mois)

8. ⬜ **50+ articles** (minimum 10 par section)
9. ⬜ **Newsletter email** (recueil via diagnostics)
10. ⬜ **Partenariats locaux** (coworking, associations Marseille)
11. ⬜ **Passage au commercial** (création entreprise, ajout tarifs)

---

## 🆘 Support

**Besoin d'aide avec cette structure ?**
- Documentation Hugo : [gohugo.io](https://gohugo.io)
- Tally.so Docs : [tally.so/help](https://tally.so/help)

**Questions techniques ?** Vérifiez :
- `/layouts/` : Tous les templates
- `/archetypes/` : Templates d'articles
- `/content/` : Tout le contenu
- `/hugo.toml` : Configuration globale

---

## 🎉 Félicitations !

Vous avez maintenant une **architecture solide** pour :
- ✅ Générer des leads **avant** votre création d'entreprise
- ✅ Démontrer votre expertise (E-E-A-T Google)
- ✅ Vous positionner localement sur Marseille
- ✅ Convertir visiteurs → diagnostics → clients

**Prêt à créer votre premier article ?** Utilisez les archetypes et inspirez-vous des exemples !

---

*Dernière mise à jour : 3 janvier 2026*
