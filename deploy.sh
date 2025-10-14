#!/bin/bash

# Script de déploiement rapide pour portfolio Hugo
echo "🚀 Démarrage du déploiement..."

# Build du site
echo "📦 Building Hugo site..."
hugo --gc --minify

# Vérification du build
if [ $? -eq 0 ]; then
    echo "✅ Build réussi"
else
    echo "❌ Erreur lors du build"
    exit 1
fi

# Ajout des fichiers
echo "📝 Ajout des modifications..."
git add .

# Commit
echo "💾 Création du commit..."
git commit -m "Update portfolio - $(date +'%Y-%m-%d %H:%M')"

# Push vers GitHub
echo "⬆️  Push vers GitHub..."
git push origin main

if [ $? -eq 0 ]; then
    echo "🎉 Déploiement terminé !"
    echo "📱 Vercel/Netlify va automatiquement déployer la nouvelle version"
    echo "⏰ Attendez 1-2 minutes pour voir les changements en ligne"
else
    echo "❌ Erreur lors du push Git"
    exit 1
fi
