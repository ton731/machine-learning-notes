# Semantic Segmentation

###### tags: `AI/ML`



### Fully Convolutional Network (2014)
- **Fully Convolutional Networks for Semantic Segmentation (Citation: 35953)**
- 藉由conv layer取代原本CNN中的fully-connected layer，最後output一個pixel-wise的class heat map。
- 在利用CNN(AlexNet, VGG, GoogLeNet)將resolution降低、feature map數量增多後，再利用devoncolution(transpose convolution)以及shortcut(shortcut, deconvolution後的map兩者相加在一起)來慢慢將resolution放大還原為原始尺寸，來做semantic segmentation。



### U-Net (2015)
- **Convolutional Networks for Biomedical Image Segmentation (Citation: 56009)**
- 我自己覺得跟FCN挺像的，左半邊藉由CNN來降低resolution，增加feature map，找出what is in the image，右半邊利用transpose convolution和一些3x3 conv來增加resolution。
- 不過他從左邊接到右邊的skip connection 的size並沒有完全對到，左邊比較大右邊比較小，所以它是用crop的方式去match size。
- U-net, FCN不同的點：Unet是對稱的FCN不是，Unet包含更多upsampling layer，且upsampling時channel數量更多，可以更好的做localization，且Unet的skip connection是把左半邊的map concat在右半邊，而FCN是直接add在一起。


### Loss function for semantic segmentation (2020)
- **A survey of loss functions for semantic segmentation (Citation: 500)**
- 沒有一種loss function是universal最通用的，要看data properties，例如distribution, skewness, boundaies...
- Balanced dataset: binary cross entropy loss
- Midly skewed dataset: smoothed or generalized dice coefficient
- Highly imbalanced segmentation: focus based loss function (focal loss)



