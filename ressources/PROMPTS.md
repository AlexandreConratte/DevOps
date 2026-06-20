# Prompts DevOps

Ces prompts sont des points de départ. Ils doivent être adaptés au contexte réel de la mission.

## Debug Général

```txt
Tu es mon pair DevOps. Je vais te donner une erreur et le contexte.
Propose 3 hypothèses classées de la plus probable à la moins probable.
Pour chaque hypothèse, donne une commande de vérification.
Ne propose aucune action destructive sans l'indiquer clairement.
```

## Docker Compose

```txt
Voici mon docker-compose.yml et l'erreur observée.
Explique pourquoi les services ne communiquent pas.
Donne uniquement des vérifications concrètes : logs, network, variables d'environnement, healthcheck.
```

## CI/CD

```txt
Voici le log d'une pipeline échouée.
Identifie l'étape exacte qui casse, la cause probable et le plus petit correctif à tester.
Ajoute une commande locale pour reproduire le problème.
```

## Terraform

```txt
Relis cette configuration Terraform.
Cherche les erreurs de syntaxe, les variables manquantes et les risques de coût.
Ne considère pas ta réponse comme valide : indique ce que je dois confirmer avec fmt, validate et plan.
```

## Kubernetes

```txt
Voici la sortie de kubectl describe et kubectl get events.
Formule des hypothèses de diagnostic pour un pod qui ne devient pas Ready.
Pour chaque hypothèse, donne la commande kubectl qui permet de confirmer.
```

## README Portfolio

```txt
Relis ce README comme un recruteur DevOps junior.
Dis ce qui est concret, ce qui est flou, ce qui manque comme preuve, et propose une version plus directe sans survendre mon niveau.
```
