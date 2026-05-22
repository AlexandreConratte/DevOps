# TERRAFORM ET INFRASTRUCTURE AS CODE - FICHE DEVOPS

## En bref

Terraform permet de creer de l'infrastructure avec du code.

Au lieu de cliquer dans une interface cloud, tu ecris ce que tu veux dans des fichiers.

## Image mentale

Sans Terraform :

> Je clique partout pour creer un serveur.

Avec Terraform :

> J'ecris une recette qui decrit le serveur, le reseau et les regles. Terraform applique la recette.

## Les mots importants

| Mot | Version simple |
|---|---|
| Infrastructure as Code | Infra decrite dans des fichiers |
| Provider | Plugin pour parler a un cloud |
| Resource | Element cree : VM, reseau, bucket |
| Variable | Valeur configurable |
| Output | Information affichee apres creation |
| State | Memoire de ce que Terraform gere |
| Plan | Apercu des changements |
| Apply | Application des changements |
| Destroy | Suppression de l'infra geree |

## Commandes essentielles

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
terraform destroy
```

## Exemple simplifie

```hcl
variable "server_name" {
  type    = string
  default = "devops-lab"
}

resource "example_server" "app" {
  name = var.server_name
  size = "small"
}

output "server_name" {
  value = example_server.app.name
}
```

Ce code est volontairement generique.

En vrai, la ressource depend du provider : AWS, Azure, GCP, Scaleway, OVH, etc.

## Le state

Le state est la memoire de Terraform.

Il repond a la question :

> Qu'est-ce que Terraform pense avoir cree ?

Sans state, Terraform ne sait pas comparer le monde reel avec les fichiers.

Attention :

- le state peut contenir des informations sensibles;
- il ne faut pas le modifier a la main;
- en equipe, on utilise souvent un state distant.

## Plan vs apply

| Commande | Role |
|---|---|
| `terraform plan` | Montre ce qui va changer |
| `terraform apply` | Fait vraiment les changements |

Regle :

> Toujours lire le plan avant apply.

## Niveau attendu en alternance

Tu dois comprendre :

- pourquoi l'infra en code est utile;
- ce qu'est un provider;
- ce qu'est une resource;
- a quoi sert le state;
- difference entre `plan` et `apply`;
- pourquoi `destroy` est dangereux.

## Exercices

| Niveau | Exercice | Instructions | Validation |
|---|---|---|---|
| Facile | Vocabulaire | Explique provider/resource/state | Juste et simple |
| Facile | Format | Lance `terraform fmt` sur un fichier exemple | Format propre |
| Facile | Plan | Lis un plan Terraform | Tu identifies creation/modification |
| Moyen | Variables | Ajoute une variable a un exemple | Valeur configurable |
| Moyen | Outputs | Ajoute un output utile | Output visible |
| Dur | VM cloud | Cree une VM avec Terraform | Destroy documente |

## Drill - 5 questions

1. Pourquoi utiliser Terraform au lieu de cliquer ?
2. C'est quoi un provider ?
3. C'est quoi le state ?
4. Difference entre `plan` et `apply` ?
5. Pourquoi faut-il faire attention a `destroy` ?

Validation : minimum 4/5.

## A retenir

Terraform sert a rendre l'infrastructure reproductible.

Pour une alternance, comprendre le principe et avoir cree une ressource simple suffit deja a montrer une bonne base.

