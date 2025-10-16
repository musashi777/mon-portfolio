---
title: "Projet : VPN Site-à-Site avec IPsec et Pfsense"
date: 2025-10-14T13:15:00+02:00
draft: false
description: "Configuration d'un tunnel VPN IPsec sécurisé entre deux sites distants pour protéger les communications."
image: "/images/vpn_project.png"
technologies: ["IPsec", "Pfsense", "Routage Statique", "AES-256"]
summary: "Découvrez comment j'ai conçu et déployé un tunnel VPN IPsec site-à-site pour connecter deux réseaux de manière sécurisée avec Pfsense."
---

## 1. Contexte et Objectifs Business

**Problématique :** Une entreprise avec plusieurs sites géographiques doit échanger des données sensibles sur Internet, ce qui expose à des risques d'interception et de corruption.

**Solution Apportée :** La mise en place d'un tunnel VPN (Virtual Private Network) IPsec site-à-site crée un canal de communication chiffré et authentifié entre les deux réseaux, les rendant logiquement connectés comme un seul réseau privé.

**Impact Mesurable :**
- **Sécurité des Données :** Confidentialité et intégrité des données garanties grâce au chiffrement AES-256.
- **Continuité d'Activité :** Les services et applications internes sont accessibles de manière transparente et sécurisée depuis les deux sites.
- **Réduction des Coûts :** Utilisation d'une connexion Internet publique au lieu de liaisons privées coûteuses.

---

## 2. Guide de Configuration Technique

Ce guide détaille les étapes pour configurer un tunnel VPN IPsec entre deux pare-feux Pfsense.

**Architecture Cible :**
- **Site A :** Réseau `192.168.1.0/24`
- **Site B :** Réseau `192.168.2.0/24`

### Étape 1 : Configuration de la Phase 1 (IKEv2)
La Phase 1 établit le canal de communication sécurisé entre les deux pare-feux.

- **Protocole :** IKEv2
- **Algorithme de Chiffrement :** AES-256-GCM
- **Hachage :** SHA-256
- **Groupe Diffie-Hellman :** 14 (2048-bit)

*Configuration via `VPN > IPsec > Add P1` sur Pfsense.*

### Étape 2 : Configuration de la Phase 2 (ESP)
La Phase 2 définit quels réseaux peuvent communiquer à travers le tunnel.

- **Mode :** Tunnel IPv4
- **Réseaux :** `192.168.1.0/24` (Local) <-> `192.168.2.0/24` (Remote)
- **Algorithme de Chiffrement :** AES-256-GCM
- **PFS (Perfect Forward Secrecy) :** Activé (Groupe 14)

*Configuration via les détails de la Phase 1 sur Pfsense.*

### Étape 3 : Règles de Pare-feu
Il faut autoriser le trafic à passer à travers le tunnel.

- **Interface IPsec :** Créer une règle autorisant le trafic (protocole `any`) depuis le réseau local vers le réseau distant.
- **Interface LAN :** Assurez-vous que le trafic sortant vers le réseau distant est autorisé.

*Configuration via `Firewall > Rules > IPsec`.*

### Étape 4 : Vérification et Dépannage
- **Statut du Tunnel :** Vérifiez que le tunnel est bien établi dans `Status > IPsec`.
- **Test de Ping :** Lancez un `ping` d'une machine du Site A vers une machine du Site B.
- **Logs :** Consultez les logs (`Status > System Logs > IPsec`) pour diagnostiquer les problèmes.

---

## 3. Compétences Démontrées

Ce projet met en avant les compétences suivantes :

- **Sécurité Réseau :** Maîtrise des concepts VPN et du protocole IPsec (IKEv2, ESP).
- **Administration de Pare-feu :** Configuration avancée de Pfsense, incluant le routage et les règles de filtrage.
- **Routage :** Compréhension et mise en place de routes pour connecter des réseaux distincts.
- **Diagnostic Réseau :** Utilisation d'outils comme `ping`, `traceroute` et l'analyse de logs pour valider et dépanner une configuration.
- **Chiffrement :** Application des meilleures pratiques en matière de chiffrement (AES-256) et d'échange de clés (DH Group 14).