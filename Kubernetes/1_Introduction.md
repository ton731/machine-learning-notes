## Introduction

### Kubernetes
- Kubernetes is a open source container orchestration tool developed by Google.
- Helps you manage containerized applications in different deployment environments.

### The need for a container orchestration tool
- Trnd from Monolith to Microservices
- Increased usage of containers
- Demand for a proper way of managing those hundreds of containers.

### What features do orchestration tools offer?
- High Availability or no downtime
- Scalability or high performance
- Disaster recovery - backup and restore



## K8s Components

### Pod
- Smallest unit of K8s
- Abstraction over container (讓你可以專注在k8s上面，而不用在意裡面的container, 裡面的container可以是docker container, 或其他的都可以)
- Usually 1 application per Pod
- Each Pos gets its own IP address (internal IP, can be used to communicate with other Pod)
- New IP address on re-creation :(

### Service
- Permanent IP address for Pod
- Lifecycle of Pod and Service are NOT connected
- 讓不同pod之間可以溝通，而ip訂下以後不會因為pods關掉重啟就需要調整溝通方式。

### Ingress
- If we want to expose our web-app to public, we already have a IP using Service, like http://124.89.101.2:8080
- 但通常我們想要 https://my-app.com，這時，可以利用在Service再加上一層Ingress來做到。
- Ingress: route traffic into cluster，讓外面的人連進來。

### ConfigMap
- Extenal configuration of your application
- 若沒有ConfigMap，當app到database的endpoint路徑改變時，要重新build, push, pull image，很麻煩，而利用ConfigMap，可以讓app image不用重來，直接去外面看config就好。

### Secret
- Used to store secret data in base64 encoding
- Database的使用者、密碼這些固然也可以存在ConfigMap，但如果只是存成plain text file很不安全，因此可以存在Secret裡面用base64編碼來保護。

### Volumes
- K8s doesn't manage data persistance!
- 如果data只存在k8s Pod裡面，當Pod停止以後data就會消失，因此可以用Volumes讓Pod可以直接連到一個實體儲存空間（local硬碟、cloud storage都可），這樣就算Pod關掉了，data還是有存著。

### Deployment
- 假設我們這一個Node1裡面的某個app Pod壞掉了，這樣會導致app server進入downtime，這樣在production是很不好的。因此解決辦法是建立另一個Node，然後在Node2再產生一個app Pod。
- Node2的app Pod會和Node1 app Pod擁有同一個Service，所以user可以用同一個網址連進去。因此這樣Node2可以作為一個load balancer。
- Deployment
    - Blueprint for app pods
    - You create Deployments
    - Abstraction of Pods
    - 真的實務上在做，要實際去產生的不是pod，而是deployment，可以在一開始就決定總共要有幾個replica。

### StatefulSet
- 在Node裡面，Database的Pod也有可能掛掉，而database無法像app一樣直接產生replica，因為DB是有state的，裡面有資料。所以比較可行的做法是讓Node1, Node2的DB Pod都指向同一個database。
- 但這樣又會產生一個synchronize的問題，因此會需要有另一個機制來管理現在是哪個pod在寫，而另一個pod就不要動，避免造成data inconsistency。這個功能就是StatefulSet。
- 所以stateLESS的Apps可以用Deployment，而stateFUL的Apps或是Database則用StatefulSet
- 但在實務上用StatefulSet其實不是很好做，有另一個常見的做法是直接把DB host在k8s外面。



## K8s Architecture
- K8s分成兩種node，master node以及working node (slave node)。

### Working Node
- Worker Nodes是真正負責跑application的，每個Node裡面會有multiple Pods
- 有3個processes是必須裝在每個Node上面的：
    1. Container runtime: 可以是Docker，也可不是，來確保Pods裡面可以跑Container。
    2. Kubelet: 來自Kubernetes，有interface with both container and node，是實際上負責start, run一個Pod的container的人，且負責分配Node的resource給Node裡面的container。
    3. Kube proxy: 負責forward the request。裡面有一些邏輯，可以讓裡面的request被送往讓資源運用更有效率的地方。
    - 通常K8s會有好幾個Working Node，每個裡面都要有這3個process installed。要怎麼讓Working Node之間彼此溝通呢？可以用Services。

### Master Node
- 每個Master node裡面有4個processes來control cluster state和那些worker nodes。
    1. Api Server: 作為master node的entrpoint，使用者可以透過UI, dashboard, CLI等API，來向master node送request。API server在收到request時，會先驗證你的權限，再把工作交給其他process。
    2. Scheduler: 當user送create new Pod的request，在經過Api server審核後，會由Scheduler來start application Pod。Schedulter會看你新的pod需要多少CPU, RAM，來決定要把你的Pod放在哪個working node。值得注意的是，scheduler只是決定new Pod要放在哪個Node，實際上執行Pod的還是Node worker的Kubelet。
    3. Controller manager: 當worker裡面有Pod死掉時，controler manager要去detect cluster changes，有發現死掉時，就會發request給scheduler去重新開始pod。
    4. etcd: key value store，cluster的brain，會紀錄pod產生、死掉等等的任何紀錄。因此schedulter, controller manager根據etcd的data來做決定。（Application data並不會存在etcd!）

- Master所需要的resource (CPU, RAM)比較少，Worker需要的resource比較多。
- Add new Master/Worker Node into server:
    1. get new bare server
    2. install all the master/worker node processes
    3. add it to the cluster
    - 這樣就可以持續擴大cluster。

