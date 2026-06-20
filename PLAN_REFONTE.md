# PLAN DE REFONTE — Programme DevOps projet-first

> Statut : **décision d'architecture**. L'ossature projet-first est créée ; les missions détaillées restent à écrire.
> Ce document garde la vision, les arbitrages et les prochains travaux.

---

## 1. Décisions actées

| Décision | Choix |
| --- | --- |
| Pédagogie | **Projet-first** : on démarre par construire, on lit la théorie quand on bute |
| Stack appli fil rouge | **Python + FastAPI + PostgreSQL** |
| App fil rouge | **Un backend de chatbot** (historique en base → puis branché à un LLM externe) |
| Théorie | **Intégrée** dans les missions (cours inline), avec ressources de révision conservées |
| CI/CD | **GitHub Actions** en principal + **portage GitLab CI** en bonus + doc d'équivalences (Jenkins) |
| Config des machines | **Ansible** (playbook de bootstrap VPS) en complément de Terraform |
| Déploiement classique | **VPS payant** (~5€/mois) → vrai déploiement public avec HTTPS |
| Cloud | **GCP** principal (Cloud Run + Terraform) + doc d'équivalences AWS/Azure |
| Sécurité | **Pas de mission dédiée** → bonnes pratiques au fil de l'eau (gitleaks, Trivy, Dependabot, incident simulé) |
| Kubernetes | **Optionnel** : core local (k3d/kind) + boss final cloud éphémère (multi-VM + k6) |
| LLM | **Externe** (pas d'auto-hébergement) → focus DevOps sur secrets/quotas/résilience/coût |
| **Pratique IA** | **AI-assisted workflow dans chaque mission** : accélérer sans déléguer aveuglément, vérifier/tester/prouver |
| Objectif | Décrocher un **stage / alternance DevOps junior** avec un GitHub crédible |

---

## 2. Principe pédagogique

Le projet est le point d'entrée de chaque chapitre. La théorie devient une ressource
« juste-à-temps » qu'on consulte quand un checkpoint nous bloque.

```txt
brief projet  →  je construis  →  je bute  →  encadré cours ciblé  →  je continue
```

---

## 3. Structure en niveaux (recommandation Codex)

Les 11 missions sont regroupées en 4 paliers, pour qu'on sache **à partir de quand on peut déjà candidater** et que la fin du parcours ne soit pas bloquée par la mission la plus dure.

| Palier | Missions | Statut | Ce que ça prouve |
| --- | --- | --- | --- |
| 🟢 **Employable Core** | 0 → 6 | **Obligatoire** | Après ça tu peux **déjà postuler** : app dockerisée, CI, en ligne en HTTPS, monitorée, avec DB sauvegardée |
| 🔵 **Cloud / IaC Plus** | 7 → 8 | Fortement conseillé | Profil **moderne** : cloud GCP réel + infra en code + CD |
| 🟣 **Wow Optionnel** | 9 | Optionnel (boss final) | Le **bonus qui impressionne** : Kubernetes + autoscaling + test de charge |
| 🏆 **Vitrine** | 10 | **Obligatoire** | Transforme « j'ai suivi une formation » en « j'ai opéré un système » |

> Règle : la **Vitrine (10) est obligatoire**, pas une récompense floue. La **Mission 9 ne doit jamais bloquer** la fin du parcours.

---

## 4. Nouvelle arborescence cible

```txt
.
├── README.md                # pitch + comment utiliser le parcours + le parcours en 1 image
├── PARCOURS.md              # parcours en missions + paliers + cadence
├── agent.md                 # guide de style, mis à jour pour le format projet-first
│
├── missions/
│   ├── 00_boot/
│   │   └── MISSION.md
│   ├── 01_signe-de-vie/
│   │   ├── MISSION.md       # brief + DoD + checkpoints + encadrés cours + bloc IA
│   │   └── starter/         # squelette de code/config à compléter (quand pertinent)
│   ├── 02_la-forge/
│   ├── 03_mise-en-boite/
│   ├── 04_le-gardien/
│   ├── 05_grande-ouverture/
│   ├── 06_tour-de-controle/
│   ├── 07_le-cerveau/
│   ├── 08_l-architecte/
│   ├── 09_sous-pression/    # optionnel
│   └── 10_vitrine/
│
├── flagship/               # le PROJET FIL ROUGE qui grossit mission après mission
│   ├── README.md           # chatbot : FastAPI + Postgres → Docker → CI → VPS → monitoring → LLM/GCP → K8s
│   ├── app/                # code FastAPI
│   ├── migrations/         # migrations Alembic
│   ├── ansible/            # playbook bootstrap-vps.yml
│   ├── k8s/                # manifests Kustomize (overlays dev/prod) + Helm (bonus)
│   ├── evidence/           # LES PREUVES (captures, schémas, postmortem, log IA) — voir §11
│   └── .github/
│       └── copilot-instructions.md  # instructions IA de revue/code/doc contextualisées (bonus)
│
└── ressources/
    ├── CHEATSHEET.md        # commandes utiles par mission
    ├── GLOSSAIRE.md         # vocabulaire recruteur
    ├── DEBUG_GUIDE.md       # "si ça casse, quoi regarder" (NOUVEAU)
    ├── CI_EQUIVALENTS.md    # GitHub Actions ↔ GitLab CI ↔ Jenkins (NOUVEAU)
    ├── CLOUD_EQUIVALENTS.md # GCP ↔ AWS ↔ Azure (NOUVEAU)
    ├── AI_DEVOPS_GUIDE.md   # bonnes pratiques IA : limites, sécurité, confidentialité, hallucinations (NOUVEAU)
    ├── PROMPTS.md           # prompts utiles par techno (NOUVEAU)
    ├── AI_USAGE_LOG.md      # exemples d'utilisation réelle de l'IA pendant les missions (NOUVEAU)
    └── PORTFOLIO_GITHUB.md  # profil GitHub + CV recruteur-ready (NOUVEAU)
```

**Sur la théorie** : les notions conceptuelles vivent en **encadrés `📖 Cours`** dans les
checkpoints. On garde aussi des ressources de révision, pour que l'apprenant retrouve vite les
commandes, mots clés et réflexes avant un entretien : `CHEATSHEET.md`, `GLOSSAIRE.md`, `DEBUG_GUIDE.md`.

---

## 5. Le modèle de Mission (template)

```md
# Mission X — "Nom"

## 🎯 Le brief
Ce que tu construis, en 3 lignes. À quoi ça ressemblera, fini, sur ton GitHub.

## 🧠 Ce que tu vas vraiment apprendre (sans le lire avant de commencer)
La carte des notions qui vont surgir pendant le projet. Pas un cours, juste la carte.

## ✅ Definition of Done
Cases à cocher qui PROUVENT que c'est réussi (+ la preuve à déposer dans evidence/).
- [ ] ...
- [ ] Capture/artefact déposé dans flagship/evidence/
- [ ] Historique de commits propre

## 🧩 Les checkpoints
Étapes concrètes et ordonnées. Chacune = une action vérifiable.

### Checkpoint 1 — ...
> Action : ...  | Vérifie : ...  | 🆘 Bloqué ? → 📖 Cours (encadré ci-dessous)
   📖 Cours : [théorie inline, ciblée, courte — déclenchée par le blocage, pas avant]

## 📦 Plan de commits
Quoi committer et quand, pour un historique Git racontable.

## 🚀 Pour aller plus loin (le bonus qui impressionne)
Options non bloquantes.

## 🤖 IA dans cette mission
Objectif : utiliser l'IA pour accélérer sans déléguer aveuglément.
**À demander à l'IA :**
- ...
**À vérifier soi-même (la vedette) :**
- ... (CI, tests, logs, métriques, scans, commandes de diagnostic)
**Artefact à conserver (→ AI_USAGE_LOG.md / evidence/) :**
- le prompt utile
- la réponse IA corrigée par moi
- la preuve que la solution fonctionne

## 🧾 Ce que tu sais maintenant
Récap des acquis + liens vers les ancres du CHEATSHEET / GLOSSAIRE (ressource de révision).

## 🗣️ Ta phrase d'entretien
La phrase exacte que tu pourras dire en entretien une fois la mission faite.
```

Principes : on construit avant de lire ; chaque mission produit une **preuve GitHub** ET un
**artefact dans `evidence/`** ; la Definition of Done est la checklist de commits ; squelette
`starter/` quand partir de zéro tuerait l'élan.

---

## 6. La liste des missions (par palier)

Le projet fil rouge (`flagship/`) est **un backend de chatbot**. Il naît en Mission 3 et grossit jusqu'à la fin. Les missions 0–2 produisent des repos satellites.

### 🟢 Employable Core (0 → 6, obligatoire)

| # | Nom | Tu construis (projet-first) | Ajouts issus des revues | Coût |
| --- | --- | --- | --- | --- |
| 0 | **Boot** | Env de dev + 1er repo `devops-journal` au README soigné, premier push | — | 0€ |
| 1 | **Signe de vie** | Serveur HTTP public qui survit à un reboot (systemd), sur le **VPS** | — | VPS ~5€/mo |
| 2 | **La Forge** | Scripts Bash/Python (backup, check site, alerte disque, extraction erreurs, JSON) + cron | — | 0€ |
| 3 | **Mise en boîte** | Backend chatbot FastAPI + PostgreSQL en Docker Compose, données persistées | **Migrations Alembic** (schéma versionné, pas de DB "à la main") | 0€ |
| 4 | **Le Gardien** | CI GitHub Actions : lint + tests + build + push GHCR, badge, protection de branche | **Trivy** (scan image), **gitleaks**, **Dependabot/Renovate**, **incident secret simulé** (clé commitée → pipeline rouge → rotation) ; **bonus : porter le pipeline vers GitLab CI** | 0€ |
| 5 | **Grande Ouverture** | Déploiement VPS + Nginx + domaine + **HTTPS** (cf. §7) | **Ansible** `bootstrap-vps.yml` (Docker/Nginx/firewall/user SSH) ; **backup/restore Postgres testé** (dump chiffré, cron, restauration vérifiée) | VPS + domaine |
| 6 | **Tour de Contrôle** | Uptime Kuma → Prometheus + Grafana, simulation de panne + runbook | **Logs** : JSON structurés + rotation + `journalctl` + requêtes utiles (core) ; **Loki + Promtail dans Grafana** (bonus) ; **postmortem** dans evidence/ | 0€ |

### 🔵 Cloud / IaC Plus (7 → 8, conseillé)

| # | Nom | Tu construis | Ajouts issus des revues | Coût |
| --- | --- | --- | --- | --- |
| 7 | **Le Cerveau** | Le chatbot appelle un **LLM externe**, déployé sur **GCP Cloud Run** (scale-to-zero) | Focus DevOps musclé : secrets, timeout, retry, **rate limiting**, cache, fallback, **coût/requête**, **endpoint mock pour tests de charge**, **redaction des logs** (pas de PII/prompt en clair), **quota utilisateur** | ~0€ free tier |
| 8 | **L'Architecte** | Terraform provisionne GCP (Artifact Registry + Cloud Run + IAM + DNS), **CD au merge** | **Budget cloud réel** : alerte de facturation + **preuve de teardown/coût** dans evidence/ ; renvoi vers `CLOUD_EQUIVALENTS.md` | ~0€ free tier |

### 🟣 Wow Optionnel (9, ne bloque pas la fin)

| # | Nom | Tu construis | Ajouts issus des revues | Coût |
| --- | --- | --- | --- | --- |
| 9 | **Sous Pression** | **Core** : déploiement K8s **local** (k3d/kind) : probes, requests/limits, **HPA**, Ingress, ConfigMap/Secret, **rollback**, dashboard, **Kustomize** (overlays). **Boss final** : cluster cloud éphémère multi-VM (Terraform) + **test de charge k6** + scale-up observé + `destroy` | Core local d'abord (gratuit, atteignable) ; multi-VM + k6 = boss optionnel ; **Helm** en bonus | 0€ local / centimes boss |

### 🏆 Vitrine (10, obligatoire)

| # | Nom | Tu construis | Coût |
| --- | --- | --- | --- |
| 10 | **Vitrine** | Consolidation recruteur-ready : `evidence/` complet (cf. §11), README, schéma d'archi, « ce que j'ai appris » + profil GitHub + bullets CV + pitch | 0€ |

---

## 7. Focus sur les missions sensibles

### Mission 5 — « Grande Ouverture » (mise en ligne, vulgarisée)
Jusque-là l'appli ne tourne que sur ton ordi (`localhost`) : personne d'autre ne peut y accéder.
C'est **le jour où tu ouvres ton restaurant** : l'appli devient joignable via une vraie adresse
(`https://mon-app.fr`) avec le cadenas. Tu loues un VPS, installes Docker, fais tourner l'appli,
mets **Nginx** en réceptionniste, **colles un domaine** (DNS), poses le **cadenas HTTPS**
(Let's Encrypt) et **verrouilles les portes** (firewall, user non-root).
- **Nouveauté Ansible** : au lieu de tout faire à la main, tu écris `bootstrap-vps.yml` qui
  installe Docker/Nginx/firewall/user SSH → serveur **reproductible** (Terraform crée la machine,
  Ansible la configure). Logique : à la main une fois pour comprendre → puis en playbook.
- **Nouveauté DB** : backup automatique (dump chiffré + cron) **et restauration testée** → tu peux
  dire « je sais déployer une app avec DB **sans perdre les données** ».

### Mission 7 — « Le Cerveau » (app IA externe + 1er contact GCP)
Le chatbot se met à **répondre** via un LLM externe (on garde l'externe : auto-héberger =
GPU/images lourdes/MLOps = mauvais signal junior). L'IA devient un _prétexte_ à de vrais sujets
DevOps : secrets, timeout/retry, rate limiting, cache, fallback, coût par requête, **endpoint mock
pour les tests de charge** (ne brûle pas de tokens), **redaction des logs**, quota par utilisateur.
Déploiement sur **GCP Cloud Run** (descend à zéro = quasi gratuit).
> Attention à ne pas confondre avec le §9 (« IA-assistée » = l'IA qui t'aide à bosser). Ici l'IA est **dans le produit**.

### Mission 9 — « Sous Pression » (K8s, en deux temps)
- **Core (local & gratuit)** : k3d/kind, probes, requests/limits, HPA, Ingress, ConfigMap/Secret,
  **rollback**, dashboard, **Kustomize**. Suffit déjà largement pour un junior.
- **Boss final (optionnel)** : cluster cloud éphémère multi-VM via Terraform + **test de charge k6**
  qui déclenche le scale-up (observé dans Grafana) → `destroy`. Garde-fous budget : alerte de
  facturation, checklist de teardown, endpoint mock CPU-bound pour le load test, session de 2-3h.

---

## 8. Sécurité : au fil de l'eau (renforcée par la revue)

Pas de mission SecOps dédiée (hors scope junior), mais des réflexes **concrets** placés là où ils sont naturels :

- **Mission 4** : `gitleaks` + image non-root + **Trivy** (scan vulnérabilités image) + **Dependabot/Renovate** (mises à jour dépendances) + **incident secret simulé** (clé commitée → pipeline rouge → rotation documentée).
- **Mission 5** : user non-root, firewall (ufw), durcissement SSH, HTTPS.
- **Mission 7** : clé d'API en secret, rate limiting, redaction des logs.
- **Mission 8** : secrets via Terraform/Secret Manager, IAM moindre privilège.

---

## 9. IA-assistée : le workflow DevOps 2026 (dimension transverse)

Objectif : **pas** mettre de l'IA partout pour faire moderne, mais prouver qu'un DevOps junior 2026
**utilise l'IA comme accélérateur tout en gardant une posture pro** : vérifier, tester, relire,
sécuriser, documenter. La vérification et la preuve restent plus importantes que la réponse IA.

**Mécanique** : chaque `MISSION.md` contient le bloc fixe `## 🤖 IA dans cette mission` (cf. template
§5) → *À demander à l'IA* / *À vérifier soi-même* / *Artefact à conserver*. Les artefacts (prompt,
réponse corrigée, preuve que ça marche) alimentent `ressources/AI_USAGE_LOG.md` et `flagship/evidence/`.

**Ressources dédiées** : `AI_DEVOPS_GUIDE.md` (bonnes pratiques, limites, **confidentialité — jamais
de secret/donnée client dans une IA externe**, hallucinations), `PROMPTS.md` (prompts par techno),
`AI_USAGE_LOG.md` (usages réels), et `flagship/.github/copilot-instructions.md` (bonus : pratique IA
contextualisée au repo).

**Exemples d'intégration par mission :**

| # | L'IA pour accélérer | La source de vérité (à vérifier soi-même) |
| --- | --- | --- |
| 0 | améliorer README, pitch GitHub, expliquer Git/SSH | relecture humaine, le push fonctionne |
| 1 | diagnostiquer `journalctl`, ports, firewall, systemd | les commandes de diag confirment |
| 2 | générer une 1re version de script | durcir : tests, logs, **shellcheck** |
| 3 | debugger Docker/Postgres/Alembic | **tests + migrations** valident |
| 4 | analyser un pipeline rouge, relire une PR | **CI + scans** restent la vérité |
| 5 | relire config Nginx/Ansible, checklist hardening | le déploiement réel + HTTPS fonctionnent |
| 6 | formuler des hypothèses d'incident depuis logs/métriques | **Grafana/Prometheus** confirment |
| 7 | l'IA est **dans le produit** (focus DevOps : secrets, coûts, résilience) | rate limit/cache/fallback testés |
| 8 | aider à écrire du Terraform | `terraform fmt / validate / plan` |
| 9 | expliquer events K8s, probes, HPA, pods pending | diagnostic confirmé par `kubectl` |
| 10 | améliorer README/CV/pitch | **garde-fou anti-survente** (ne revendiquer que le prouvé) |

**Phrase d'entretien à viser :**
> « J'utilise l'IA pour accélérer le debug, la documentation, les scripts et la revue, mais je ne lui
> fais pas confiance aveuglément : je valide avec la CI, les tests, les logs, les métriques, les scans
> sécurité et les commandes de diagnostic. »

---

## 10. Ressources de révision (point Codex : ne rien perdre avant l'entretien)

- `CHEATSHEET.md` — commandes par thème.
- `GLOSSAIRE.md` — vocabulaire recruteur (idempotence, reverse proxy, HPA, état Terraform…).
- `DEBUG_GUIDE.md` — « si ça casse, quoi regarder » (arbre de décision de debug).
- `CI_EQUIVALENTS.md` — GitHub Actions ↔ GitLab CI ↔ Jenkins.
- `CLOUD_EQUIVALENTS.md` — GCP ↔ AWS ↔ Azure (Cloud Run = App Runner/Container Apps, IAM = IAM/Entra ID, Cloud SQL = RDS/Azure DB…).
- `AI_DEVOPS_GUIDE.md` / `PROMPTS.md` / `AI_USAGE_LOG.md` — cf. §9.
- Chaque mission se termine par **« Ce que tu sais maintenant »** + liens vers les ancres du cheatsheet.

---

## 11. Le dossier `evidence/` (le détail qui différencie)

Dans `flagship/evidence/`, on accumule les **preuves d'opération** au fil des missions :

- capture **pipeline vert** (Mission 4) ;
- capture **dashboard Grafana** + **alerte/incident** (Mission 6) ;
- capture **app en ligne en HTTPS** (Mission 5) ;
- **schéma d'architecture** (Mission 10) ;
- **postmortem d'un incident simulé** (Mission 6) ;
- **preuve de teardown cloud + coût** (Missions 8-9) ;
- **extraits d'`AI_USAGE_LOG`** (prompt → réponse corrigée → preuve que ça marche).

> C'est ce qui transforme « j'ai suivi une formation » en « j'ai opéré un système ». Capturer la preuve fait partie de la Definition of Done de chaque mission concernée.

---

## 12. Backlog bonus & exclusions assumées

**Bonus (si l'apprenant accroche, jamais bloquant)** : Helm, Loki, SonarQube, OpenTelemetry, Vault/SOPS, Argo CD (GitOps).

**À NE PAS ajouter maintenant (signal/coût défavorable pour un junior)** : modèle LLM auto-hébergé, mission SecOps complète, Kubernetes trop profond dans le tronc principal.

---

## 13. Cadence suggérée (6 mois, ~5-8 h/semaine)

| Mois | Missions | Jalon |
| --- | --- | --- |
| 1 | Boot, Signe de vie | Un serveur public qui répond + un journal Git |
| 2 | La Forge, Mise en boîte | Backend chatbot dockerisé + migrations Alembic |
| 3 | Le Gardien, Grande Ouverture | CI (Trivy/gitleaks) + **en ligne HTTPS** + Ansible + backups |
| 4 | Tour de Contrôle | Monitoring + logs + incident/postmortem → **🟢 candidatable** |
| 5 | Le Cerveau, L'Architecte | Chatbot IA sur GCP + infra en code (CD) |
| 6 | Sous Pression (opt.), Vitrine | (K8s en bonus) + portfolio/CV/pitch prêts |

On avance à la complétion des **Definition of Done**, pas au calendrier. Dès la fin du palier
🟢 (Mission 6), on peut **commencer à postuler en parallèle** des missions 7-10.

---

## 14. État De Migration

| Élément | État |
| --- | --- |
| `README.md` | Réécrit : pitch projet-first + paliers + comment utiliser les missions |
| `PARCOURS.md` | Créé : missions + paliers + cadence |
| `agent.md` | Mis à jour : règles de style du format mission, dont bloc IA |
| `missions/` | Créé avec les 11 `MISSION.md` |
| `flagship/` | Créé avec dossiers app, migrations, Ansible, Kubernetes et evidence |
| `ressources/` | Créé avec debug, portfolio, IA, prompts, cheatsheet, glossaire, équivalences |

---

## 15. Prochaines Étapes

1. **Écrire la Mission 3 « Mise en boîte » en premier comme pilote** : squelette FastAPI chatbot + Alembic + bloc IA inclus.
2. Valider le format sur ce pilote.
3. Dérouler les missions du palier 🟢 d'abord (priorité employabilité), puis 🔵, puis 🟣/🏆.
4. Enrichir les ressources au fil des missions, sans les transformer en cours séparés.
5. Garder `AI_USAGE_LOG.md` léger : 2 ou 3 usages marquants par mission maximum.

---

## 16. Points ouverts à trancher

- **Nom du chatbot fil rouge** : idées de repo public `sidekick-chatbot`, `chatops-assistant`, `devops-chatbot`.
- **VPS** : quel hébergeur (Hetzner ~4€/mois, OVH, DigitalOcean) ? As-tu déjà un **nom de domaine** (requis pour le HTTPS, Mission 5) ?
- **CI bonus** : portage **GitLab CI** (par défaut) suffit, ou tu veux aussi un volet **Jenkins** ?
- **Compte GCP** : créé ? (300$ de crédits offerts couvrent largement tout).
- **LLM** : fournisseur (Gemini free tier généreux, Anthropic, OpenAI) ?
