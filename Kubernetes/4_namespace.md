## Namespaces

### What is a Namespace?
- Organise resources in namespaces
- Virtual cluster inside a cluster

### 4 Namespaces per Default
`kubectl get namespace`
- kube-system
    - Do NOT create or modify in kube-system
    - System process
    - Master and Kubectl processes
- kube-public
    - Publicly accessible data
    - A configmap, which contains cluster information
    - `kubectl cluster-info`
- kube-node-lease
    - Heartbeats of nodes
    - Each node has associated lease obkect in namespace
    - Determines the **availability of a node**
- default
    - Resources you create are located here

### Create a Namespace
- `kubectl create namespace my-namespace`
- Create a namespace with a configuration file (better)

### Why to use Namespace?
1. Everything in one Namespace is not clean --> Group resources in Namespaces
    - Officially: Should not use for smaller projects (to 10 users)
    - Nana: It's always a good way to use namespace, since even small project can has a lot of services and deployments
2. Conflicts: Many teams, same application
    - If different teams have same applications in a namespace, it may cause some conflict issue
3. Resource Sharing: Staging and Development
    - We can place Staging and Development in the same cluster with different namespaces, so that these two can directly use the other common resources like Nginx-Ingress Controller and Elastic Stack placed in the same cluster
    - **Blue/Green Deployment:** Production Blue and Production Green, they can both use the common shared resources
4. Access and Resource Limits on Namespaces:
    - When there are several teams using a single cluster, using namespace can limit the access to different namespace. It can also limit the CPU/RAM/Storage resources to different team (namespace).

### Characteristics of Namespace
- You can't access most resources from another Namespace
    - Each Namespace must define own ConfigMap/Secret
    - Service can share across namespace
- Components, which can't be created within a Namespace
    - live globally in a cluster
    - you can't isolate them
        - `kubectl api-resources --namespaced=false`
        - `kubectl api-resources --namespaced=true`
        - volume
        - node

### Create component in a Namespace
- By default, components are created in a default Namespace
- `kubectl get configmap -n default` is same as `kubectl get configmap`
- `kubectl apply -f mongo-configmap.yaml --namespace=my-namespace`
- Or we can include the namespace information in the config file (recommended, since it is documented and useful for automated deployment):
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
    name: mongo-configmap
    namespace: my-namespace
data:
    ...
```
