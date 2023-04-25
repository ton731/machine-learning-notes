# MLOps 1: Introduction to Machine Learning in Production


###### tags: `MLOps`


## Week 1: Overview of the ML Lifecycle and Deployment

### Life Cycle of a ML Project
![](https://i.imgur.com/jlnOqe5.png)
1. Scoping
    - **Define project**
    - Define target, key metrics
    - Estimate resource and timeline
2. Data
    - **Define data and establish baseline & Label and organize data**
3. Modeling
    - **Select and train model, Perform error analysis**
    - 3 key inputs for ML model:
        - Code (algorithm, model)
        - Hyperparameters
        - Data
    - In research/academia, usually fix data and adjust code & hyperparmeters
    - In production, usually fix code and adjust hyperparameters & data
4. Deployment
    - **Deploy in production & Monitor and mantain system**

### Key Challenges
- Deploy時的主要挑戰可分為兩類：(1) machine learning or the statistical issues, (2) software engine issues。
- **Machine learning and statsistical issue:**
    - Concept drift & Data drift: 當deployment後有新的data進來時，新的data可能會和之前train的data不太一樣，使得model需要重新訓練
    - Concept drift: x -> y 這個mapping改變，如房價變貴
    - Data drift: x 改變，如影像光源都改變了
- **Software engineering issues:**
    - Checklist of questions
        - Realtime or Batch
        - Cloud vs. Edge/Browser
        - Compute resources (CPU/GPU/memory)
        - Latency, throughput (QPS, query per second, 吞吐量)
        - Logging (記錄用戶使用、預測的這些資訊)
        - Security and privacy

### Deployment Patterns
- Common deployment cases
    1. New product/capability
    2. Automate/assist with manual task
    3. Replace previous ML system
    - Key ideas: (1) Gradual ramp up with monitoring, (2) Rollback
- **Shadow mode:**
    - ML systems 跟 human 同時平行在跑
    - 但ML的output沒有被用來做decision
    - 好處是可以用來verify ML algorithm
- **Canary deployment:**
    - 一開始只讓ML佔很小的traffic，如5%
    - 後續持續monitor system然後再逐漸調高traffix
- **Blue green deployment:**
    - 當有新的 New/Green version進來，讓系統保留原始舊的 Old/Blue version，這樣好處是當新的表現不好，可以隨時切換還舊的穩定的
- Degrees of automation:
    - Human only --> Shadow modw --> AI assitance --> Partial automation --> Full automation

### Monitoring
- 可以用dashboard來記錄、監控一些metrics，如：
    - **Software metrics**: Memory, compute, latency, throughput, server load...
    - **Input metrics:** Avg input length, Num missing values, Avg image brightness...
    - **Output metrics:** times return null, times user redoes search, click through rate...
- 可以設定threshold for alarms!
- **Pipeline monitoring:** 可能一個service中包含數個ML model，彼此可能會互相影響performance，這時候monitor會比較複查但也很重要，可以用上面那些metrics來監控每個ML model的狀況


## Week 2: Select and Train a Model

### Model-centric vs. Data-centric AI development
- 在practical cases中，data-centric AI development可能會更方便，因為code的部分可以先固定，例如從github抓，想如何去改善data quality會比較實際

### Why low average error on test set isn't good enough?
- **Performance on disproportionately important examples:** 有些部分的預測會比其餘重要很多，錯一個就會影響很大，但是整體test error低不代表在這部分預測表現會好。
- **Performance on key slices of the dataset:** 有時test error表現很好，但像是loan approval case，ML model評斷標準可能涉及到種族、性別、地區等等因素，這樣是不被允許的。又像是推薦系統，可能都推薦大廠牌的東西而不推薦小廠牌，雖然總score可能是高的，但對小廠牌不公平。
- **Rare classes**: skewed data distribution，若出現model一律猜0或猜1，在production會出問題。

### Establish a baseline
- Unstructured and structured data
    - 對於unstructured data如影像、聲音、文字，通常human level performance (HLP)是一個很好的baseline
    - 而對於structured data如excel sheet，HLP就沒辦法做到太好

### Tips for getting started
- **Getting started on modeling**
    - 從literature search, courses, blogs, open-source projects看看有沒有可行和已經寫好的implementations可以用
    - 不要去找那些上週才出的cutting edge的paper來做，通常a resonable algorithm with good data will often outperform a great algorithm with no so good data.
- **在選model時要考量到deplyment constraints嗎？**
    - Yes, 如果已經有baseline且目標是要biuld and deploy。
    - No (or not necessarily), 如果只是要建立baseline或嘗試看看哪個方向直得深入研究。
- **Sanity-check for code and algorithm**
    - 在訓練真正大dataset前，一定要先確定code, algorithm可以overfit一個很小的dataset。

### Error analysis and performance auditing
- **Error analysis example:**
    - 可以看看在dev set裡面哪些case是不好的，他們不好的原因是什麼？可以用tag的方式記錄在excel sheet，或是現在有些MLOps工具也可以協助。
    - 有了這些tag後，我們可以看看像是：(1)多少比例的error有這個tag, (2)所有有這個tag的資料中，多少有error, (3)多少data有這個tag, (4)這個tag的data還有多少improve空間？
- **Prioritizing what to work on**
    - 可以看目前不同tag的data還差benchmark多遠，以及他們各佔data總共的比例是多少，來決定要優先改善哪一部份的error，可以最大程度改善結果。
    - 除此之外，也可以考慮那種類型error出現的頻率、改善的難度、改善空間有多大等等來評估
    - 改善方法：增加更多data, 用data augmentation, improve label accuracy/data quality...
- **Skewed datasets**
    - 用recall, precision, f1 score 來取代僅僅只看accuracy
- **Performance auditing**
    - 在model要正式進入production前的最後確認，可以確認如accuracy, fairness/bias和其他問題：
        1. Brainstorm系統在哪些情況可能會出錯，如特定某族群、性別的data，或rare class performance等
        2. 在這些可能會出錯的狀況中建立合適的metrics

### Data iteration
- **Data-centric AI development:** data的quality是最重要的，當quality夠好，許多不同的model都能夠有好的表現。因此應該專注於提升data quality。
- **Data augmentation:**
    - **目標:** 產生realistic examples that (1) the algorithms does poorly on, but (2) haumans or baseline do well on.
    - Checklist: (1) Does it look realistic? (2) Is the x-> y mapping clear? (can human recognize it?) (3) Is the algorithm currently doing poorly on it?
    - Data iteration loop: Add/improve Data(holding model fixed) --> Training --> Error analysis --> Add/improve Data
- **Can adding data hurt?**
    - 照理說data augmentation應該只對training set做，所以最後training set和dev, test set distribution有些許不同是正常的。
    - 對unstructured data，當(1) model is large (low bias), (2) the mapping x->y is clear (人類可以輕鬆判斷) ，那加入data幾乎不會傷害accuracy。
- **Adding features:**
    - 對structured data來說，data augmentation很難做，所以比較實際的作法還是去尋找有用的feature然後加上去。
    - 雖然DL號稱不用再做feature engineering，但那比較是對於如image, text這種unstructured data，當我們在用structure data且數據不多時，feature engineering還是很重要。Data越多、資訊越多，越能走向end-to-end的training方式。
- **Experiment tracking**
    - 紀錄自己做過什麼很重要，如algorithm/code versioning, dataset used, hyperparameters, results
    - 而記錄的方式，可以從簡單的text files, 到比較scalable的spreadsheet，又或者更進階的experiment tracking system。
- **From big data to good data:**
    - Try to 確保在ML project lifecycle各個階段都有consistently high quality data。
    - Good data 包含：(1) Cover到重要cases, (2) 有明確, consistent 的 x->y, (3) 有即時的production data作為feedback (data, concept drift), (4) Data size 合適


## Week 3: Data Definition and Baseline

### Define data and establish baseline
- **Major types of  data problems:**
    - Data: unstructured vs. structures, small data vs. big data
    - small data: clean label are critical
- **Small data and label consistency:**
    - Label consistency 在 small data格外重要
    - Big data也會遇到small data的challenge，當data裡面有long tail rare events
- **Human level performance (HLP):**
    - **Why measure HLP?** (1) 可以看有沒有bayes error / irredducible error 可以幫助我們對error做分析和對未來優化方向做選擇；(2) 在學術中作為benchmark；(3) 可以看實務上最好表現可以到什麼程度。
    - **HLP問題：** 若ground truth是根據某個labeler或human所label出來的，而由另外一個labeler所label出來的答案作為HLP，那這樣會導致HLP實際上是在算two random labelers agree的機率，導致HLP偏低。而ML則會學習如何agree with humans，所以很有可能ML的performance比HLP高，但實際上表現卻沒HLP好。
    - **Raising HLP:** 當HLP << 100%時，有可能是因為label inconsistency造成的問題，試著去改善這方便也會對label的乾淨程度有幫助。
    
### Label and organize data
- **Obtaining data:**
    - 要盡快進到model+hyperameters+data -> training -> error analysis這個loop裏面
- **Meta-data, data provenance and lineage:**
    - meta-data: 描述data的data，如一個影像x，又包含了拍照時的焦距、手機模型、時間、地點等等
    - data provenance: 在整個data pipeline間，某個data從哪來
    - data linage: 每個步驟的順序、流程
    - 紀錄meta-data可以在data出問題時很容易找到問題的來源





