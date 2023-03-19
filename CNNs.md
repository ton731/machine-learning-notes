# CNNs

[![hackmd-github-sync-badge](https://hackmd.io/bsYG6g9oQ1e3JmrUQTx8GA/badge)](https://hackmd.io/bsYG6g9oQ1e3JmrUQTx8GA)


###### tags: `AI/ML`



## Computer Vision Related Videos/Tutorials
- **Pytorch Tutorials (CV, NLP) - Aladdin Persson: https://www.youtube.com/playlist?list=PLhhyoLH6IjfxeoooqP9rhU3HJIAVAJ3Vz**
- Computer Vision — Andreas Geiger: https://www.youtube.com/playlist?list=PL05umP7R6ij35L2MHGzis8AEHz7mg381_
- Andrew Ng Convolutional Neural Networks: https://www.youtube.com/playlist?list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF
- The Ancient Secrets of Computer Vision (YOLO v1-v3 author): https://www.youtube.com/playlist?list=PLjMXczUzEYcHvw5YYSU92WrY8IwhTuq7p
- One-stage, Two-stage Object detection: https://www.youtube.com/@hgffly/videos


## Great CV article writers
- https://ivan-eng-murmur.medium.com/
- https://medium.com/@chingi071
- https://chih-sheng-huang821.medium.com/



## CNN Architecture

### AlexNet (2012)
- **ImageNet Classification with Deep Convolutional Neural Networks (Citation: 122186)**
- 他們提出了一個比之前都深的CNN model(5 conv + 3 fc)，而這麼大的model及這麼多參數就需要解決速度慢及overfitting的問題。針對速度慢，他們使用ReLU,多GPU來加速，overfitting部分則使用data augmentation及dropout來改善，最後結果比前人都好。
- top-1, top-5 accuracy & error rate: top-1 acc是model預測出機率最高的class等於truth的機率, top-5則是屬於機率前5高的



### Network In Network (2013)
- **Network In Network (Citation: 7695)**
- 提出兩個主要概念：(1) MLP Convolutional Layer (1x1 convolution), (2) Global Average Pooling (GAP)
- MLP Convolutional Layer: 一般的convolution+relu像是對input用一個線性function+relu，作者認為這樣的表達能力不夠，因此用mlpconv。mlpconv在經過一個convolution後，用一個MLP對單一pixel的所有channel做轉換、融合，相當於channel-wise pooling(Cascaded Cross Channel Parametric Pooling, 1x1 convolution)。
- GAP：原先CNN架構裡面最後用的fully-connected很容易overfit，所以作者提出在最後一層將channel數量調整至與class數量相同，而將某個channel的feature map做average，來得到那個class的confidence，最後得到每個class的confidence再過softmax，這樣可以強迫model去學confidence，且不用任何額外參數，減少overfit影響。
- references
    - https://zhuanlan.zhihu.com/p/40050371
    - https://chih-sheng-huang821.medium.com/%E5%8D%B7%E7%A9%8D%E7%A5%9E%E7%B6%93%E7%B6%B2%E8%B7%AF-convolutional-neural-network-cnn-1-1%E5%8D%B7%E7%A9%8D%E8%A8%88%E7%AE%97%E5%9C%A8%E5%81%9A%E4%BB%80%E9%BA%BC-7d7ebfe34b8
    - https://meetonfriday.com/posts/a151bfa2/
    - https://medium.com/@chensheep1005/network-in-network-d847f9232846
- **1x1 convolution:** 簡單來說1x1在調整feature map的channel數量（升維、降維），在inception, resnet都有用到，可以適當地減少模型參數量，並且可以提高模型之nonlinearity，可以視為對單一pixel的所有channel用fully-connected做整合、讓不同channel間彼此訊息交通。



### VGG (2014)
- **Very Deep Concolutional Networks For Large-Scale Image Recognition (Citation: 93108)**
- 相較於之前ImageNet透過僅有幾層convolutional layer(如5層)和較大的kernel(5x5, 7x7)，VGG提出使用更深的convolution layer (11-19層)，並使用最小的kernel:3x3。
- 疊兩層3x3 kernel可以達到一個5x5 kernel的receptive field，三層可以達到7x7，而之所以用三層3x3而不用一個7x7是因為參數量更少。3個3x3 --> 3 * (C * 3 * 3) = 27C，而一個7x7 --> 1 * (C * 7 * 7) = 49C，因此可以將三層3x3視為一層7x7的regularization。



### GoogLeNet (2014, Inception v1)
- **Going deeper with convolutions (Citation: 45704)**
- 22層，由數個包含multi scale的inception module構成的model，主要有兩個特別的地方：(1) Inception module, (2) Intermediate output layer (我自己叫這麼名字)
- Inception module: 關於kernel要用3x3, 5x5等多大尺寸一直有套論，Inception覺得那就全都用。一個module裏面包含1x1, 3x3, 5x5, max-pool這四個的conv，做完以後這四個在channel dimension concat起來 (注意：必須讓feature map的spatial resolution保持不變，因此需要做padding)，而為了減少計算成本，在3x3, 5x5 conv之前都有先用1x1 conv來做dimenstion reduction，而也有在max-pool之後用1x1來減少dim。
- Intermediate output layer: 因為層數多，為了能讓他好train，容易backprop，讓中間的conv layer角色很重要。因此他們在中間多做了兩個softmax output layer，並在訓練時也用中間兩層來預測，計算loss(weight=0.3)，來讓中間層數的featuer map具有一定意義幫助訓練。
- references:
    - Andrew Ng inception module: https://www.youtube.com/watch?v=C86ZXvgpejM&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF&index=19
    - https://ithelp.ithome.com.tw/articles/10205210
    - https://medium.com/%E5%AD%B8%E4%BB%A5%E5%BB%A3%E6%89%8D/googlenet-inception%E7%9A%84%E6%BC%94%E9%80%B2-f8a5641e99c3



### ResNet (2015)
- **Deep Residual Learning for Image Recognition (Citation: 147354)**
- ResNet主要想解決很深的網路不好訓練的問題，即疊越多層training error可能更高，照理說capcacity更高應該要不比原先差。
- 透過short cut(residual)，y = F(x) + x，每2-3個layer加入一個residual connection作為一個building block，在參數不改變的時候，可以提高model的彈性。若多餘的layer沒有用處，可以學習到把多餘的layer F(x) 參數調低，而調高原先 x 部分的權重。
- 當中的bottleneck block利用了1x1 kernel先將map降維(256->64)，做3x3 conv後再用1x1提升維度(64->256)，如果不先降維，直接像原先的block做兩次256dim的3x3 conv，參數量會多很多：
    - 用256做3x3 conv: 3x3x256x256 * 2 = 11796496
    - 先用1x1降維: 1x1x256x64 + 3x3x64x64 + 1x1x64x256 = 69632
    - 相差16倍的參數量！



### Feature Pyramid Networks (2016)
- **Feature Pyramid Networks for Object Detection (Citation: 16795)**
- 藉由金字塔形狀，不同尺度的feature map，來更好的辨識照片中的小物件。越高層的feature map所包含的semantic information越多，但解析度較粗糙，適合辨識大物件，而越低層的feature map中semantic info較低，但resolution較大，適合拿來辨識小物件。其中利用了Bottom-up (CNN forward), Top-down(upscaling)以及lateral connections來做pyramid feature，其中每層feature都會去predict output，而不是只有最上面或是最下面有而已。
- 在top-down的過程，high-level feature map會做upscaling，與經過1x1的lateral feature map加起來合併。
- **FPN於Fast RCNN應用：** Fast RCNN是用selective search來提出region proposal，再將region在backbone得到的feature map經過ROI pooling得到每個ROI的feature。利用FPN，在backbone的各個階段不同尺度的feature map都可拿來做ROI pooling，paper提出一個公式，ROI區域大小越大，會使用越高層(size較小、semantic info越多)的feature map，而ROI很小的則會使用低層(size較大、semantic較低)的feature map來做ROI pooling。來讓後續classifier, regressor可以更好抓到各種不同大小的物件。
- **FPN於Faster RCNN應用：** Faster RCNN將backbone產生的feature map餵進去RPN(Region Proposal Network)，去做sliding window，在每個pixel設置許多不同比例、尺寸的anchor，並用RPN預測這些anchor為foreground/background的機率和要調整的位置、尺寸。而透過FPN，backbone中每個scale的feature map皆會自己做一個RPN，並最後把每個scale產生的ROI合併起來並選出foreground機率最高的那些作為final ROI。而這裡跟faster不一樣的點在於因為現在已經有了多個scale的feature map，在設置anchor時只要有不同比例形狀的就好，不同scale裡面用的是同個尺寸的anchor。同個尺寸的anchor，例如5x5，在高層、較小的feature map上可能對應到原始照片的512x512，而在低層最大的feature map則對應到32x32。



### MobileNet (2017)
- **MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications (Citation: 17133)**
- 若要將model裝置在mobile, embedded device，模型要小、快。本文提出MobileNet，利用depthwise seperable convolution所構成，在幾乎不影響performance情況下大大降低計算成本及參數量。本文也額外使用width multiplier, resolution multiplier進一步縮減model。
- Depthwise seperable convolution
    - 將標準convolution拆成兩個階段：(1)Depthwise convolution, (2)Pointwise convolution。Depthwise時利用M個DkxDkx1的kernel對每層channel個別做convolution，M個channel彼此訊息互不相通。Pointwise convolution則藉由N個1x1xM的kernel，每個1x1xM對一個pixel的所有channel做weighted sum，也就是NIN，1x1 convolution，讓channel間訊息彼此交換。這種conv方式較節省時間，餐數量也用的較少，accuracy也能維持。
    - 設kernel size Dk, image size DfxDf, channel M, new channel N，則
    - standard convolution所需cost = N * Dk * Dk * M * Df * Df
    - depthwise seperable convolution，(1) Dk * Dk * M * Df * Df, (2) N * M * Df * Df


### RetinaNet (2017)
- **Focal Loss for Dense Object Detection (Citation: 17988)**
- aaa


### EfficientNet (2019)
- **Rethinking Model Scaling for Convolutional Neural Networks (Citation: 10274)**
- 通常的CNN架構，可以透過增加conv layer depth (layer number)、width (channel number), 或是resolution (width x height)來增進accuracy。不過之前的研究都只有從上述選一個來imporve acc。EfficientNet提出在相同計算量下，同步增加這三項會比只增加一項的效果來得好。
- EfficientNet利用一個BaseModel，先用簡單的search找出當計算資源有2倍時，depth, width, resolution最好的scaling constant，接著再利用這個比例，繼續放大model，得到很好的表現。
- EfficientNet base-model當中用了很多的MBConv(MobileConv，應該是這個的縮寫)，又叫inverted residual block，這個MBConv在新版的MobileNet似乎也有被使用。在一般的residual block，channel dimension會先透過1x1縮小，然後做完conv以後再用1x1放大回去原始尺寸，但MBConv卻是在bottleneck中利用depthwise seperable conv去放大channel dimension，等做完depthwise conv後再用pointwise 1x1 conv縮小至原始channel dimension，我目前還沒參透這樣做的用意。
    - ref: https://www.youtube.com/watch?v=TJSCSyoA-EU






## Image Captioning

### Implementation
- https://youtu.be/y2BaTt1fxJU
- 大致流程：利用CNN和RNN，先將image通過CNN做feature extract，得到的feature embedding作為RNN timestep的input，來產生下一個word index，也利用next word作為下一個timestep之input，來產生sequence output。

### Show, Attend and Tell: Neural Image Caption Generation with Visual Attention (2015)
- **Show, Attend and Tell: Neural Image Caption Generation with Visual Attention (Citation: 10149)**
- aaa



## Neural Style Transfer

### A Neural Algorithm of Artistic Style
- **A Neural Algorithm of Artistic Style (Citation: 2550)**
- https://youtu.be/imX4kSKDY7s
- 大致流程：Input一個content image和style image，訂定content loss, style loss來學習content照片中的內容物，以及style照片中的風格。從一個VGG裡面抓出幾個feature map，讓generated image學習內容和風格。Content loss直接比對generated, content兩者之間差距。Style loss則注重feature map中不同channel的correlation，要讓generated image的不同channel去學習style image不同channel的表示。利用兩個loss權重相加作為最後的loss function。



