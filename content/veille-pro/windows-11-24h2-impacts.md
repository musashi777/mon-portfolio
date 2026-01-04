---
title: "Windows 11 24H2 : Les impacts pour le support IT"
date: 2025-01-03
description: "Analyse des changements majeurs de la version 24H2 : fin de support WordPad, exigences POPCNT, et nouvelles GPO de sécurité."
tags: ["Windows 11", "SysAdmin", "Sécurité", "Veille"]
---

## Introduction

La mise à jour Windows 11 24H2 n'est pas qu'une simple mise à jour de fonctionnalités ("Feature Update"), c'est un véritable changement de plateforme (OS Swap) basé sur la branche "Germanium". Pour les équipes de support et les administrateurs système, cela implique plusieurs points de vigilance.

## 1. Exigences Matérielles Renforcées (POPCNT)

Contrairement aux versions précédentes où le contournement des prérequis TPM 2.0 était relativement simple via des clés de registre (type Rufux/Ventoy), la version 24H2 impose strictement l'instruction CPU **POPCNT**.
*   **Conséquence :** Les processeurs très anciens (Core 2 Duo, premiers Athlon 64) qui pouvaient techniquement encore booter Windows 11 via des hacks ne pourront plus du tout démarrer le noyau.

## 2. Sécurité : SMB et NTLM

Microsoft durcit le ton sur les protocoles hérités :
*   **SMB Signing** est désormais activé par défaut sur toutes les éditions (Pro, Enterprise, et même Home). Cela peut ralentir légèrement les transferts de petits fichiers sur des NAS anciens mais sécurise grandement les échanges.
*   **NTLM** est en voie de dépréciation active au profit de Kerberos.

## 3. Nettoyage des Apps Héritées

C'est officiel :
*   **WordPad** est supprimé.
*   **Cortana** est désactivé.
*   **Tips** est supprimé.

Pour le support, cela signifie s'assurer que les utilisateurs ont bien une suite bureautique installée ou utilisent le Bloc-notes (qui a été modernisé avec des onglets) pour les fichiers texte basiques.

## Conclusion

Cette version stabilise Windows 11 comme un OS mature pour l'entreprise, mais nécessite une validation du parc matériel plus stricte qu'auparavant.
