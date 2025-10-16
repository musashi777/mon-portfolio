---
title: "Projet : Installation et Configuration d'un Serveur GLPI"
date: 2025-10-14T15:00:00+02:00
draft: false
description: "Déploiement complet d'un serveur GLPI sur Debian/Ubuntu pour la gestion de parc et le suivi d'incidents."
image: "/images/glpi_project.png"
technologies: ["GLPI", "Linux (Debian)", "Apache", "MariaDB (MySQL)", "PHP"]
summary: "Découvrez comment j'ai installé et configuré un serveur GLPI complet, de l'analyse des besoins à la sécurisation post-installation."
---

## 1. Contexte et Objectifs Business

**Problématique :** Une entreprise sans solution ITSM centralisée fait face à une gestion des incidents inefficace, un manque de traçabilité et une perte de temps pour les équipes techniques et les utilisateurs.

**Solution Apportée :** Le déploiement d'un serveur GLPI (Gestionnaire Libre de Parc Informatique) permet de centraliser la gestion des tickets, d'automatiser l'inventaire du parc et de fournir des rapports précis sur l'activité du support.

**Impact Mesurable :**
- **Réduction du temps de traitement des tickets** d'environ 30% grâce à la centralisation.
- **Amélioration de la satisfaction utilisateur** avec un suivi transparent des demandes.
- **Optimisation de la gestion des actifs** (software et hardware).

---

## 2. Guide d'Installation Technique Détaillé

Ce guide documente la procédure complète pour installer et configurer un serveur GLPI sur une base Debian/Ubuntu.

### Prérequis
- Un serveur Debian (11/12) ou Ubuntu (22.04/24.04).
- Accès root ou un utilisateur avec privilèges `sudo`.
- Connaissances de base en ligne de commande Linux.

### Étape 1 : Installation de la Stack LAMP

```bash
# Mise à jour des paquets
sudo apt update && sudo apt upgrade -y

# Installation d'Apache et MariaDB
sudo apt install -y apache2 mariadb-server

# Installation de PHP et des extensions requises
sudo apt install -y php php-cli php-mysql php-xml php-gd php-curl php-mbstring php-intl php-apcu php-zip php-bz2 php-ldap php-cas php-xmlrpc

# Sécurisation de MariaDB
sudo mysql_secure_installation
```

### Étape 2 : Création de la Base de Données

```sql
-- Connexion à MariaDB
sudo mysql -u root -p

-- Création de la base et de l'utilisateur
CREATE DATABASE glpidb CHARACTER SET UTF8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'glpi_user'@'localhost' IDENTIFIED BY 'votre_mot_de_passe_securise';
GRANT ALL PRIVILEGES ON glpidb.* TO 'glpi_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### Étape 3 : Déploiement de GLPI

```bash
# Téléchargement de la dernière version
cd /tmp
wget https://github.com/glpi-project/glpi/releases/download/10.0.15/glpi-10.0.15.tgz

# Extraction et déplacement des fichiers
tar -xzf glpi-10.0.15.tgz
sudo mv glpi /var/www/html/glpi
```

### Étape 4 : Configuration des Permissions et d'Apache

```bash
# Attribution des permissions à l'utilisateur www-data
sudo chown -R www-data:www-data /var/www/html/glpi
sudo chmod -R 755 /var/www/html/glpi

# (Optionnel) Création d'un Virtual Host Apache
sudo nano /etc/apache2/sites-available/glpi.conf
```

Contenu du fichier `glpi.conf`:
```apache
<VirtualHost *:80>
    ServerName glpi.votredomaine.com
    DocumentRoot /var/www/html/glpi
    <Directory /var/www/html/glpi>
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
```

```bash
# Activation du site et redémarrage d'Apache
sudo a2ensite glpi.conf
sudo a2enmod rewrite
sudo systemctl restart apache2
```

### Étape 5 : Finalisation via l'Interface Web
1.  Accédez à `http://glpi.votredomaine.com`.
2.  Suivez les instructions de l'installeur web.
3.  Connectez-vous avec `glpi` / `glpi` et changez les mots de passe immédiatement.
4.  **Important :** Supprimez le fichier d'installation.
    ```bash
    sudo rm /var/www/html/glpi/install/install.php
    ```

---

## 3. Compétences Démontrées

Ce projet illustre ma maîtrise des compétences suivantes :

- **Administration Système Linux :** Gestion des services, des paquets et des permissions.
- **Serveurs Web :** Configuration d'Apache, y compris les Virtual Hosts.
- **Bases de Données :** Administration de MariaDB (MySQL), gestion des utilisateurs et des privilèges.
- **Déploiement d'Applications :** Suivi de procédures complexes et résolution de dépendances.
- **Sécurité :** Sécurisation de base de la stack LAMP et des permissions applicatives.
- **Documentation Technique :** Création de guides clairs et reproductibles.