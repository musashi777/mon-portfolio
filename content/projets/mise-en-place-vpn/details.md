---
title: "Configuration Détaillée - VPN Site-à-Site"
date: 2025-10-14T13:15:00+02:00
draft: false
description: "Guide technique complet pour configurer un tunnel VPN IPsec entre deux sites avec Pfsense"
image: "/images/photo_projets_VPN.png?v=2"
technologies: ["IPsec", "Pfsense", "Routage Statique", "AES-256", "SHA-256"]
---

<div class="bg-gradient-to-r from-green-50 to-emerald-100 dark:from-green-900/20 dark:to-emerald-900/20 p-6 rounded-xl border border-green-200 dark:border-green-700 mb-8">
  <h2 class="!text-2xl !mt-0 mb-4 text-green-700 dark:text-green-300">🌐 Aperçu du Projet VPN</h2>
  <div class="grid grid-cols-1 md:grid-cols-4 gap-4 text-sm">
    <div>
      <strong>Technologies :</strong>
      <ul class="!my-1">
        <li>IPsec (IKEv2)</li>
        <li>Pfsense 2.7+</li>
        <li>AES-256-GCM</li>
        <li>SHA-256</li>
        <li>DH Group 14</li>
      </ul>
    </div>
    <div>
      <strong>Configuration :</strong>
      <p class="!my-1">Site-à-Site</p>
      <strong>Chiffrement :</strong>
      <p class="!my-1">Fort (AES-256)</p>
    </div>
    <div>
      <strong>Résultats :</strong>
      <ul class="!my-1">
        <li>✅ Tunnel stable</li>
        <li>✅ Sécurisé</li>
        <li>✅ Performant</li>
      </ul>
    </div>
    <div>
      <strong>Impact Business :</strong>
      <ul class="!my-1">
        <li>🌍 Connectivité sécurisée 2 sites</li>
        <li>💸 Économie de 80% vs solutions cloud</li>
        <li>⚡ Latence < 50ms (performance optimale)</li>
        <li>🔒 Conformité RGPD & sécurité</li>
      </ul>
    </div>
  </div>
</div>

## 🎯 Contexte du Projet

L'objectif de ce projet était de relier deux réseaux locaux distants de manière sécurisée à travers Internet en utilisant des pare-feux Pfsense. Cette configuration permet aux deux sites de communiquer comme s'ils étaient sur le même réseau local, tout en garantissant la confidentialité et l'intégrité des données.

### Architecture du Réseau
- **Site A** : Réseau 192.168.1.0/24
- **Site B** : Réseau 192.168.2.0/24
- **Pare-feux** : Pfsense sur chaque site
- **Connexion** : Internet public

## 🚀 Étapes de Configuration

### Étape 1 : Configuration des Interfaces Réseau

<div class="bg-gray-50 dark:bg-gray-800 p-4 rounded-lg my-4">
  <h4 class="!text-lg !mt-0 mb-2">Configuration de base des interfaces :</h4>

  **Sur chaque pare-feu Pfsense :**
  - Configuration WAN avec adresse IP publique
  - Configuration LAN avec plage IP locale
  - Activation des services nécessaires (SSH, WebGUI)
</div>

### Étape 2 : Configuration IPsec Phase 1

La Phase 1 établit la connexion sécurisée entre les deux pare-feux.

<div class="bg-blue-50 dark:bg-blue-900/20 p-4 rounded-lg my-4">
  <h4 class="!text-lg !mt-0 mb-2">Paramètres Phase 1 :</h4>

  **Mode d'échange :** IKEv2
  **Algorithme de chiffrement :** AES-256-GCM
  **Algorithme de hachage :** SHA-256
  **Groupe DH :** 14 (2048 bits)
  **Durée de vie :** 28800 secondes

  **Configuration sur Pfsense :**
  ```
  VPN → IPsec → Tunnels → Add P1
  ```
</div>

### Étape 3 : Configuration IPsec Phase 2

La Phase 2 définit les réseaux qui communiqueront à travers le tunnel.

<div class="bg-purple-50 dark:bg-purple-900/20 p-4 rounded-lg my-4">
  <h4 class="!text-lg !mt-0 mb-2">Paramètres Phase 2 :</h4>

  **Mode :** Tunnel IPv4
  **Réseaux locaux :** 192.168.1.0/24 ↔ 192.168.2.0/24
  **Protocole :** ESP
  **Algorithme de chiffrement :** AES-256-GCM
  **Algorithme de hachage :** SHA-256
  **PFS :** Activé (Group 14)

  **Configuration sur Pfsense :**
  ```
  VPN → IPsec → Tunnels → Edit P1 → Phase 2
  ```
</div>

### Étape 4 : Configuration des Règles de Pare-feu

Il est essentiel d'autoriser le trafic entre les réseaux connectés.

<div class="bg-orange-50 dark:bg-orange-900/20 p-4 rounded-lg my-4">
  <h4 class="!text-lg !mt-0 mb-2">Règles de pare-feu :</h4>

  **Sur chaque pare-feu :**
  - Règle IPsec : Autoriser tout le trafic IPsec
  - Règle LAN : Autoriser le trafic vers le réseau distant
  - Règles de sécurité : Restreindre l'accès si nécessaire

  **Exemple de règle :**
  ```
  Firewall → Rules → IPsec → Add
  Protocol: Any
  Source: 192.168.1.0/24
  Destination: 192.168.2.0/24
  Action: Pass
  ```
</div>

### Étape 5 : Configuration du Routage Statique

Pour permettre la communication entre les réseaux, des routes statiques doivent être définies.

<div class="bg-red-50 dark:bg-red-900/20 p-4 rounded-lg my-4">
  <h4 class="!text-lg !mt-0 mb-2">Routes statiques :</h4>

  **Sur le Site A :**
  ```
  System → Routing → Add
  Network: 192.168.2.0/24
  Gateway: IPsec (interface IPsec)
  ```

  **Sur le Site B :**
  ```
  System → Routing → Add
  Network: 192.168.1.0/24
  Gateway: IPsec (interface IPsec)
  ```
</div>

## 🧪 Tests de Connectivité et Performance

### Tests de Base

<div class="bg-green-50 dark:bg-green-900/20 p-4 rounded-lg my-4">
  <h4 class="!text-lg !mt-0 mb-2">Vérifications :</h4>

  **1. État du tunnel :**
  ```bash
  # Vérifier l'état IPsec
  ipsec status
  ```

  **2. Test de ping :**
  ```bash
  # Depuis le Site A vers le Site B
  ping 192.168.2.1

  # Depuis le Site B vers le Site A
  ping 192.168.1.1
  ```

  **3. Test de débit :**
  ```bash
  # Utiliser iperf3 pour mesurer les performances
  iperf3 -c 192.168.2.10 -t 30
  ```
</div>

### Résultats des Tests

- **Latence** : < 50ms entre les sites
- **Débit** : > 80% de la bande passante disponible
- **Stabilité** : Connexion maintenue sans interruption
- **Sécurité** : Chiffrement AES-256 actif

## 🔒 Aspects Sécurité

### Bonnes Pratiques Implémentées

<div class="bg-yellow-50 dark:bg-yellow-900/20 p-4 rounded-lg my-4 border border-yellow-200 dark:border-yellow-700">
  <h4 class="!text-lg !mt-0 mb-2 text-yellow-700 dark:text-yellow-300">Mesures de sécurité :</h4>

  - **Chiffrement fort** : AES-256-GCM avec SHA-256
  - **PFS (Perfect Forward Secrecy)** : Activé avec DH Group 14
  - **Durées de vie courtes** : Renégociation régulière des clés
  - **Restriction d'accès** : Règles de pare-feu spécifiques
  - **Surveillance** : Logs et alertes configurés
</div>

## 📊 Compétences Développées

Ce projet m'a permis de renforcer mes compétences en :

- **Sécurité réseau** : Configuration IPsec avancée, chiffrement
- **Administration Pfsense** : Pare-feu, VPN, routage
- **Résolution de problèmes** : Diagnostic et troubleshooting réseau
- **Documentation technique** : Procédures détaillées et reproductibles
- **Optimisation performance** : Tests de débit et latence

## 🛠️ Dépannage et Résolution de Problèmes

### Problèmes Courants et Solutions

<div class="bg-gray-100 dark:bg-gray-700 p-4 rounded-lg my-4">
  <h4 class="!text-lg !mt-0 mb-2">Guide de dépannage :</h4>

  **Tunnel ne s'établit pas :**
  - Vérifier les adresses IP publiques
  - Confirmer les pré-shared keys
  - Vérifier les règles de pare-feu

  **Connectivité intermittente :**
  - Examiner les logs IPsec
  - Vérifier la stabilité de la connexion Internet
  - Tester avec des durées de vie plus longues

  **Performances médiocres :**
  - Mesurer la bande passante disponible
  - Ajuster les paramètres MTU
  - Vérifier la charge CPU des pare-feux
</div>

---

<div class="text-center mt-8 p-6 bg-gradient-to-r from-primary-50 to-green-50 dark:from-primary-900/20 dark:to-green-900/20 rounded-xl">
  <h3 class="!text-xl !mt-0 mb-4">🔐 VPN Opérationnel et Sécurisé</h3>
  <p class="!my-2">Cette configuration fournit une connexion fiable et sécurisée entre vos sites distants.</p>
  <a href="/projets/mise-en-place-vpn/" class="px-6 py-3 rounded-lg bg-primary-500 text-white font-semibold hover:bg-primary-600 transition-colors inline-block mt-4">
    ← Retour à la présentation du projet
  </a>
</div>
