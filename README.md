# 🧮 Projet RabbitMQ – Système de Calcul Distribué

## 📌 Objectif
Ce projet implémente un **système de calcul distribué** utilisant **RabbitMQ**. Il simule un environnement où des **clients envoient des opérations mathématiques** (add, sub, mul, div) à des **workers spécialisés** via un **message broker** RabbitMQ.

---

## 🧱 Architecture du Projet

```plaintext
+------------+        +-------------+        +-------------+
|  Client TX | -----> | RabbitMQ 🐇 | -----> |   Workers   |
| (Génère    |        |             |        |  (add/sub/…)|
| opérations)|        |             |        |             |
+------------+        +-------------+        +-------------+
                                 |
                                 v
                         +---------------+
                         | Client RX     |
                         | (Affiche les  |
                         | résultats)    |
                         +---------------+
