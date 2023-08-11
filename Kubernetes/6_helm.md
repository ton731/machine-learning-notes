## Helm

### NOTICE!
Helm changes a lot between versions, so, understand the basic common principles and uses cases will make it eaiser to use in practice no matter which version you use.

### What is Helm?
- Package Manager for Kubernetes
    - To package YAML files and distribute them in public and private repositories
    - It's like a github repo for k8s cluster setting. Some people may have already tried the settings for example, a database app, then he can package it as a Helm Chart, and then you can download and run the cluster with it directly.
    
### Feature 1: Helm Charts
- Bundle of YAML files
- Create your own Helm Charts with Helm
- Push them to Helm repository
- Download and use existing ones

### Feature 2: Templating Engine
- In some cases, you will have many microservices in your k8s cluster, and most of the yaml files are similar, only with different app name or image name. 
- With Helm, we can define a template file, so that you don't need to have many yaml files for each service, you only need to have one template yaml:
    1. Define a common blueprint
    2. Dynamic values are replaced by placeholders
    3. Create a values file which defines the yaml settings for each microservices
- This is very practical when you are using continous integration/delivery (CI/CD)
    - In your Build you can replace the values on the fly

### Another Use Case: Same Application across different environments
- When you want to deploy an application in different envs, for example, Development, Staging, and Production, you don't have to deploy the yaml files seperately.
- You can use Helm to package the files as your own chart, so that you can deploy it with one line in different environments.

### Helm Chart Structure
Directory structure:
- `mychart/`: name of the chart
    - `Chart.yaml`:  meta info about chart
    - `values.yaml`: values for the template files
    - `charts/`: chart dependencies
    - `templates`: the actual template files
    - `README or license, ...`
- Deploy: 
    - `helm install <chart-name>`: this will use the `values.yaml` as default setting
    - `helm install --values=my-values.yaml <chart-name>`: this will override the default `values.yaml`

### Feature 3: Release Management
Helm Version 2 vs. 3
- Helm Version 2 comes in two parts:
    1. CLIENT (helm CLI): send request to Tiller
        - `helm install <chart-name>`
    2. SERVER (Tiller): run the components and stores copy of the chart configuration
    - Tiller keeps track of all chart executions:
        - `helm install <chart-name>`
        - `helm upgrade <chart-name>`
        - `helm rollback <chart-name>`
    - Downsides of Tiller:
        - Tiller has too much power inside of k8s cluster
        - Security issue
- So in Helm V3, Tiller got removed!

