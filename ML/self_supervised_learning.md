# Self-supervised Learning in Computer Vision


###### tags: `AI/ML`


- **Why self-supervised learning?**
    - In self-supervised learning, we replace human annotations by **creatively exploiting** some property of data to set up a pseudo-supervised task.
    - 例如：
        - **Rotation:** 將unlabeled image旋轉，去預測旋轉角度
        - **Colorization:** 將image轉成grayscale，去預測rgb image
        - **Super Resolution:** 將image縮小，去預測原始尺寸
        - **Image Inpainting:** image中間挖掉一塊，去預測被挖掉的
        - **Jigsaw Puzzle:** 將image切成patch，用亂patch順序，去預測patch排序
        - **Context Prediction:** 將image切成patch，去預測哪些patch是某個patch的哪個相對位置
        - **Frame Order Verification:** 從video取出幾個frame，去預測frame的順序
    - Once we use self-supervised learning to learn representations from these million of images, we can use transfer learning to fine-tune it on some supervised task like image classification.


## Self-Supervised Paradigms

### Reconstructive
- **Masked Auto-Encoders (MAE)**
    - **Masked Autoencoders Are Scalable Vision Learners (CVPR 2022)**
    - 被公認為self-supervised最有用的，可以將影像mask掉70-80%，然後還原回去，這樣找出來的representation很好。
    - Encoder: 只input沒有被mask掉的、看得到的patches，算出這些patch的representation，然後再把masked掉的patch補回原本的順序。
    - Decoder: 拿各個patch的representation (包含masked, non-masked patches)，還原回去原始的image。
    - 非對稱，encoder比較大，decoder比較小。
    - MAE的downstream task: 將一個完整的image input encoder後，就可以得到一個image的representation。


### Contrastive
- **Contrastive learning with negative examples**
    - **SimCLR**
        - **A Simple Framework for Contrastive Learning of Visual Representations (ICML 2020)**
        - 將一個original image做random transformation, augmentation，得到transformed image，要去maximize這兩個image在representation上的similarity。
        - 首先先用一個CNN得到兩張image的representation。接著他後面還有個projection head來對representation做nonlinear transform，出來以後就可以算original image & transformed image他們特徵的cosine similarity。
        - 在算loss時，用了一種特別的cross entropy，考慮了original image & transformed image的similarity，也考慮original image & another diffferent image的similarity。一個要大(positive example)，一個要小(negative example)。
        - 中間學到的representaiton就可以用在downstream tasks。
    - **MoCo**
        - **Momentum Contrast for Unsupervised Visual Representation Learning (2019)**
        - SimCLR用同一個mini-batch的其他照片作為negative examples，所以negative examples是和batch-size綁在一起的。
        - MoCo藉由momentum encoder和一個queue of activations來decouple batc-size和negative example的關係。
- **Contrastive learning without negative examples**
    - BYOL
        - 只有用到SimCLR的positive sample部分，image和augmented image兩個的representation要很接近。
        - 因為沒有negative sample，為了避免model對這兩個image都預測0，他多加了一個MLP在後面來防呆。