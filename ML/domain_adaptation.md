# Domain Adaptation


###### tags: `AI/ML`


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