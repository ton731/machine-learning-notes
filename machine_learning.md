# ML Notes

[![hackmd-github-sync-badge](https://hackmd.io/n6MEaSDsRHGE7-kRLZXzyw/badge)](https://hackmd.io/n6MEaSDsRHGE7-kRLZXzyw)



###### tags: `AI/ML`


## Algorithms

### K-Nearest Neighbors (KNN)
- 為一種多數表決的supervised learning。唯一的參數$k$代表要選幾個鄰居來做表決。當做classification時，一個data會去計算與其他labeled data的距離，選$k$個最近的，用這$k$個class label去做多數決。
- 在regression問題中，predicted的value即為$k$個data $y$的平均值。
- $k$的大小很關鍵，若$k$太小($k=1,2$)可能會變得noisy並被outlier所影響。而若$k$太大，則有可能會覆蓋掉一些距離很近，但數量很少的correct class。$k$的大小可以用validation set來設定。

### K-means
- 為一unsupervised clustering方法。透過初始化選擇$k$個data point作為center。在每個iteration中，利用data到每個center的距離來將每個data assign class，接著以每個class所有data的平均來重新定位class center，並重新assign class label，這樣持續下去直到class label不再變動。
- $k$數量的選擇可以畫出不同$k$時整體每個class variance加起來的值。$k$越高則variance會越低，可以選擇這個圖中的elbow point(marginal variance開始減小)來選$k$。




## Distributions

### Probability vs. Likelihood
- 以老鼠重量為例子，
- Probability為在給定某個distribution下，某個data出現的機率：pr(mouse weight > 34 gram | mean=32, std=2.5)
- Likelihood為在給定某個data下，某個distribution產生這個data的可能性：L(mean=32, std=2.5 | mouse weight = 34 gram)

### Maximum Likelihood
- Maximum likelihood的目標是在給定已經有一些data (measurement)的情況下，找出最能夠fit這些data的distribution，或者說最有可能產生這些data的distribution。
- 若已經有一個distribution $P$和data $x_1, x_2, ..., x_n$，則$P$產生這些data的likelihood為$P(x_1) \cdot P(x_2) \cdot ... \cdot P(x_n)$。
- 可以對這個likelihood去optimize maximum value來找對最好的distribution。可以用grid search一一去嘗試distribution type, mean, std等，也可以像logistic regression表示成cross entropy後用gradient descent去解。

### Normal Distribution
- $p_{normal}(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
- 中央極限定理 (Central Limit Theorem): 從任意分佈$p(x)$採樣$n$筆，若採樣過程i.i.d.，且分佈$p(x)$的mean為$E_{x \sim p(x)}[x] = \mu$和variance為 $Var_{x \sim p(x)}[x] = \sigma^2$，則當$n$接近無限大時，樣本的分佈會接近$p_{normal}(\mu, (\frac{\sigma}{\sqrt{n}})^2)$。
- 因自然界中我們所觀測到的物理量常常是由許多微小貢獻疊加而成，而不管原本的分佈長怎樣，巨觀物理量因中央極限定理而成為normal distribution，這也是為什麼隨機誤差大都呈現normal distribution的原因。
- Normal distribution很好用的原因還有第二個：在給定mean和variance的分佈中，normaal distribution是隨機性最大的分佈，且是最少先驗知識(prior knowledge)假設的。隨機性最大 (Entropy最高)、且額外假設最少。

### Information Entropy 資訊熵
- 量化訊號中存在資訊量的方式，最初目的是為了傳輸數據的編碼，探討要怎麼將資料編碼使得傳輸有效率。資訊理論背後直覺：越不容易發生的事件帶給我們的資訊量越大，即事件的資訊量$\propto$事件的不確定程度。
- 量化方式：$I(x) = -log_2p(x)$。$log_2$代表單位用bits，$p(x)$為事件出現機率。特性：資訊量必為正、當$p(x)=1$，事件永遠是對的，則$I(x)=0$，資訊量為0、$p(x)$越小$I(x)$越大、若$p(x)=p_1(x) \times p_2(x)$，兩事件為獨立事件，則$I(x)=I_1(x) \times I_2(x)$。
- 這種self-information只處理單一一個結果，若我們相關住整個系統，Shannon Entropy可以量化整個機率分佈中不確定性的程度：$H(x)=E_{x \sim p}[I(x)] = -E_{x \sim p}[log_2p(x)]$。上述的Shannon Entropy即為self-information的期望值。而若假設系統為離散的，則$H(x) = -\sum_i p_i log_2 p_i$。
- 在ML中常把$log_2$換成自然常數$e$，得Entropy $H(p) = E_{x \sim p}[-\operatorname{ln} p(x)]$，其實就只是把度量單位從bits換成nats，方便計算。
- Uniform distribution可以使得entropy最大，代表uniform distribution是隨機性最大的分佈，也是資訊量最大的分佈。（在有給定variance下normal distribution才是有最大entropy）
- 小結：Entropy中$-log$扮演編碼的角色，決定需要用幾個bits來傳輸事件，而entropy意義是這套編碼運用到系統的bits期望值。Shannon理論說$-logp(x)$已經是最有效率的編碼，所以Entropy是bits期望值的下界。

### Cross Entropy
- 在classification問題中，cross entropy被定義為$-y \operatorname{ln}(q) - (1-y) \operatorname{ln}(1-q)$，可以從maximum likelihood來推導。但其實有更一般的定義: $Cross Entropy: H(p,q) = E_{x \sim p} [-\operatorname{ln}q(x)]$，其中$p(x)$為目標分佈，想要學習的未知分佈，而$q(x)$為model的輸出分佈。
- 當我們試圖減少cross entropy，其實就是試圖調整$q(x)$使其更接近$p(x)$，因為當$q(x)=p(x)$時，$H(p,q)=H(p,p)=H(p)$有最小的cross entropy。延續編碼的概念，雖然知道$-\operatorname{ln}p(x)$是最好的編碼，但因為我們不知道實際的$p(x)$，所以退一步用model的$q(x)$來做編碼，而cross entropy則代表用$q(x)$編碼所得到的系統的nats期望值，並目標是想辦法降低cross entropy。
- 當目標是binary的離散系統，
    - $H(p,q) = -p_{positive} \cdot \operatorname{ln}(q_{positive}) - p_{negative} \cdot \operatorname{ln}(q_{negative})$，而因$q_{positive}+q_{negative}=1$，可寫成
    - $H(p,q) = -p_{positive} \cdot \operatorname{ln}(q_{positive}) - (1 - p_{positive}) \cdot \operatorname{ln}(1 - q_{positive})$，而當label為1，則$p_{positive}=1$，反之亦然，故可寫成：
    - $H(p,q) = -y \cdot \operatorname{ln}(q) - (1-y) \cdot \operatorname{ln}(1-q)$
- Cross Entropy不需要假設model用sigmoid、模型長相。Cross Entropy可以用在各種問題、分佈，包括regression問題。

### KL Divergence (Kullback-Leibler Divergence)
- 若今天從$p(x)$抽出一個$x$，而同時有另一個獨立的分佈$q(x)$也對應到這個$x$，則KL Divergence可以用來衡量這兩個distribution的差異：$D_{KL}(p||q) = -E_{x \sim p}[\operatorname{ln}q(x) - \operatorname{ln}p(x)] = -E_{x \sim p}[\operatorname{ln}\frac{q(x)}{p(x)}]$
- 可以改寫成：$D_{KL}(p||q) = -E_{x \sim p}[\operatorname{ln}q(x)] -E_{x \sim p}[\operatorname{ln}p(x)] = H(p,q) - H(p)$。其實KL Divergence就是cross entropy扣掉目標分佈的entropy，更深層看，KL divergence表示了目前的編碼方法最多還可以下降多少nats期望值。
- KL Divergence嚴格來說不是distance，因為不具有對稱性：$D_{KL}(p||q) \not= D_{KL}(q||p)$





## Metrics

### ROC, AUC
- ROC (Receiver operator characteristic)定義為在各種decision threshold設定下，True Positive Rate (真陽率，真正是1的有多少個1倍預測出來)與False Positive Rate（假陽率，真正是0的有幾個被預測成1）之間的變化。若用logistic regression，則用不同的threshold來classify可以得到ROC上面不同的點，最後可以連成一條線。越左上角的點越好。基本上一定要在$y=x$這直線的左上方，不然在他右下方基本上就比猴子猜的還爛。
- AUC (area under curve)為ROC curve下方的面積，越大越好。ROC裡面不同的點代表同一個model下，不同決策threshold間的tradeoff。而不同的AUC則代表不同model間的好壞，如$AUC_{random forest}$ vs. $AUC_{logistic regressor}$。

### mAP (Average Precision)
- 對於每個預測的target class，假設現在已經有model的bounding box & class & confidence prediction了，我們可以設定一個IoU threshold來篩選掉不好的prediction，接著我們可以用confidence的高低來排序每個prediction。在排序好之後，主要關注累積的precision和recall。當計算confidence第$k$名時，recall因為只考慮$1$~$k$總共答對幾個正確的case，所以累積起來會是一直增加的。而precision則是考慮前$k$的case的預測裡面有幾個是正確的，所以累積起來會有高有低。最後將recall(x) vs. precision (y)的圖畫出來，zigzag曲線就是average precision (AP)。
- AP@.50代表IoU threshold設定為0.5下的AP，AP@.75則代表threshold設在0.75，會比AP@.50更嚴苛。





### Batch Normalization

### Layer Normalization

### KL Divergence

### Convex






### 數學運算
- $H = -1 \operatorname{log_2}1=0$
- $H = -\frac{1}{2}\operatorname{log_2}\frac{1}{2} -\frac{1}{2}\operatorname{log_2}\frac{1}{2} = 1$
- $H = -\frac{1}{4}\operatorname{log_2}\frac{1}{4} -\frac{1}{4}\operatorname{log_2}\frac{1}{4} -\frac{1}{4}\operatorname{log_2}\frac{1}{4} -\frac{1}{4}\operatorname{log_2}\frac{1}{4} = 2$
- $\operatorname{log_2}p(x) \rightarrow \operatorname{ln}p(x)$
- $p(x)$, $q(x)$
- $H(p, p)$
- $H(p,p)=-0.35\operatorname{log_2}0.35 -0.40\operatorname{log_2}0.40 -0.05\operatorname{log_2}0.05 -0.20\operatorname{log_2}0.20=1.739$
- $H(p,q)=-0.35\operatorname{log_2}0.32 -0.40\operatorname{log_2}0.38 -0.05\operatorname{log_2}0.14 -0.20\operatorname{log_2}0.16=1.804$
