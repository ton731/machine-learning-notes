# Object Detection & Semantic Segmentation

[![hackmd-github-sync-badge](https://hackmd.io/71vXvwmnQ9aX51Dv4ULQ1g/badge)](https://hackmd.io/71vXvwmnQ9aX51Dv4ULQ1g)


###### tags: `AI/ML`




## Object Detection: YOLO series


### YOLO v1 (2015)
- **You Only Look Once: Unified, Real-Time Object Detection (Citation: 31548)**
- 之前RCNN系列two-stage的object detection，先做bounding box的proposal，再用CNN去predict category，bbox refinement，會很慢。Yolo提出one-stage的regression formulation，直接用一個CNN去預測bbox位置和類別。
- YOLO直接將image劃分成SxS(paper用7x7)個區域，每個區域會predict出B個(paper用2)bbox(x, y, w, h, confidence)和C個(class種類)conditional class probability，接著每個box會將confidence乘上class probability，得到這個box屬於每個class的confidence，最後也會透過non-max suppression把不同grid合併。
- 在決定好SxS後，paper用24個conv和2個fc來設計CNN，讓最後輸出的feature map為 7x7x30，也就是每個grid cell會有30個值，在paper包括：2個bbox * 5個值(x,y,w,h,conf)/每個bbox + 20個class(PASCAL VOC dataset)。
- YOLO v1的limitations:(1)一個grid cell只能有2個bbox和一個class，對small objects appear in groups表現差， (2)很難generalize到新的aspect ratio的object，(3)大box和小box之small error量一樣，但同樣error對小box IOU影響很大，目前無法很好處理。


### YOLO v2 (2016)
- **YOLO9000: Better, Faster, Stronger (Citation: 15067)**
- YOLOv2對v1的方法做了一些改進，讓他better, faster, stronger
- Better: (1)在所有conv後面加上batch normalization，加速收斂並起到regularization效果，(2)在pre-trained classifier用high resolution image: 448x448(原先是224x224)，(3)v1是直接預測bbox的xywh，v2利用anchor，讓model不用憑空產出bbox，而是根據起始bbox做修正就好，並將v1中7x7的feature map變成13x13的grid size，(4)在anchor box shape選擇上，Faster R-CNN是用人工re-defined的大小，而YOLOv2則是對VOC和COCO的bbox做k-means clustering，選出5個anchor box shape，而讓每個grid有5個bbox，(5)為了能更好的預測小物件，將先前26x26的map拆小疊加起來concat到之後的13x13，(6)在訓練時每隔10 epoch就會隨間變換image size，達到multi-scale training，讓input可以在performance, speed間做選擇。
- Faster: 提出Darknet-19架構，把v1最後的fully-connected換掉，用Network in Network裡面的Avgpool來取代。
- Stronger: 用WordTree將ImageNet classification的data也可以幫助object detection訓練。


### YOLO v3 (2018)
- YOLOv3: An Incremental Improvement (Citation: 18107)
- 這是作者Joseph Redmon最後一篇YOLO文了，他在2020說出於道德考慮，決定停止一切有關電腦視覺之研究。
- 作者在這篇並沒有對YOLO整體架構提出改變，只是改良一些原先的方法。
    - Bounding Box Prediction：改成以logistic regression預測每個bounding box的score，但他不會看所有bbox，他計算loss只看跟ground truth overlap最多的那個bbox。
    - Class Prediction: 把原本利用softmax預測每個class的機率的方式，改成每個class獨立的logistic classifier，他讓一個image允許有multi-label，例如一個男人他既是male也是person，如果用之前softmax無法涵蓋這種觀念。
    - Predictions Across Scales：利用 feature pyramid network來涵蓋多個尺度下的feature map，來幫助model預測小物件
    - Feature Extractor: 這裡他對之前的backbone Darknet-19做了改良，利用Resnet中的residual方法加深到Darknet-53。


### YOLO v4 (2020)
- **YOLOv4: Optimal Speed and Accuracy of Object Detection (Citation: 7663)**
- aaa








## Object Detection: RCNN Series

### Selective Search
- 一個based on hierarchical grouping的region proposal產生方法。
- 先藉由image segmentation將image切成很細的一個一個segment，每個segment都可產生各自的tight bounding box。接著在每個iteration中，會把similarity最相近的兩個segment，把他們merge起來，直到沒有segment可以merge。最後會從每個iteration選出一些bounding box作為regional prposal，最後把不同iteration的box都搜集起來，增加proposal的多樣性，實務上總共取約2000個。

### RCNN

- Paper: **Rich feature hierarchies for accurate object detection and semantic segmentation**
- Selective Search
    - Hierarchical Grouping + Diversification Strategies，用4種指標來衡量bounding box之間相似度，並用bottom-up的方式把box給group起來
    - Tutorial: https://medium.com/lifes-a-struggle/%E5%8F%96%E5%BE%97-region-proposals-selective-search-%E5%90%AB%E7%A8%8B%E5%BC%8F%E7%A2%BC-be0aa5767901
    - Tutorial: https://zhuanlan.zhihu.com/p/39927488
    - Tutorial: https://blog.gtwang.org/programming/selective-search-for-object-detection/
    - Hierarchical Grouping 演算法是利用 Graph Based Segementaion 來找出 initial region的
        - Paper: Efficient Graph-Based Image Segmentation
        - Tutorial: https://blog.gtwang.org/programming/opencv-graph-based-segmentation-tutorial/
    - Diversification Strategies 中紋理相似度是利用SIFT-like的方法計算的
        - Paper: Distinctive Image Features from Scale-Invariant Keypoints
        - Tutorial: https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html
- IoU, AP, mAP explaination
    - http://yy-programer.blogspot.com/2020/06/iouapmap.html
    - https://chih-sheng-huang821.medium.com/%E6%B7%B1%E5%BA%A6%E5%AD%B8%E7%BF%92%E7%B3%BB%E5%88%97-%E4%BB%80%E9%BA%BC%E6%98%AFap-map-aaf089920848
- Non-Maximum Suppression (NMS)
    - Explanation: https://chih-sheng-huang821.medium.com/%E6%A9%9F%E5%99%A8-%E6%B7%B1%E5%BA%A6%E5%AD%B8%E7%BF%92-%E7%89%A9%E4%BB%B6%E5%81%B5%E6%B8%AC-non-maximum-suppression-nms-aa70c45adffa
- RCNN from scratch tutorial:
    - pytorch: https://medium.com/codex/implementing-r-cnn-object-detection-on-voc2012-with-pytorch-b05d3c623afe
        - colab: https://colab.research.google.com/drive/1nCj54XryHcoMARS4cSxivn3Ci1I6OtvO?usp=sharing
    - tensorflow (上面pytorch那篇說這篇在取data部分有點問題): https://github.com/Hulkido/RCNN
- Implementation
    - 先domain specific fine-tuning再object category classification
    - fine-tuning用的data是img的region proposal，若IoU < threshold當作positive，其餘當作negative，讓positve:negative保持1:3
    -  object category classification拿img的true label bounding box當作postive，而IoU < 0.3作為negative，也保持1:3來訓練
    -  這邊classier實作上跟paper用的不一樣，paper最後還有一個0/1的category SVM，我們這邊直接NN後面接softmax，所以cnn features後面有兩個分支：(1)classifier+softmax, (2)bounding box regression
    -  classification + regression --> 留下confidence > threshold的RoI --> 對留下的RoI不同category做NMS




### Fast R-CNN

- Paper: **Fast R-CNN**
    - 原本RCNN要將image中2000個region proposal都通過CNN，這樣計算量很大，Fast RCNN改變順序，每張image只要過一次CNN，regional proposal則是用過了CNN的feature map來取
    - Explanation: https://ivan-eng-murmur.medium.com/obeject-detection-s2-fast-rcnn-%E7%B0%A1%E4%BB%8B-40cfe7b5f605
- Spatial Pyramid Pooling (SPP)
    - 將不同尺寸的img做數個不同level的pooling，使得output的feature dimension是相同的，可以讓原本不同尺寸input都餵進去後面的fully connected layer
    - Explanation: https://kknews.cc/zh-tw/code/6gz4k2l.html
- RoI Pooling
    - 對image做max-pooling變成相同的output shape
    - Explanation: https://blog.csdn.net/u011436429/article/details/80279536
    - Explanation: https://blog.csdn.net/weixin_44638957/article/details/97144418
- SPP vs. RoI Pooling
    - RoI Pooling和Spatial Pyramid Pooling的差別在於SPP是由不同level(size)的pooling之後concat形成的，但RoI Pooling就單純只有一種level，可以視為單獨一個level的SPP
    - Explanation: https://blog.csdn.net/weixin_42486139/article/details/111831397
- Fast-RCNN some function example:
    - pytorch: https://github.com/zjZSTU/Fast-R-CNN
    - detectron: https://github.com/facebookresearch/Detectron/blob/main/detectron/modeling/generate_anchors.py
- Imlementation
    - 流程：
        - img --VGG--> img feature map
        - RoI + feature map --RoI pool & FC--> RoI feature vector
        - RoI feature --FC & softmax--> category classification
        - RoI feature --FC--> bounding box regression
    - Data generation
        - 因為還是用selective search，所以如果training time再每個img產生RoI會太慢，所以要先在一開始把每個img裏2000個RoI的rectangle和class，以及若一個RoI為object，也紀錄正確object的rectangle。
        - IoU >= 0.5為postive, 0.1 <= IoU < 0.5的為negative (background)
        - data.pkl格式：[img_data_1, img_data_2, ...]
            - img_data_1: {img, [positive_rois], [negative_rois], [positive_labels], [negative_labels]}
        - 用`__getitem__`和`collate_fn`來做mini-batch sampling
    - Training
        - 在training時，每個mini-batch中，隨機挑選兩個img(N=2)，每張img會sample 64個RoI(positive:negative=16:48)，可以說batch size = 128
        - 原先bbox的x1, x2, y1, y2是定義在img shape上的，要先計算這些coordinate在feature map上面的位置才能做roi pool



## Semantic Segmentation

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




