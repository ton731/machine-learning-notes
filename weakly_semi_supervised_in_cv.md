# Weakly and Semi-Supervised Learning in Computer Vision


###### tags: `AI/ML`


- **Semi-supervised:** learns from a set of labeled (bounding box) and unlabeled images.
- **Weak-supervision:** lower degree (or cheaper) annotation at train time than the required output at test time.
- **Weakly semi-supervised:** learns from a set of labeled (bounding box) and weakly labeled (image label) images



## Weak-Supervision

### Weakly Supervised Object Detection (WSOD)
- 要做object detection，但沒有bounding box的label，只有object的tag, 例如我知道這個image和motorcycle有關，這個image和motorcycle無關。
    - Terminology
        - bag = images
        - instances = pathes，可能是用selective search或是region proposal找到的
        - positive bag: 有包含目標object的image
        - negative bag: 沒有包含目標object的image
- 挑戰：
    - Intra-bag similarities: image patches會重疊，導致不同patches會有similarity
    - Instance Co-occurrence: 像是熊通常跟草地一起出現，所以當你以為你抓到熊了，但你可能也抓到草了
- **Multiple Instance Learning:**
    - 現在data不是一個一個boudning box，而是一個一個bag，每個image可能為一個negative bag，代表裡面的patch(region proposal)沒有目標物體，也有可能是positive bag，裡面至少有一個目標物體。我們只知道這個bag是positive or negative，但我們不知道哪個region proposal (patch)是什麼class。我們要從這些bags去學怎麼做object detection抓到目標物體。 


## Semi-Supervision

### Self-Training
Idea: 用最初的label data訓練一個模型，接著去對unlabeld data預測pseudo labels，然後再用groudn truth label + pseudo label訓練一次。
- **Pseudo labeling:**
    - Total loss $L = L_{labeled} + \alpha_t \times L_{unlabeled}$
    - Pseudo label loss 的 weight $alpha_t$ 會隨著epoch而變動。一開始很低，後來隨著epoch升高。代表一開始不相信這個假label，直到原本labeled data訓練到一定時，再慢慢提高pseudo的weight。
- **Noisy Student:**
    - 首先有個先用labeled data train的老師模型，接著拿老師模型去predict unlabeled data的pseudo labels。
    - 接著訓練一個更大的學生模型（因為通常unlabeled data多很多），同時對labeled, pseudo labeled data進行學習。
    - 接著再拿這個訓練好的學生模型再去對unlabeled data預測pseudo label，接著就持續這個學生模型的iteration。
    - 學生模型在訓練時，會加入一些noise，例如data augmentation, dropout, stochastic depth (stochastic depth會隨機丟掉一些model layer，因為model很大，希望透過這樣改善generalizability)。

### Consistency Regularization
Idea: model predictions on an unlabled image should remain the same even after adding noise.
- **$\pi$-model:**
    - 把image做augmentation，預測出來的prediction distribution，除了計算entropy label loss，也把augmented predicted distribution和原先無調整的predicted distribution做squared loss，希望做augmentation後model能夠做出和先前一樣的預測。
    - 這個可以同時對labeled, unlabeled image來做。Labeled data就多去計算entropy classification loss，而unlabeled就只做predicted distribution difference loss。
- **Mean Teacher:**
    - 和pi model很像，在pi model中original image和augmented image都是用同個model，而在mean teacher裏面原先image用studement model，而augmented image用teacher model。其中student model就是很正常的一個model，而teacher model則是把不同iteration的student model做 Exponential Moving Avergae (EMA)來得到，所以不是直接學來的。
- **Virtual Afversarial Training:**
    - 和pi model很像，只是它不是用augmented image，而是用adversairal image (來自adversarial attack)。接著對original image和adversarial example去求出他們的prediction distribution，並去計算他們的KL Divergence
- **Unsupervised Data Augmentation:**
    - 對於labeled image，他只用來計算classification loss，而unlabeled image，他只做consistency loss，也就是做augmentation然後希望prediction很接近原本的。
    - 其中他augementation使用AutoAugment，讓model去學怎樣的augmentation效果最好。

<!-- ### Hybrid Methods -->


