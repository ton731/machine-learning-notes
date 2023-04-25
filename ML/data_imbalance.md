# Data Imbalance


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