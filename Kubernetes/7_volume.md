## Volume

### Storage Requirements
1. We need storage that doesn't depend on the pod lifecycle.
2. Storage must be availble on all nodes.
3. Storage needs to survive even if cluster crashes.

### Another Use Case: Persistent Volume
- A cluster resource
- Created via YAML file
    - kind: PersistentVolume
    - spec: e.g. how much storage
- Needs actual physical storage, like local disk, nfs, server, cloud storage, ...
- What type of storage do you need? You need to create and manage them by yourself
- **Persistent Volumes are NOT namespaced**
    - PV is outside of namespaces
    - Accessible to the whole cluster

### Local vs. Remote Volume Types
- Each volume type has it's own use case!
- Local volume types violate 2. and 3. requirement for data persistence:
    - NOT Being tied to 1 specific node
    - NOT surviving cluster crashes
- For Database persistence, use remote storage!

### K8s Administrator and K8s User
- Admin: 
    - k8s admin sets up and maintains the cluster
    - who configures the storage
    - create the PV components from these storage backend
    - usually are system administrator or DevOps engineer
- User: 
    - k8s user deploys applications in cluster
    - explicitly configure the application yaml file to use those PV, and the app has to claim that volume storage (persistent volume claim, PVC)
    - developer and DevOps team

### Storage Class
- When you are going to have hundreds of apps, you have to ask admin to create hundreds of PVs, and admin maybe has to ask another manager... It's tedious, so here comes the Storage Class.
- SC provisions persistent Volumes dynamically, when PersistentVolumeClaim claims it.
