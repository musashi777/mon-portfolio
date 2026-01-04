---
title: "Guide Détaillé - Installation Serveur GLPI"
date: 2025-10-14T15:00:00+02:00
draft: false
description: "Guide technique complet avec toutes les commandes pour installer et configurer GLPI sur Debian/Ubuntu"
image: "/images/technicien-aide-collegue.png"
technologies: ["GLPI", "Linux (Debian)", "Apache", "MariaDB (MySQL)", "PHP"]
---

<div class="bg-gradient-to-r from-blue-50 to-indigo-100 dark:from-blue-900/20 dark:to-indigo-900/20 p-6 rounded-xl border border-blue-200 dark:border-blue-700 mb-8">
  <h2 class="!text-2xl !mt-0 mb-4 text-blue-700 dark:text-blue-300">📋 Aperçu du Projet</h2>
  <div class="grid grid-cols-1 md:grid-cols-4 gap-4 text-sm">
    <div>
      <strong>Technologies :</strong>
      <ul class="!my-1">
        <li>GLPI 10.0.15</li>
        <li>Debian 12</li>
        <li>Apache 2.4</li>
        <li>MariaDB 10.11</li>
        <li>PHP 8.2</li>
      </ul>
    </div>
    <div>
      <strong>Durée :</strong>
      <p class="!my-1">2-3 heures</p>
      <strong>Niveau :</strong>
      <p class="!my-1">Intermédiaire</p>
    </div>
    <div>
      <strong>Résultats :</strong>
      <ul class="!my-1">
        <li>✅ Serveur fonctionnel</li>
        <li>✅ Interface web</li>
        <li>✅ Base sécurisée</li>
      </ul>
    </div>
    <div>
      <strong>Impact Business :</strong>
      <ul class="!my-1">
        <li>📈 Gestion centralisée de 50+ utilisateurs</li>
        <li>⏱️ Réduction de 25% du temps de résolution</li>
        <li>💰 Solution open-source (économie de licence)</li>
        <li>🔧 Automatisation des processus IT</li>
      </ul>
    </div>
  </div>
</div>

## 🎯 Objectif du Projet

L'objectif de ce projet est de documenter la procédure complète pour installer et configurer un serveur GLPI, un outil open-source de gestion des services informatiques (ITSM) et de gestion des actifs (ITAM). Cette solution permet de gérer efficacement un parc informatique, le suivi des tickets d'incidents et l'inventaire matériel et logiciel.

## ✅ Prérequis

Avant de commencer, assurez-vous de disposer des éléments suivants :
- Un serveur avec une installation fraîche de Debian (11 ou 12) ou Ubuntu (22.04 ou 24.04)
- Un accès root ou un utilisateur avec des privilèges sudo
- Une connaissance de base de la ligne de commande Linux
- Un client SSH (comme PuTTY ou le terminal de votre machine) pour vous connecter à votre serveur

## 🚀 Étapes Clés de la Réalisation

Nous allons suivre 5 étapes principales pour mettre en place notre serveur GLPI.

### Étape 1 : Installation de la stack LAMP

La première étape consiste à installer l'environnement web nécessaire : Apache2 (le serveur web), MariaDB (le système de gestion de base de données) et PHP (le langage de programmation de GLPI).

<div class="bg-gray-50 dark:bg-gray-800 p-4 rounded-lg my-4">
  <h4 class="!text-lg !mt-0 mb-2">Commandes à exécuter :</h4>

  **Mettez à jour la liste des paquets :**
  ```bash
  sudo apt update && sudo apt upgrade -y
  ```

  **Installez Apache2 et MariaDB :**
  ```bash
  sudo apt install -y apache2 mariadb-server
  ```

  **Installez PHP et les extensions requises par GLPI :**
  ```bash
  sudo apt install -y php php-cli php-mysql php-xml php-gd php-curl php-mbstring php-intl php-apcu php-zip php-bz2 php-ldap php-cas php-xmlrpc
  ```

  **Sécurisez votre installation MariaDB :**
  ```bash
  sudo mysql_secure_installation
  ```
</div>

### Étape 2 : Création de la Base de Données

GLPI a besoin de sa propre base de données et d'un utilisateur dédié pour des raisons de sécurité et d'organisation.

<div class="bg-gray-50 dark:bg-gray-800 p-4 rounded-lg my-4">
  <h4 class="!text-lg !mt-0 mb-2">Configuration de la base de données :</h4>

  **Connectez-vous à MariaDB :**
  ```bash
  sudo mysql -u root -p
  ```

  **Dans l'invite MySQL, exécutez les commandes suivantes :**
  ```sql
  CREATE DATABASE glpidb CHARACTER SET UTF8mb4 COLLATE utf8mb4_unicode_ci;
  CREATE USER 'glpi_user'@'localhost' IDENTIFIED BY 'votre_mot_de_passe_securise';
  GRANT ALL PRIVILEGES ON glpidb.* TO 'glpi_user'@'localhost';
  FLUSH PRIVILEGES;
  EXIT;
  ```
</div>

### Étape 3 : Téléchargement et Déploiement de GLPI

Nous allons maintenant télécharger la dernière version de GLPI et la placer dans le répertoire du serveur web.

<div class="bg-gray-50 dark:bg-gray-800 p-4 rounded-lg my-4">
  <h4 class="!text-lg !mt-0 mb-2">Déploiement de GLPI :</h4>

  **Téléchargez GLPI :**
  ```bash
  cd /tmp
  wget https://github.com/glpi-project/glpi/releases/download/10.0.15/glpi-10.0.15.tgz
  ```

  **Extrayez l'archive :**
  ```bash
  tar -xzf glpi-10.0.15.tgz
  ```

  **Déplacez les fichiers vers le répertoire web :**
  ```bash
  sudo mv glpi /var/www/html/glpi
  ```
</div>

### Étape 4 : Configuration des Permissions

Il est crucial que le serveur web (qui s'exécute avec l'utilisateur www-data) ait les permissions d'écrire dans certains dossiers de GLPI.

<div class="bg-gray-50 dark:bg-gray-800 p-4 rounded-lg my-4">
  <h4 class="!text-lg !mt-0 mb-2">Configuration des permissions :</h4>

  **Changez le propriétaire du répertoire GLPI :**
  ```bash
  sudo chown -R www-data:www-data /var/www/html/glpi
  ```

  **Ajustez les permissions pour plus de sécurité :**
  ```bash
  sudo chmod -R 755 /var/www/html/glpi
  ```

  **Configuration Apache (optionnel mais recommandé) :**
  ```bash
  sudo nano /etc/apache2/sites-available/glpi.conf
  ```

  **Contenu du fichier de configuration :**
  ```apache
  <VirtualHost *:80>
      ServerAdmin admin@example.com
      DocumentRoot /var/www/html/glpi
      ServerName glpi.votredomaine.com

      <Directory /var/www/html/glpi>
          Options FollowSymLinks
          AllowOverride All
          Require all granted
      </Directory>

      ErrorLog ${APACHE_LOG_DIR}/glpi_error.log
      CustomLog ${APACHE_LOG_DIR}/glpi_access.log combined
  </VirtualHost>
  ```

  **Activez le site et les modules :**
  ```bash
  sudo a2ensite glpi.conf
  sudo a2enmod rewrite
  sudo systemctl restart apache2
  ```
</div>

### Étape 5 : Installation via l'Interface Web

La dernière étape se passe dans votre navigateur.

<div class="bg-green-50 dark:bg-green-900/20 p-4 rounded-lg my-4">
  <h4 class="!text-lg !mt-0 mb-2">Installation via l'interface web :</h4>

  1. **Accédez à l'URL** de votre serveur GLPI
  2. **Sélectionnez la langue** et acceptez la licence
  3. **Vérifiez les prérequis** - tous doivent être en vert
  4. **Configurez la base de données** avec les informations créées précédemment
  5. **Sélectionnez la base de données** glpidb
  6. **Finalisez l'installation** et notez les identifiants par défaut
</div>

## 🏁 Résultat Obtenu et Étapes Suivantes

À l'issue de ce projet, un serveur GLPI est pleinement fonctionnel et accessible via le réseau. La plateforme est prête à être configurée pour l'inventaire automatique du parc, la gestion des tickets et le suivi des actifs.

### ⚠️ Actions post-installation (TRÈS IMPORTANT)

<div class="bg-red-50 dark:bg-red-900/20 p-4 rounded-lg my-4 border border-red-200 dark:border-red-700">
  <h4 class="!text-lg !mt-0 mb-2 text-red-700 dark:text-red-300">Sécurisation du serveur :</h4>

  **Supprimez le fichier d'installation :**
  ```bash
  sudo rm /var/www/html/glpi/install/install.php
  ```

  **Changez les mots de passe par défaut :**
  - Connectez-vous avec l'utilisateur `glpi` et le mot de passe `glpi`
  - Changez immédiatement tous les mots de passe par défaut dans Administration > Utilisateurs
</div>

## 📊 Compétences Développées

Ce projet m'a permis de renforcer mes compétences en :

- **Administration Linux** : Gestion des paquets, permissions, services
- **Configuration réseau** : Virtual Hosts Apache, sécurité
- **Bases de données** : MariaDB/MySQL, création d'utilisateurs, privilèges
- **Sécurité** : Hardening des applications web, bonnes pratiques
- **Documentation** : Création de guides techniques détaillés

---

<div class="text-center mt-8 p-6 bg-gradient-to-r from-primary-50 to-blue-50 dark:from-primary-900/20 dark:to-blue-900/20 rounded-xl">
  <h3 class="!text-xl !mt-0 mb-4">🚀 Prêt à déployer votre propre instance GLPI ?</h3>
  <p class="!my-2">Ce guide vous fournit toutes les étapes nécessaires pour une installation réussie.</p>
  <a href="/projets/installation-serveur-glpi/" class="px-6 py-3 rounded-lg bg-primary-500 text-white font-semibold hover:bg-primary-600 transition-colors inline-block mt-4">
    ← Retour à la présentation du projet
  </a>
</div>
