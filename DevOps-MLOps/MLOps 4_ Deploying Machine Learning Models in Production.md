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



### Model Monitoring

- **Monitoring Targets in ML**
    - Basics: **Input and output monitoring**
        - Model input distribution
            - Does distributions align with what you've seen in the past?
        - Model prediction distribution
            - Unsupervised: Compare model prediction distributions with statistical tests (median, mean, standard deviation, min/max values)
            - Supervised: When labels are available
        - Model versions
        - Input/prediction correlation
    - **Operational Monitoring**
        - Latency
        - IO / Memory / Disk Utilization
        - Sysyem Reliability (Uptime)
        - Auditability

- **Logging for ML Monitoring**
    - **目標：Build observability**
        - 從能夠開箱及用(out-of-the-box)的
        logs, metrics, dashboards開始
        - 加入agent來搜集、分析logs, metrics
        - 加入一些log-based metrics來作為alert的基礎
        - 用aggregated sinks & workspaces來centralize logs和monitoring
        - 紀錄從request傳來的data作為之後新的training data
    - Logging pros & cons
        - Pros: 容易產生、可以提供valuable insight、專注在特定事件
        - Cons: 過多logging會影響系統效能、log-based alerts可能代價昂貴

- **What is Model Decay**
    - **Model Decay**
        - ML production operate的環境可能會隨時間變化，若model都是static且沒有改變，可能會離真實環境越來越遠。
    - Model decay 原因
        - Data Drift (Feature Drift): input的distribution改變
        - Concept Drift: 同樣的input但output改變
    - Detcting drift on time:
        - Drift在系統會隨時間慢慢產生影響，若沒偵測到，會影響表現，因此要及早monitor & detect。

- **Model Decay Detection**
    - Detecting drift:
        - 利用logged data, model predictions, ground truth (如果有的話)來計算統計上的特徵。可以在dashboard畫個圖來方便觀察。
        - 有一些library可以detect drift: TensorFlow Data Validation, Scikit-multiflow library

- **Ways to Mitigate Model Decay**
    - 如果已經偵測到decay，我們可以：
        - 看看training data裡面哪些部分還是正確的（如果可以）
        - 保留好data，丟掉壞data，和增加新data
        - 丟掉某個時間以前的data，然後加入新data
        - 直接重新產生新dataset
    - Fine Tune, or Start Over?
        - 都可以，都直得試試，不過也要看有多少新的labeled data。
    - Model Re-Training Policy
        - On-Demaind: 人工去re-train
        - On a Schedule: 如每天、每週、每個月
        - Availbility of New Training Data: 當對某種特定data有特別需求
    - Redesign Data Processing Steps and Model Architecture
        - 當decay超過可接受程度時，可以考慮崇熙設計整個pipeline，如feature engineering, feature selection，model architecture等。

- **Privacy Issue**
    - 許多規範對用戶的隱私進行規範，有兩個常見的做法：Anonymization, Pseudonymisation。
    - Anonymization: 對data進行irreversible的transform，使得就算是負責ananymization的team都無法辨認出哪個data是哪個user的。
    - Pseudonymisation：將data裡面有user便是資訊的部分，如email, name隨機用一些別名、化名方式來取代。

    

