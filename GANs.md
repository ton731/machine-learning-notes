# GANs

[![hackmd-github-sync-badge](https://hackmd.io/9iU6d-hxQ3Ci1YvHBt9R5A/badge)](https://hackmd.io/9iU6d-hxQ3Ci1YvHBt9R5A)


###### tags: `AI/ML`




## Generative Adversarial Networks (GANs)

### GAN (2014)
- **Generative Adversarial Networks (Citation: 55404)**
- Discriminator負責辨別這個data是真是假，Generator負責產生很像真的的假data，以假亂真，唬discriminator。GAN的generator在學習將某個distribution的sample (ex. normal distribution)經過mapping後要很接近real data distribution。
- Discriminator的loss: max log(D(x)) + log(1 - D(G(z)))
- Generator的loss: min log(1 - D(G(z)))，但Aladdin説實務上這樣gradient會很小不好更新，所以會用 max log(D(G(z)))
- GANs對hyperparameter很sensitive，不是那麼好train。
- Discriminator在maximize target function時，其實經過推導後會很接近JS Divergence，target值越大，代表real和fake的distribution差異越大，divergence也就越大，而當real, fake兩者distribution很接近時，divergence小，也讓target的值變小。
- JS Divergence有個問題，就是當兩個distribution沒有交集時(像是人臉image在高維只是很小一個集合，因此大多情況real, fake不相交)，divergence都是log2，不論兩個distribution距離多近多遠。這讓G無法學習，因為即使現在G產生的fake distribution更靠近real了，但對D來說要max的target沒有改變，使得D也沒有被更新，而進一步讓G的進步沒有得到反饋，G自然就會學不好。（後來WGAN就是要解決JS Div的問題）


### DCGAN (2015)
- **Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks (Citation: 14027)**
- DCGAN作者將CNN融入GAN中，相較於之前GAN用fully-connected產生圖片，DCGAN用CNN架構，其中discriminator用CNN將image來output一個single value，預測為真實image之機率，而generator利用transpose convolution用100 dim的noise z來產生圖片來唬爛discriminator。
- 用這樣unsupervised learning訓練之後的discriminator，拿來當作其他supervised training如image classification的pretrain效果比其他unsupervised (KNN) 都來得好。
- 將不同Z points內插後，可以發現內插中間那些點有學到原先兩個點之間的semantic transition。而將z做vecotr arithmetic operation也可以得到例如：z(man with glasses) - z(man without glasses) + z(woman without glasses) = z(woman with glasses)。


### WGAN (2017)
- **Wasserstein GAN (Citation: 11649)**
- 作者提出Earth Mover(EM) distance，也就是wasserstein distance，衡量了一個distribution移動到成為另外一個distribution最小需要的距離。因為即使兩個distribution不相交，當距離越近時EM distance就會越小，相較於之前GAN用不能反應不相交時距離的JS divergence，EM可以幫助收斂。作者說此舉讓train GAN不用一直在意D, G之間的平衡，也不用花一堆時間去設計網路架構，也減少了mode collapse(不管sample什麼z，generator都產生同一張很像真的的output)和mode dropping (只學習到real data其中一部分的distribution)的發生。
- Discriminator的角色變成了critic，因為不再是去做classification，而是去對real/fake image打分數。而為了不讓critic直接把real image預測成無限大，critic要符合1-Lipschitz，簡單說也就是要足夠平滑。在實做上WGAN直接把critic weight做clipping到(-clip_val, clip)的範圍。


### WGAN-GP (Gradient Penalty) (2017)
- **Improved Training of Wasserstein GANs (Citation: 8200)**
- 在WGAN中，為了讓critic score符合1-Lipschitz，grad值都要等於1，直接clip掉過高過低的部分，WGAN-GP作者發現這樣會讓critic只能學到很簡單的function，降低model capacity，所以作者提出將這樣的constraint變成是penalty loss，若grad距離1越遠loss就越高，來幫助模型能學習到較複雜的function。



### GAN evaluation: Frechet Inception Distance (FID)
- aaa

### Conditaional GAN
- aaa

### Pix2Pix
- image to image translation

### CycleGAN
- unsupervised learning



