# 📋 Instructions pour Vercel - Configuration du Pré-réglage

## 🎯 Sur la page Vercel "Import Git Repository"

### **Étape 1 : Connexion**
- Cliquez sur "Continue with GitHub"
- Autorisez l'accès à votre compte

### **Étape 2 : Import du dépôt**
- Sélectionnez votre dépôt : `musashi777/mon-portfolio`

### **Étape 3 : Configuration du Framework Preset**

**Dans la section "FRAMEWORK PRESET", sélectionnez :**

```
Hugo
```

**OU si Hugo n'apparaît pas directement :**

```
Other
```

### **Étape 4 : Vérification automatique**

Vercel devrait **automatiquement détecter** la configuration grâce à votre fichier `vercel.json` :

```json
{
  "buildCommand": "hugo --gc --minify",
  "outputDirectory": "public",
  "installCommand": "npm install -g hugo-extended"
}
```

### **Étape 5 : Champs à vérifier**

Si vous devez remplir manuellement :

| Champ | Valeur à mettre |
|-------|-----------------|
| **Framework Preset** | `Hugo` |
| **Build Command** | `hugo --gc --minify` |
| **Output Directory** | `public` |
| **Install Command** | `npm install -g hugo-extended` |

### **Étape 6 : Déploiement**

- **Ne changez pas** le nom du projet (il sera `mon-portfolio`)
- **Cliquez sur "Deploy"**

---

## 🔍 Si Hugo n'est pas dans la liste

Si "Hugo" n'apparaît pas dans les options :

1. **Sélectionnez "Other"** dans Framework Preset
2. **Les champs seront automatiquement remplis** grâce à `vercel.json`
3. **Si pas automatique**, remplissez manuellement :
   - Build Command: `hugo --gc --minify`
   - Output Directory: `public`

---

## ✅ Ce qui devrait se passer

**Après le déploiement :**

- ✅ Build automatique détecté
- ✅ Configuration Hugo appliquée
- ✅ Site généré dans le dossier `public`
- ✅ URL créée : `mon-portfolio-musashi777.vercel.app`

**Temps estimé :** 1-2 minutes

---

## 🚨 En cas de problème

### **Si le build échoue :**

1. **Vérifiez les logs** dans Vercel Dashboard
2. **Assurez-vous que** :
   - Framework Preset = `Hugo` ou `Other`
   - Build Command = `hugo --gc --minify`
   - Output Directory = `public`

### **Si Hugo n'est pas reconnu :**

Utilisez cette configuration alternative :

```
Framework Preset: Other
Build Command: hugo --gc --minify
Output Directory: public
Install Command: npm install -g hugo-extended
```

---

## 🎉 Résultat attendu

Votre portfolio sera accessible sur :
**https://mon-portfolio-musashi777.vercel.app**

**Le site sera :**
- Rapide (CDN global)
- Sécurisé (HTTPS automatique)
- Automatiquement mis à jour à chaque push Git
- Optimisé pour les recruteurs techniques

**Vous pourrez ensuite :**
- Personnaliser le domaine
- Ajouter des analytics
- Configurer des redirections
