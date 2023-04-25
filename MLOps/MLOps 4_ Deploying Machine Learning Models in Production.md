# MLOps 4: Deploying Machine Learning Models in Production


###### tags: `MLOps`


### Model Serving

- **Model Serving:**
    - Model serving是指將訓練好的ML model deploy到生產環境中，並將其對外提供服務。

- **Important Metrics:**
    - Latency: user的action和收到response之間的delay
    - Throughput: 單位時間內的number of successful requests
    - Cost: 每個inference cost應該要被minimized，如CPU, GPU, Caching等
    - 目標：minimize latency, cost, maximize throughput

- **Resources and Requirements for Serving Models:**
    - Model complexity越高，雖然accuracy會越好，但也會增加latency, computation, 和maintenance burden。因此如何balance complexity and cost就很重要。


### Model Serving: Patterns and Infrastructure

- **ML Infrastructure**
    - **On premises (本地伺服器):**
        - 在自己的hardware infrastructure 做training & deployment
        - 要自行採購CPUs, GPUs, ...
        - 對大公司來說若持續做ML是能賺錢的
    - **On Cloud (雲端伺服器):**
        - 在cloud上面train & deploy，可以用內部提供的ML workflow
        - Amazon Web Services, Google Cloud Platform, Microsoft Azure, ...

- **Model Servers**
    - Simplify the task of deploying ML models at scale. It can handle scaling, performance, some model lifecycle management etc.
    - 例如：TensorFlow Serving, TorchServe, KF Serving, NVIDIA Triton inference server
    - **TorchServe**: initiative from AWS and Facebook
        - Batch and Real-time Inference
        - Support REST Endpoints
        - Default handlers for Image Classification, Object Detection, Image Segmentation, Text Classification
        - Multi-Model Serving
        - Monitor Detail Logs and Customized Metrics
        - A/B Testing

- **Scaling Infrastructure**
    - **Horizintal Scaling over Vertical Scaling**
        - Vertical scaling: Upgrading, more RAM, faster storaget, upgrading GPU, increased power, ...
        - Horizintal scaling: More CPUs/GPUs instead of bigger ones
        - **Horizintal好處：**
            1. 更彈性，可以根據load, throughput, latency調整機器數量
            2. Application不會斷線，不用為了scaling而將現有機器關機
            3. 硬體上限沒有限制
    - Container and Container Orchestration 
        - Container比VM更方便、輕量化，可以用Docker
        - 可以再利用Container Orchestration Tools來管理containers，如Kurbernetes, Docker Swarm。

    - **Online Inference**
        - ![](https://i.imgur.com/kx13iN4.png)
        - 即時、real-time的prediction，需要optimize latency, cost, and throughput。一次對一個observation進行prediction。

    - **Data Preprocessing**
        - 在inference之前，可能會有一些preprcoessing，如：Data Cleansing, Feature Tuning, Feature Construction, Representation Transformation, Feature Selection

    - **Batch Inference**
        - 一次對 a batch of observations進行prediction。
        - Batch jobs常常是用在例行性的prediction，不用給即時的prediction。


### ETL Pipelines

### Model Management and Delivery

- **Experiment Tracking**
    - Data, Model, experiment的versioning都很重要
    - ML Model, experiment可以被如此versioning:
        - Version: Major.Minor.Pipeline
        - Major: Incompatiblity in data or target variable
        - Minor: Model performance is improved
        - Pipeline: Pipeline of model training is changed

- **Continuous Delivery**
    - **Continuous Integration (CI)**
        - Triggered when new code is pushed or committed
        - Build packages, container image, executables etc
        - Performs unit and integration tests for the components
        - Delivers the final packages to Comtinuous Delivery pipeline
    - **Continuous Delivery (CD)**
        - Deploys new code and trained models to the target environment
        - Ensures compatibility of code and models with the target environment
        - Checks the prediction service performance of the model before deploying

    - **ML Unit Testing in CI**
        - Unit testing input data: Test feature engineering logic, test values, test format
        - Unit testing model performance: Test model methods, test th emodel performance metrics, test to avoid inherent bias, test to avoid NaN values, empty strings

- **Progressive Delivery**
    - 傳統Continuous Delivery (CD)一旦發布，就會將所有的新功能或更改一次性應用在所有的客戶，會造成問題，如當新的版本有錯誤，所有客戶都會受影響，且很難快速回到先前的版本。
    - 相比之下，progressive delivery允許團隊將開發的新功能逐步推向不同的客戶，降低了deployment risk。
    - progressive delivery包含不同方法，如shadow deployment, A/B testing, Canary deployment等





