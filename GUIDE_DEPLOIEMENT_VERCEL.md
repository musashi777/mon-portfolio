# Guide de Déploiement Vercel - Portfolio Hugo

## 📋 Pré-requis

- Compte GitHub connecté à Vercel
- Dépôt GitHub du portfolio configuré
- Accès administrateur au projet

## 🚀 Procédure de Déploiement

### 1. Préparation des Modifications

```bash
# Vérifier l'état du dépôt
git status

# Ajouter les nouveaux fichiers
git add .

# Commit des modifications
git commit -m "feat: ajout article réparation GRUB et image dual boot"

# Pousser vers GitHub
git push origin main
```

### 2. Déploiement Automatique Vercel

**Vercel détecte automatiquement les changements** sur la branche `main` et déploie automatiquement.

### 3. Vérification du Déploiement

1. **Accéder au dashboard Vercel** : https://vercel.com/dashboard
2. **Sélectionner le projet** "mon-portfolio"
3. **Vérifier le statut** de la dernière build
4. **Visiter le site** : https://mon-portfolio.vercel.app

## 🛠️ Configuration Vercel

### Build Settings (Configurées)

- **Framework Preset** : Hugo
- **Build Command** : `hugo --gc --minify`
- **Output Directory** : `public`
- **Install Command** : (vide - Hugo n'a pas de dépendances npm)

### Variables d'Environnement

Aucune variable d'environnement nécessaire pour ce projet Hugo statique.

## 🔍 Vérification Post-Déploiement

### 1. Test de l'Article

```bash
# Vérifier que l'article est accessible
curl -s https://mon-portfolio.vercel.app/blog/reparation-grub-apres-mise-a-jour-windows/ | grep -o '<title>.*</title>'
```

### 2. Test Responsive

**Sur Mobile :**
- Ouvrir l'URL sur smartphone
- Vérifier que l'image s'adapte (`max-w-full`)
- Tester la navigation

**Sur Desktop :**
- Vérifier que l'image est limitée (`md:max-w-lg`)
- Tester les breakpoints

### 3. Test des Images

```bash
# Vérifier que l'image est servie
curl -I https://mon-portfolio.vercel.app/images/photo_dual_boot.png
```

## 🐛 Résolution de Problèmes

### Build Échoue

```bash
# Vérifier localement avant déploiement
cd mon-portfolio
hugo --gc --minify

# Vérifier les erreurs
hugo server
```

### Image Non Affichée

1. Vérifier le chemin dans l'article
2. Confirmer que l'image est dans `static/images/`
3. Vérifier les permissions du fichier

### Problème Responsive

1. Vérifier les classes Tailwind CSS
2. Tester avec différentes tailles d'écran
3. Utiliser les outils de développement navigateur

## 📊 Monitoring

### Métriques à Surveiller

- **Temps de build** : < 30 secondes
- **Taille du bundle** : < 5MB
- **Performance Lighthouse** : > 90/100
- **SEO Score** : > 90/100

### Logs Vercel

- Accéder aux logs via le dashboard Vercel
- Vérifier les erreurs de build
- Surveiller les performances

## 🔄 Workflow Recommandé

1. **Développement local** avec `hugo server`
2. **Test responsive** sur différents appareils
3. **Commit et push** vers GitHub
4. **Vérification automatique** Vercel
5. **Test de production** sur l'URL déployée

## 📞 Support

- **Documentation Vercel** : https://vercel.com/docs
- **Documentation Hugo** : https://gohugo.io/documentation/
- **Problèmes GitHub** : Ouvrir une issue dans le dépôt

---

**Dernière mise à jour** : 17 octobre 2025
**Statut** : ✅ Prêt pour le déploiement
