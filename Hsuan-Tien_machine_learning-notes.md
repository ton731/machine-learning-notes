# 軒田機器學習筆記


###### tags: `AI/ML`



## Machine Learning - Hsuan-Tien Lin

### Lecture 1: Basics of Machine Learning
- **PLA (Perceptron Learning Algorithm)**
    - **How:** 假設linear seperable, 任意d-dim都可，初始一$W$, 隨機抽一個error的點，用來更新$W$, $W = W + y_n x_n$，不斷迭代後$W$就會成功seperate class
    - **Why:** 有數學證明，當用錯誤的($x_n$, $y_n$)來更新$W$時，$W$會離正確解$W_f$越來越近，需要迭代的數量也可證明是被bounded

### Lecture 3: Feasibilty of Learning (When Can Machine sLearn?)
- 根據Hoeffding's Inequality，當取樣時根據$i.i.d.$ (Independent and identically distributed)取樣且，數量$N$或容許誤差$\epsilon$夠大時，從罐子取出的sample distribution ($v$, $E_{in}$)會和罐子中真實的distribution ($\mu$, $E_{out}$)很接近，probably approximately correct (PAC)
- 現在可知當data $N$夠大，$E_{in} \approx E_{out}$。若給定一個hypothesis $h$，learning不一定會成功，因為大部分的$h$，$E_{in}(h)$都不小，因此會需要有很多$h$來讓algorithm $A$來挑選$h$，每個$h$代表一個對bin裡面顏色分佈的猜測
- 在只有一個$h$時，data為 $BAD Data$ ($E_{in}$和$E_{out}$很遠)的機率很小，被hoeffding bound住。但若今天有很多$h$，對原本$h$沒問題的data，可能對其他$h$是$BAD Data$，導致這個data $D$是不好的，則可藉由union Hoeffging計算$Bad Data$的機率。Union後機率除了被原先的$\epsilon$和$N$控制外，多了一項$M$，為hypothesis的數量。若$M$為finite，則$E_{in} \approx E_{out}$
- 學習最主要的兩個目標：
    1. $E_{out}(g) \approx E_{in}(g)$
    2. $E_{in}(g) \approx 0$

### Lecture 4: Theory of Generalization (Why Can Machines Learn?)
- 在上一節，若想要讓$A$可以在很多$h$裡面挑最好的，且考慮到$Data$可能對不同$h$來說是不好的$D$，則需要將所有$h$的hoeffding機率union起來。因此在考慮很多$h$，$E_{in}$與$E_{out}$很接近的機率在hoeffding inequality會多出$M$這項，也就是hypothesis的數量$|H|$。若$h$連續，則$|H|$可能為無限大，造成$E_{in}(h) - E_{out}(h)$的大小無法被bound住，因此這章想證明其實大部分的$h$都是重疊的，可分為好幾個group，而重疊的那些就不用去重複算$Bad Data$機率，使得$M$可以從$\infty$往下壓到一個finite polynominal的值，使得machine可以學習。
- Effective number of lines, 或稱(應該是一樣的)growth function, $m_H(N)$，為當有$N$個data point且做binary classification時，可以產生最多多少直線來用直線將這些points分類，$m_H(1)=2, m_H(2)=4, m_H(3)=8, m_H(4)=14$，最大被bounded在$2^N$，m_H(N)若為polynomial是好的，exponential就不太好。
- VC dimension $d_{vc}$為最大出現可shatter的data數量。PLA雖然$|H|$為$\infty$，但是因為2d在平面上$d_{vc}=3$，$|H|$被bound住，使得PLA learning可行。
- Model complexity ($d_{vc}$)會反應在hoeffding的probability當中，$d_{vc}$越大，$E_{in}, E_{out}$差很多的機率就越大。雖然$d_{vc}$越大in sample error會越小，但由於model complexity的代價，使得out sample error會變大，因此要小心選擇$d_{vc}$，在trainditional ML model裡面complexity越高容易overfitting(我自己的結論，DL裡面好像model複雜度沒有對overfitting影響那麼大?待驗證)

### Lecture 5: Linear Models (How Can Machines Learn)
- **Linear Regression**
    - **How:** 用MSE作為loss, 可得gradient的公式解，並找出gradient=0(最佳解)時的weight，有close form solution, $W = X^{\dagger}Y$
    - **Why:** 有close form solution
- **Logistic Regression**
    - **How:** 用maximum likelihood作為$h$的loss function，推導後成為cross entropy loss ($min \frac{1}{N} \sum_{n=1}^{N} -ln \theta (y_n w^T x_n)$)，然後因為微分後較難直接算closed form solution使得gradient=0，故利用gradient descent來optimize
    - **Why:** 現在有real data的(x, y) pair，而在已知觀測結果，likelihood衡量了某個模型參數($h$)產生這個觀測結果的可能性。為了要讓猜測的$h$與真實產生data的$f$越像，我們要找出所有$h$裡面，產生這組data可能性最大的那個$h$，因此以maximum likelihood作為目標 (ref: https://medium.com/qiubingcheng/%E6%9C%80%E5%A4%A7%E6%A6%82%E4%BC%BC%E4%BC%B0%E8%A8%88-maximum-likelihood-estimation-mle-78a281d5f1d)

### Lecture 6: Beyond Basic Linear Models (How Can Machines Learn?)
- **Multiclass classification**
    - One-Versus-All (OVA): 每個class和其餘的class去做logistic classification，最後選機率最大的那個class。這樣有效率，但容易造成training unbalance。
    - One-versus-one (OVO): 每個class對每個class去做binary classification，之後藉由voting來做預測。這樣結果較穩定，但當class number數量變多，要多花時間、空間。
- **Nonlinear transform**
    - 當data在原始空間並不是linear seperable時，可以用nonlinear transform將資料轉到更高維變成在高維中linear seperable的，就可以用linear model來做了
    - 但用越高維度的nonlinear transform不僅增加計算、空間成本，也會造成generalization issue

### Lecture 7: Combatting Overfitting (How Can Machines Learn Better?)
- Noise會使得model overfitting，而noise又可分為兩種：
    - Stochastic noise: 在每個data i.i.d.加入的如guassian noise
    - Deterministic noise: 因問題的複雜度所造成很像noise的影響，當問題很複雜而model很簡單，$f \not\in H$，$f$有些部分是$H$所capture不到的
- 處理overfitting的方法：
    - Data cleaning / pruning：去更正錯誤的label / 丟掉極端example
    - Data augmentation
        - Note: virtual example 不是 iid sample的
    - Regularization：例如讓model保有在$H_{10}$的flexibility，但又儘量model不要太複雜($H_2$)
- **Weight decay regularization**
    - 不希望model太複雜導致overfitting $\rightarrow$ 在optimize$E_{in}$時對weight的大小加上constraint
    - 有constraint的optimzation不好解，用Lagrange Multiplier，得到grad($E_{in}(W_{reg}))$與$W_{reg}$的關係，並可以得到linear regression with constraint的closed-form solution，在統計又叫ridge regression。
    - 將closed form solution還原回去，可以得到另一個等價的optimzation problem，將$\frac{\lambda}{N}w^Tw$作為augmented error加在原本的 min $E_{in}(w)$。
    - 雖然這邊是linear regression當例子，但weight decay regularization可以work with and transform + linear model。
- **L1, L2 regularizer**
    - L2 regularizer: 上面的example，將$||W||_2^2$加在original target function。convex, differentiable everywhere, easy to optimize。通常結果為每個$w$都不會太大。
    - L1 regularizer: 將$||W||_1$加在target function。convex, not differentiable everywhere。通常結果比較sparse，少數$w$有值而其餘為0。若在edge computing對storage, computation有要求，L1 is useful。

### Lecture 8: Combatting Overfitting 2 (How Can Machines Learn Better?)
- 選model時，選$E_{in}$最小的會有overfitting問題，而選$E_{test}$也不切實際，因為看不到實際test data，因此折衷切一塊validation set。用train set訓練model, validation set選好model以後，再拿全部data用這選好的model再train一次。
- Validation set 大小 $K$ 要選多大是個兩難，若$K$很小，則$E_{out}(g) \approx E_{out}(g^-)$，model訓練得較好，但因為$K$小，導致$E_{val}(g^-) \not\approx E_{out}(g^-)$。而若$K$大，雖然$E_{val}(g^-) \approx E_{out}(g^-)$，但$E_{out}(g) \not\approx E_{out}(g^-)$，data少model training效果不好。
- **Leave-One-Out Cross Validation:** $K=1$，每個data都當一次validation並用其餘作為training，$E_{loocv} = \frac{1}{N}\sum_{n=1}^{N}E_{val}^n$，這樣好處是因為training data size夠大，model夠好，而平均下來$E_{val}(g^-) \approx E_{out}(g^-)$。但缺點是計算成本、空間大。
- **V-Fold Cross Validation:** 選$V=5, 10$，做cross validation，使得$E_{cv} = \frac{1}{V}\sum_{v=1}^{V}E_{val}^v$，為single validation & LOOCV的折衷方法。

### Lecture 9: Wisdom of Using Machine Learning (How Can Machines Learn Better?)
- **Occam's Razor:** The simplest model that fits the data is also the most plausible.簡單的model越不容易去fit data和noises，但一旦fit，就真的是找到data的trend。
- **Sampling Bias:** If the data is sampled in a biased way, learning will produce a similarly biased outcome.
- **Data Snooping:** If a dataset has affected any step in the learning process, its ability to assess the outcome has been compromised.

### Lecture 10: Support Vector Machine 1 (Embedding Numerouos Features: Kernel Models)
- 藉由最大化classification時line的margin，來讓model更robust to noises。在$E_{in}=0$時去增加margin(min $w^Tw$)，可以達到類似regularization的效果，better generalization。
- Hard-margin SVM要解maximiazation問題，最大化margin，同時subject to $E_{in}=0$，可以寫成$y_n(w^T x_n + b) \geq 1$。可以透過quadratic programming的solver解這個線性規劃問題。
- 當若使用nonlinear transformation或是feature dimension很高時，不好解，因此把問題轉成dual form。這些數學我忘掉一大半，但大概是用先用Lagrange把constraint加進target function, 在用KKT作轉換、化簡，最後是可以把$w$中$d+1$個variable的dependencies轉到$N$個。
- 兩個方式對比：
    - 原本的primal hard-margin SVM：直接去解$w, b$，找到一條好的線
    - 轉換後的dual hard-margin SVM：去找落在margin上的那些support vectors以及他們的lagrange multipliers。

### Lecture 11: Support Vector Machine (2)
- Kernel Trick: 想要移除之前SVM對feature dimension $d$的depenency。這邊我讀了但是都忘掉了有點讀不懂，有機會再回來看。
- **Soft-Margin SVM**
    - Hard-SVM缺點：若堅持要sepearble，可能導致對noise overfitting。
    - 解決方法：Give up 那些noisy example，將錯誤的sample違反的margin量當作penalty加在target function。使得變成 min $\frac{1}{2}w^Tw + C \cdot\sum_{n=1}^{N}[y_n \not=sign(w^Tz_n+b)]$，並被constrain在$y_n(w^Tz_n+b)≥1-\infty \cdot [y_n \not= sign(w^T z_n+b)$
    - $C$這個parameter控制了large margin & margni violation的trade-off
        - large $C$: 想要更少的margin violation，希望data勁量不要預測錯。
        - small $C$: 可以錯一些data，希望能用這些錯誤data換取一個更大的margin。
    - 剩下就和前面Hard-margin一樣換成dual problem來解。


### Lecture 12: Bagging and Boosting (Combining Predictive Features: Aggregation Models)
- Aggregation的效果看起來像是feature transform & regularization，能讓performance更好。理論上，當base model acc ≥ 0.5，aggregate起來至少會比原本好。Linear model像是PLA，在aggregate之後可以變成nonlinear的樣子。
- **Boostrap Aggregation (Bagging)**
    - Bootstrap: 每次從size $N$ dataset sample $N$個data出來，可以有重複和沒選到的data，用新的dataset來train base classifier，增加diversity。
    - Aggregation: 把不同的base classifier做voting(uniform或是depend on accuracy應該都可)。
- **Adaptive Boosting (AdaBoost)**
    - 核心概念：引導model每次去把上一步發生的error改正。
    - Bootstrap每次用到不一樣的data，其實就等於對data做re-weighting，被選到多錯weight就高，沒辦選到的在loss function的weight就等於0。Adaboost每個iteration把上一步錯誤的data weight調高，而上一步正確的weight降低，這樣相當於在做bootstrap，增加model diversity，讓每次的model都不一樣。
    - Adaboost在調整data weight時用到scaling factor，是根據目前error rate算出來的。error data乘上後weight變大，correct data除以後weight變小。前提是base classifier accuracy ≥ 50%。
    - 每個base classifier透過decision stump來選擇要怎麼將data切成兩半。Decision stump去一一找要用哪個feature, threshold用多少，哪個方向是positive, negative。
    - 最後依照權重把每個base classifier aggregate起來。權重可以用classifier的error rate來算，越準的權重越高。

### Lecture 13: Decision Tree Ensembles (Combineing Predictive Features: Aggregation Models)
- **Decision Tree**
    - 若termination criteria，回傳目前的tree(classifier/regressor)，不然去學branching criteria，學習將目前的data很好的分成兩半，接著每一半再繼續做decision tree。
    - Branching可以看作purifying，讓data變得更乾淨。藉由找decision stump，降低impurity。Classification可用Gini index，regression可用當前data $y$的平均 $\bar{y}$與每個$y_n$的差距來算regression error。
    - 若每個$x_n$都不一樣，decision tree可以讓$E_{in}=0$，但會overfitting，因此可以用number of leaves來作為regularization，又稱pruned decision tree。
    - 簡單、有效率、人類好解讀，但缺乏理論解釋。
- **Random Forrest**
    - Bagging (reduce variance) + Decision Tree (large variance)。
    - 裡面的每個decision tree會藉由隨機選feature來訓練以增加diversity。
    - 繼承了decision tree的優點，能夠平行化、有效率計算，並減緩fully-grown tree overfit的問題。
- Out-Of-Bag Estimate
    - 用Bagging在每次隨機抽data時，會有約$1/e$的data都不會被抽中。可以用這些out-of-bag sample來做self-validation。
    - 對於每個data，去計算每個在訓練時沒有選到這個data的model對他的validation error，加起來可以得到這個bagging model的validation error。
- Optimization View of Adaboost
    - 可以把Adaboost用optimization角度來看。當現在已經run了$t-1$ round，有$t-1$個base classifier了，新的$h(x_n)$要minimize的東西是$\sum_{n=1}^{N}u_n^{(t)}(-y_nh(x_n))$。上一輪犯錯的data $u_n$就會變大，因此可以說成是Adaboost迭代的去correct先前所犯的錯。
- **Gradient Boosting**
    - 按照上面Adaboost的概念，可以將error function延伸至任意的function。若以squared error為例，最後新的base classifier要optimize的target為：min $\sum_{n=1}^{N}2h(x_n)(s_n-y_n)$，其中$s_n$是先前的base classifier們aggregate的結果。也就是說新的base classifier要去彌補前面那些人所留下來的錯誤。
    - 簡單來說gradient boosting是一種aggregate許多weak classifier的方式。從一開始只有一個base classifier，每次增加一個base classifier來讓weak classifier在aggregate後結果更好。而每一個新的base classifier要optimize的目標就是先前aggregation後做不好的地方。
    - 在optimize新的base classifier後，就可以把新的classifier加到之前aggregated classifier上面。因此新的classifier角色就很像gradient，來更新aggregated classifier，並讓他變得更好，因此叫boosting。
- **Gradient Boosted Decision Tree**
    - 用decision tree作為base classifier。
    - 透過序列方式生成tree，每一棵tree要去改善上一個tree的缺點。
    - (Random Forest是用bagging來aggregarte decision tree，可以平行計算，每棵樹tree跟其他不相干。而Gradient Boosted Decision Tree則是用boosting來aggregate decision tree，每棵tree會和前一棵tree有關。)
- **eXtreme Gradient Boosintg (XGBoost)**
    - 結合Bagging和Boosting，保有GBDT的boosting方法，但又在生成每棵樹的時候去random sample feature來達到bagging。
    - 他也在loss function中加入L1, L2 normalization term。

### Lecture 15: Machine Learning Soundings (Distilling Implicit Features: Extraction Models)
- Deep Learning Weight Initializations
    - 若都設成0則對tanh太對稱(tanh在0幾乎是線性)，而對ReLU來說也不可微分。若設成固定constant，則每個neuron就會變成一樣。若設太大，對tanh會造成saturation or gradient vanishing，且若有很多負且大的weight，會讓relu dying，因為relu後變成0的話，weight就無法被更新了。
    - 理論上，在使用tanh且weight不大時，將weight設定成$var(w) = 1/d^{(l-1)}$，可以讓$var(x_j^{(l)}) \approx var(x_i^{(l-1)})$。
    - **Xavier initialization (Glorot)**: 在用tanh時除了forward時讓每層的$x$ variance接近，也可以讓backprop時grad接近。設定$var(w) = 1/d^{(l)}$可以讓$\delta^{(l-1)} \approx \delta^{(l)}$。結合這兩項，可以將weight設定成：$var(w) = \frac{2}{d^{(l-1)}+d^{(l)}}$。
    - **He initialization**: 當使用ReLU時，可以設定weight $var(w) = 2/d^{(l-1)}$使得$var(s^{(l)}) \approx var(s^{(l-1)}$。
- Deep Learning Optimization
    - 先前SGD很好逃脫saddle points & local maxima，但gradient不stable，且通常在平台時需要更大的learning rate，在峽谷時需要較小的learning rate。
    - 如何讓SGD的gradient更stable? 可以用averaging。
    - **SGD with Momentum**: Reuse先前的grads來做moving window/average。$\beta$ * moving average + $(1-\beta)$ * 新的grad。這樣可以remove一些SG造成的variance，並減緩在峽谷時震盪的狀況。
    - **RMSProp**: SGD + per-component learning rate using running average of magnitude。目標是想要讓當grad很大時，learning rate的step可以小一點，而grad很小時，step可以大一點。有一項$u_t$在用類似moving average的方式根據目前grad大小來動態調整learning rate的step value。
    - **Adam (Adaptive Moment Estimation)**: Adam $\approx$ momentum + RMSProp + global decay。Adam除了有有momentum來穩定住grad value，也用RMSProp動態調整learning rate step，也用global decay來隨著timestep慢慢降低learning rate。
- Deel Learning Regularization
    - **Dropout**: Implicit aggregation of many thinner networks。會降低收斂速度，但每個iteration會更快。





