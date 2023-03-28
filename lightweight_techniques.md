# Lightweight Techniques


###### tags: `AI/ML`


近幾年，模型越來越大，但 edge、endpoint 裝置越來越小，資源有限，怎麼把大的model塞進去是重要的議題。以下主要注重在 CNN-based model。


### Overview

- 現今的network大多都overparameterized。很多network其實只要5%的參數就可以預測出剩下的95%。但其實如果直接用小網路來訓練，通常會因為capacity不夠導致訓練不起來，因此還是得從大模型開始訓練。也因此後續的ligitweight就很重要。
- Occam's razor: Better generalization with lower complexity
- Over-paramterized models are easier to train! (**Gradient Descent Provably Optimizes Over-parameterized Neural Networks**):當參數只有一個，gradient descent很容易卡在local minimum，而參數有兩個、或更多時，model更容易可以找到路徑達到global minimum。


## Compressing and optimizing models

### Down-sizing models: Pruning
- **Weight/Connectivity Pruning:** weight pruning拔掉neuron，而connectivity拔掉neuron間的連接。
- 實務上是最簡單也最有效，可以在performance掉不多的情況下把size降低10-20倍。
- 但缺點是假設今天想要減小到原先的100倍，一直拔掉會讓performance不好。

### Down-sizing models: Knowledge Distillation / Neural Architecture Seacrh (NAS)
- 設計一個新的、目標大小的小model，直接學習原本的大model。

### Operator Factorization
- 將原先的矩陣運算做decomposition，讓參數量減小，但運算基本上是等價的。

### Value Quantization
- 將weight/activations轉換成low precision value representation，例如FP32 $\rightarrow$ INT8。

### Value Compression
- Compress values，像是 entropy-based (e.g., Huffman)或是correlated-based (e.g., gzip)。

### Parameter Sharing
- 讓model裡面有些layer長得一樣，就可以在layer-wise share這些parameter (e.g., ShapeShifter networks or CNNs)。

### Sparsification
- 去找NN的sparsity，來讓model縮下來，方法、技巧可以很多元。
- Model Sparsity (per model)：拿掉model裡面的一些weights/neurons/filters/channels/heads。
- Ephermeal Sparsity (per example)：model裡面設計一些選項，根據不同的input來選擇裡面要用哪個小model。


## Other Strategies

### Network Augmentation for Tiny Deep Learning (2021)
- 他們發現data augmentation對大模型overfitting有效，但對小模型會傷害他的表現，導致underfitting。
- 因此對於小模型，他們去做 network augmentation，在原有網路下多加了一些augmented layer，作為輔助，讓model變大，使得原本的小model表現更好。

### FasterNet: Fast Neural Networks (2023)
- 減少NN在計算上的複雜度 (FLOPs, floating-point operations)
- 過往Depthwise convolution/group convolution雖然減少FLOPs，但卻增加了memory access的次數，還有其他additional data manipulatations，像是concat, pooling等。
- 他發現同一個feature map裡面很多內容是重複、redundant的，因此他FasterNet只對一部份的channel做convolution (Partial Convolution)，其他部分就直接copy到下一層。



