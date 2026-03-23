
# App Deployment using Kubernetes

Simple app created using Python and deployed using Docker and Kubernetes.
## Deployment

To deploy this project first run

```bash
  minikube start
  
  minikube dashboard
```

Then use the kubectl to for deployment

```bash

kubectl apply -f deployment.yaml

```
Then use the kubectl to apply the service

```bash

kubectl apply -f service.yaml

```
Port Forwarding :

```bash

kubectl port-forward svc/fenrir 5000

```
## Authors

- Sahil Jha

