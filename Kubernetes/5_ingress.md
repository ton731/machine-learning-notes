## Ingress

### What is Ingress?
- Suppose we have my-app pod and my-app service now. If we want to access the app, we can use some endpoint like http://124.89.101.2:35010. This is enough for testing, but it's not good for production, since in production, you would like to make your service something like https://my-app.com. At this situation, you can leverage Ingress.
- Using Ingress, when a request comes from the browser, it will first reach Ingress, and then Ingress will redirect to the internal service, and then finally end up with pod.

### How to configure Ingress in your Cluster?
- Simply running Ingress alone is not going to work.
- You need an implementation for Ingress! Which is **Ingress Controller**

### What is Ingress Controller?
- it's another pod apart from the ingress
- evaluate all the rules in the cluster
- manages redirections
- entrypoint to the cluster
- many third-party implementations

### Usage
1. install Ingress Controller in Minikube
    - `minikube addons enable ingress`
    - automatically starts the k8s Nginx implementation of Ingress Controller
2. create Ingress rule
    - `dashboard-ingress.yaml`

### Use case
- Multiple paths for same host
    - Example: Google
    - One domain but many services
    - `google/calendar`, `google/mail`, ...
    - like `http://myapp.com/analytics` and `http://myapp.com/shopping`
- Multiple sub-domains or domains
    - Instead of `http://myapp.com/analytics`, use `http://analytics.myapp.com`

### Configuring TLS Certificate - https//
1. Data keys need to be `tls.crt` and `tls.key`
2. Values are file contents NOT file paths/locations
3. Secret component must be in the same namespace as the Ingress component