# Guide IA Pour DevOps

Objectif : utiliser l'IA comme accélérateur sans lui déléguer le jugement.

## Bon Usage

Utiliser l'IA pour :

- expliquer une erreur ;
- proposer une première version de script ;
- relire une configuration ;
- générer des hypothèses de debug ;
- reformuler un README ;
- préparer une phrase d'entretien.

## Source De Vérité

Une réponse IA ne valide rien toute seule.

Toujours confirmer avec :

- tests ;
- CI ;
- logs ;
- métriques ;
- scans sécurité ;
- `terraform plan` ;
- `kubectl describe` ;
- commandes de diagnostic ;
- documentation officielle quand le détail compte.

## Confidentialité

Ne jamais envoyer à une IA externe :

- secret ;
- clé API ;
- token ;
- mot de passe ;
- donnée client ;
- dump de base ;
- fichier `.env` réel ;
- information privée d'entreprise.

Remplacer par des valeurs factices avant de demander de l'aide.

## Hallucinations

L'IA peut inventer :

- options CLI inexistantes ;
- syntaxes obsolètes ;
- noms de ressources cloud faux ;
- configurations dangereuses ;
- explications plausibles mais fausses.

La bonne posture : demander, tester, corriger, documenter.

## Phrase D'entretien

> J'utilise l'IA pour accélérer le debug, la documentation, les scripts et la revue, mais je valide toujours avec la CI, les tests, les logs, les métriques, les scans et les commandes de diagnostic.
