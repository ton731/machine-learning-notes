# Data Imbalance and Domain Adaptation


###### tags: `AI/ML`


## Data Imbalance
- 真實large-scale datasets通常是long tailed (imbalance)
- Imbalance Ratio $IR = \frac{N_{majority}}{N_{minority}}$

### Resampling
- Undersampling：多的變少
- Oversampling：少的變多

### Reweighting
- Thresholding：調整classifier做decision時的threshold。用貝氏定理將$p(i)$這個對class的prior做調整，數量少的class prior就調高點。
- **Class-Balanced Loss Based on Effective Number of Samples (2019)**: 計算整個dataset裏面實際的effective sample number，接著再用這個effective number作為loss function中的weighting。原本reweighting有個很直覺的方式是用這個class佔data的比例之倒數作為loss的權重，這篇主要的不同是比起直接用佔比，他先計算了effective sample number。

### Problems in Rebalancing Tricks
- **Resampling問題：** 做resmapling可能會導致minor class容易overfitting，而其他的class underfitting。
- **Reweighting問題：** Reweighting可能會因為調整loss weight而distort原始data的分佈。

### Trick Combinations: 怎麼結合同時解決resampling & reweighting的問題
- 一般CNN可以分成 Feature Extractor & Classifier。而學習過程可以分成representaiton learning & classification learning。
- **A example framework for long-tailed visual recognition:** 用Two-stage的訓練，第一次訓練feature extractor + classifier，第二次固定feature extarctor，只訓練classifier。並在兩次都有三種策略：(1)用原始cross entropy, (2)做resampling, (3)做reweighting。實驗完發現最好的策略是第一次訓練用原始cross entropy訓練，不做rebalance，而第二stage則用resampling來做。
    - 第一次不做rebalance可以讓學到的feature更有代表性。
    - 第二次用resampling開始慢慢加入imbalance的方法。
    - Firstly learn the universal features, then pay attention to the tail data gradually。


## Domain Adaptation
- Overcoming the dataset bias：train的資料跟實際用的資料不一樣
- 又叫domain bias, domain shift

### Adversarial domain alignment
- **Feature-space:** 在feature space中加入一個domain discriminator，讓新domain和舊domain利用Encoder CNN所output的feature會越接近越好。同時利用classifier loss和GAN loss，其中clf loss去找出feature space的decision boundary，而GAN loss則為判斷兩個domain的feature的discriminator loss。
- **Pixel-space:** 其實就是風格轉換，跟SimGAN類似的概念，將input domain A image 透過 NN 來轉換成 domina B image，然後利用discriminator來讓兩個domain產生的feature要很像。(Pixel space的disc是加在featuer space，而SimGAN是加在input image space)

### Beyond adversarial alignment
- **Category shift:** 除了domain會變以外，新的domain裡面包含的object category可能也會變。
    - **Universal Domain Adaptation:** 通常假設target domain是unlabeled，而我們不知道target domain還有什麼class。無法保證新的class在原本的feature space會怎麼分佈，導致會出問題
- **Feature disentanglement:** 將feature map分成兩個部分，domain-specific以及domain-invariant。其中domain-specific去預測這是來自哪個domain，而domain-invariant判斷image中的物體。因此在inference時，先將image轉成feature，接著只取domain-invariant部分的feature出來做預測，就不管domain-specific那部分學習風格的feature。
    - 有個有趣的應用，拿來做同個人不同年紀之間的face recognition。(Disentangled Representation for Age-Invariant Face Recognition: A Mutual Information Minimization Perspective, 2021)