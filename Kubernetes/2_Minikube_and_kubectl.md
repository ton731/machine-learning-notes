## Minikube
- 在production階段，通常會有兩個以上的master node，和好幾個worker node，其中每個node可能會在physical (local)或是virtual (cloud) machine上面。
- 這讓開發者很難在自己local電腦上測試，因為可能沒有那麼多的資源。
- 這時minikube是一個工具，他在你電腦上用virtual box開了一個虛擬環境，建立一個Node，接著他把Master proceses和Worker processes都裝在這個Node上面，讓開發者在local也可以輕易測試。可以想成是一個 1 Node K8s cluster，主要是for testing pruposes。
- 在Minikube中，
    - Kubectl CLI is for configuring the Minikube cluster
    - Minikube CLI is for start up/deleting the cluster


### Commands
```bash
minikube start
minikube status
```


## kubectl
- kubectl是k8s cluster的command line tool，用kubectl可以跟master node的Api Server互動。
- kubectl可以用在任何kubernetes cluster，像是Minikube cluster，或是Cloud cluster都可以用kubectl。

### Commands: Status of different K8s components
```bash
kubectl version
kubectl get nodes
kubectl get pod
kubectl get pod -o wide
kubectl get services
kubectl get replicaset
kubectl get deployment
```

### Commands: CRUD (create, read, update, delete)
- Pod is the smallest unit. BUT, you are creating Deployment, which is the abstraction over Pods
- Deployment is the blueprint for creating pods, and is the most basic configuration for deployment.
- Replicaset is managing the replicas of a Pod.
- **Layers of Abstraction: Deployment manages a ReplicaSet. ReplicaSet manages a set of Pods. Pod is an abstraction of Container.**
```bash
# create deployment
kubectl create deployment [name] --image=nginx

# create deployment via config yaml file
kubectl apply -f [file name]

# edit deployment
kubectl edit deployment [name]

# delete deployment
kubectl delete deployment [name]

# delete with configuration file
kubectl delete -f [file name]
```

### Commands: Debugging pods
```bash
# log to console, it shows the logging printed by
# the pod, and it's useful for debugging
kubectl logs [pod name]

# describe
kubectl describe pod [pod name]

# get interactive terminal
kubectl exec -it [pod name] -- bin/bash
```