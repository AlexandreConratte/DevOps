# KUBERNETES - FICHE DEVOPS

## En bref

Kubernetes gere des conteneurs automatiquement.

Docker lance des conteneurs.

Kubernetes organise, surveille, redemarre et expose ces conteneurs.

## Image mentale

Docker prepare des boites applicatives.

Kubernetes gere l'entrepot :

- combien de boites doivent tourner;
- sur quelle machine les placer;
- que faire si une boite tombe;
- comment exposer les boites aux utilisateurs;
- comment changer de version progressivement.

## Les mots importants

| Mot | Version simple |
|---|---|
| Cluster | Ensemble de machines Kubernetes |
| Node | Machine dans le cluster |
| Pod | Plus petite unite lancee par Kubernetes |
| Deployment | Regle qui maintient des pods en vie |
| Replica | Copie d'un pod |
| Service | Adresse stable pour joindre des pods |
| Ingress | Entree web depuis l'exterieur |
| ConfigMap | Configuration non sensible |
| Secret | Donnees sensibles |
| Namespace | Separation logique dans le cluster |

## Pourquoi Kubernetes existe

En production, on veut souvent :

- plusieurs copies d'une application;
- redemarrer automatiquement si ca crash;
- deployer sans tout couper;
- repartir le trafic;
- isoler plusieurs environnements;
- gerer la configuration proprement.

Kubernetes fait ca avec des fichiers YAML.

## Exemple Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
        - name: api
          image: nginx:1.27
          ports:
            - containerPort: 80
```

Version simple :

> Je veux 2 copies de mon application `api`.

## Exemple Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api-service
spec:
  selector:
    app: api
  ports:
    - port: 80
      targetPort: 80
```

Version simple :

> Donne une adresse stable pour parler aux pods qui ont le label `app: api`.

## Commandes utiles

```bash
kubectl get pods
kubectl get deployments
kubectl get services
kubectl apply -f deployment.yml
kubectl logs pod_name
kubectl describe pod pod_name
kubectl delete -f deployment.yml
```

## Attention niveau junior

Ne commence pas par Kubernetes.

Avant Kubernetes, il faut connaitre :

- Linux;
- reseau;
- Docker;
- YAML;
- logs;
- CI/CD.

## Niveau attendu en alternance

Tu dois connaitre les bases :

- ce qu'est un pod;
- ce qu'est un deployment;
- ce qu'est un service;
- comment appliquer un YAML;
- comment lire les logs d'un pod;
- pourquoi Kubernetes est utile.

Tu n'as pas besoin d'etre expert Kubernetes pour commencer une alternance.

## Exercices

| Niveau | Exercice | Instructions | Validation |
|---|---|---|---|
| Facile | Vocabulaire | Explique pod/deployment/service | Simple et juste |
| Facile | YAML | Lis un Deployment | Tu identifies image et replicas |
| Facile | Commandes | Liste pods/services | Commandes comprises |
| Moyen | Minikube/kind | Lance un cluster local | Cluster actif |
| Moyen | Deploy nginx | Applique Deployment + Service | Pod running |
| Dur | Debug pod | Casse une image puis lis l'erreur | Cause documentee |

## Drill - 5 questions

1. Difference entre Docker et Kubernetes ?
2. C'est quoi un pod ?
3. A quoi sert un Deployment ?
4. A quoi sert un Service ?
5. Pourquoi Kubernetes peut redemarrer une app automatiquement ?

Validation : minimum 4/5.

## A retenir

Kubernetes est puissant, mais il arrive apres les bases.

Pour un junior, l'objectif est de comprendre le modele mental, pas de devenir admin cluster senior.

