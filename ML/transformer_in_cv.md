# Transformer in CV


###### tags: `AI/ML`



## Backbone

### ViT (2020)
- **An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (Citation: 11914)**
- 我是先讀SETR才讀ViT的，SETR的Encoder基本上就是ViT的架構。作者拿transformer encoder來做image classification。將image拆成很多16x16的patches之後當成是sequence，丟進去tarnsformer encoder，再用output的第一個timestep output作為prediction head去預測分類。




## Semantic Segmentation

### SETR (2020)
- **Rethinking Semantic Segmentation from a Sequence-to-Sequence Perspective with Transformers (Citation: 1296)**
- 之前semantic segmentation最流行的方法FCN主要的限制在於receptive field的限制，讓model只能看到local的範圍。SETR提出用Transformer來作為Encoder (Feature Extractor)，讓model在每層transformer layer都能看到global的範圍。
- SETR將一張image分成很多16x16的patch，將每個patch中256個pixel先過linear投影到C dim的embedding space，讓image中HW/256個patch變成一個1D的sequence。而除了patch各自的embedding，他們也加入了learnable的position embedding來把spatial information加進去。在過完encoder後，會得到一個HW/256 x C維度的output，用這個作為decoder的input，來還原出原本resolution的image。
- Decoder目的是將transformer encoder的feature還原回去original resolution並做pixel-wise classification。作者提出三種decoder架構：
    1. Naive Upsampling：先用1x1 conv把diemsnsion project到class number後，直接用bilinear upsampling放大16倍回去。
    2. Progressive Upsampling (PUP)：相較於naive直接放大16倍，PUP一次只放大2倍，利用五層convolution將feature放大回去original resolution。
    3. Multi-Level Feature Aggregation (MLA)：跟Feature pyramid network有點像，利用24層transformer layer裡面的不同層layer，做一些conv, add, concat並upsample回原始尺寸。
- 訓練細節：他們都有先將image resize變成一樣大小(有看到，但待確認)，除此之外他們也有在transformer中間layer用auxiliary loss來輔助，除此之外他們也提到transformer的pretraining很重要(ViT, DeiT)。
- pytorch implementation:
    - official: https://github.com/fudan-zvg/SETR
    - https://github.com/gupta-abhay/setr-pytorch
    - https://github.com/920232796/SETR-pytorch


### SegFormer (2021)
- **SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers (Citation: 849)**
