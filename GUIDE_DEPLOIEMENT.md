# 📋 Guide de Déploiement - Portfolio Hugo sur Vercel

## 🎯 Objectif
Déployer votre portfolio Hugo gratuitement sur Vercel (ou alternative) pour le rendre accessible en ligne.

## 📊 Solutions Gratuites Recommandées

### **1. Vercel (Recommandé)**
- **Avantages** : Rapide, automatique, excellent pour Hugo
- **Limite gratuite** : Illimitée pour usage personnel
- **URL** : `votre-nom.vercel.app`

### **2. Netlify (Alternative)**
- **Avantages** : Facile, bon support Hugo
- **Limite gratuite** : 100GB/mois bande passante
- **URL** : `votre-nom.netlify.app`

### **3. GitHub Pages**
- **Avantages** : Intégration GitHub native
- **Limite gratuite** : 1GB stockage
- **URL** : `votre-nom.github.io`

---

## 🚀 Procédure Vercel (Recommandée)

### **Étape 1 : Préparer votre dépôt GitHub**

1. **Initialiser Git** (si pas déjà fait) :
```bash
git init
git add .
git commit -m "Initial commit - Portfolio Hugo"
```

2. **Créer un dépôt sur GitHub** :
   - Allez sur [github.com](https://github.com)
   - Créez un nouveau dépôt (ex: `mon-portfolio`)
   - Ne pas initialiser avec README

3. **Connecter votre projet** :
```bash
git remote add origin https://github.com/votre-nom/mon-portfolio.git
git branch -M main
git push -u origin main
```

### **Étape 2 : Configurer pour Vercel**

1. **Créer un fichier `vercel.json`** à la racine :
```json
{
  "buildCommand": "hugo --gc --minify",
  "outputDirectory": "public",
  "installCommand": "npm install -g hugo-extended"
}
```

2. **Mettre à jour `baseURL`** dans `hugo.toml` :
```toml
baseURL = "https://votre-nom.vercel.app/"
```

### **Étape 3 : Déployer sur Vercel**

1. **Aller sur [vercel.com](https://vercel.com)**
2. **S'inscrire avec GitHub**
3. **Importer votre dépôt**
4. **Configuration automatique** :
   - Framework Preset : Hugo
   - Build Command : `hugo --gc --minify`
   - Output Directory : `public`
5. **Cliquer sur "Deploy"**

### **Étape 4 : Configuration DNS (Optionnel)**

Pour un domaine personnalisé :
1. **Acheter un domaine** (ex: namecheap.com)
2. **Dans Vercel** : Settings → Domains
3. **Ajouter votre domaine**
4. **Configurer les DNS** chez votre registrar

---

## 🔧 Configuration Alternative : Netlify

### **Étape 1 : Préparer le déploiement**

1. **Créer un fichier `netlify.toml`** :
```toml
[build]
  publish = "public"
  command = "hugo --gc --minify"

[build.environment]
  HUGO_VERSION = "0.151.0"
```

2. **Mettre à jour `baseURL`** :
```toml
baseURL = "https://votre-nom.netlify.app/"
```

### **Étape 2 : Déployer sur Netlify**

1. **Aller sur [netlify.com](https://netlify.com)**
2. **S'inscrire avec GitHub**
3. **"New site from Git"**
4. **Choisir votre dépôt**
5. **Build settings automatiques** :
   - Build command: `hugo --gc --minify`
   - Publish directory: `public`
6. **"Deploy site"**

---

## ⚙️ Configuration Hugo Optimisée

### **Fichier `hugo.toml` final pour production** :
```toml
baseURL = "https://votre-nom.vercel.app/"
languageCode = "fr-fr"
title = "Portfolio de Stéphan Uniatowitz - Expert Support Technique & Infrastructure"
theme = "blowfish"

[params]
  description = "Portfolio technique de Stéphan Uniatowitz - Expert support N2/N3, réseaux et systèmes avec 85% de taux de résolution en environnements critiques"
  keywords = ["support technique", "réseaux", "systèmes", "GLPI", "VPN", "infrastructure", "technicien IT"]

[markup]
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true

# Menu de navigation
[[menu.main]]
  name = "Projets"
  url = "/projets"
  weight = 1
[[menu.main]]
  name = "Blog"
  url = "/blog"
  weight = 2
[[menu.main]]
  name = "À Propos"
  url = "/about"
  weight = 3
[[menu.main]]
  name = "Contact"
  url = "/contact"
  weight = 4
```

---

## 🛠️ Scripts Utiles

### **Script de build local** (`build.sh`) :
```bash
#!/bin/bash
hugo --gc --minify
echo "Site built in public/ directory"
```

### **Script de déploiement rapide** (`deploy.sh`) :
```bash
#!/bin/bash
hugo --gc --minify
git add .
git commit -m "Update portfolio"
git push origin main
echo "Pushed to GitHub - Vercel will auto-deploy"
```

---

## 🔍 Vérifications Pré-Déploiement

### **1. Test local** :
```bash
hugo server -D
# Vérifier http://localhost:1313/
```

### **2. Build de test** :
```bash
hugo --gc --minify
# Vérifier le dossier public/
```

### **3. Vérifier les liens** :
```bash
# Installer htmltest
brew install htmltest

# Tester les liens
htmltest public/
```

---

## 📈 Optimisations Recommandées

### **1. Performance** :
- Images optimisées (WebP format)
- CSS/JS minifiés
- Cache headers configurés

### **2. SEO** :
- Sitemap automatique (`/sitemap.xml`)
- Meta descriptions complètes
- Structure HTML sémantique

### **3. Sécurité** :
- HTTPS automatique
- Headers de sécurité
- Pas de données sensibles

---

## 🚨 Dépannage Courant

### **Problème** : Build échoue sur Vercel
**Solution** : Vérifier la version Hugo dans `vercel.json`

### **Problème** : Images ne s'affichent pas
**Solution** : Vérifier les chemins dans `static/images/`

### **Problème** : CSS/JS cassés
**Solution** : Vérifier `baseURL` et chemins relatifs

---

## ✅ Checklist de Déploiement

- [ ] Dépôt GitHub créé et synchronisé
- [ ] `baseURL` mis à jour pour production
- [ ] Fichier de configuration déploiement créé
- [ ] Test local réussi
- [ ] Build production réussi
- [ ] Déploiement Vercel/Netlify configuré
- [ ] Domaines configurés (optionnel)
- [ ] Redirections HTTPS vérifiées
- [ ] Analytics intégrés (optionnel)

---

## 📞 Support

- **Documentation Hugo** : https://gohugo.io/hosting-and-deployment/
- **Support Vercel** : https://vercel.com/docs
- **Support Netlify** : https://docs.netlify.com/

**Votre portfolio sera en ligne en moins de 10 minutes ! 🎉**
