# 単回帰分析

### 問題設定

**例：家賃の予測**   

y:出力変数   出力y  
x:入力変数  予想するためのファクターx (広さ、距離など）  
単回帰分析ではファクターは１つ。複数の場合は重回帰分析

### 1 学習
広さに対して、家賃がこのくらいという結果を入力していく  

例：広さ20のときは、家賃5, 広さ30のときは、家賃7など、x=40, y=9・・・  
事前にこういう部屋の広さのときは、こういう家賃というのを例えば10万件など入力して、モデルを学習させていく  
### 2 推論
学習済みのモデルはその規則性をわかっているので、新しい部屋の広さ、例えば25の場合は、家賃は6と推論してくれる。  
注意点は内挿しか予想できないこと。例えば部屋10のときは外挿なので、入力データに10以下を入れておいてあげると、内挿になる。  

**大事なのは学習。ここの関係性をどうやって見るけるかが大事。推論はPCが勝手にやってくれる。**

#### 家賃予測

1. 「モデル」を決める
家賃と広さの関係は直線的なグラフで表される場合、 まず人間が家賃と広さは<img src="https://latex.codecogs.com/gif.latex?y=ax&plus;b" title="y=ax+b" />ような直線で関係で表せるだろうと決めてしまう。  
yの上に^（ハット）をつける(ワイハットと読む)と予測値であることを表す。  
<img src="https://latex.codecogs.com/gif.latex?\hat{y}=ax&plus;b" title="\hat{y}=ax+b" />

どんな傾きなのか=a, 切片はどこか？=b　　  
このaとbを人間が設定しておいてあげないといけない。  
yとxはすでにわかっているデータからの値( 家賃と広さ)  
つまり予測できる直線をひくのがゴールなので、aとbを決めるのがゴールになる  
この設定しておいてあげないといけない値(a, b)をパラメータと呼ぶ. 

ゴール  
データ（x1, x2,..y1, y2..)に基づいて「適切」にパラメータaとbを決定する。  
「適切」はコンピュータにとってむずかしい→次のステップ。

データの中心化  (センタリング）   
データをグラフの原点あたりにもってくる。データを真ん中に寄せる。  
何が嬉しいのか？　　
<img src="https://latex.codecogs.com/gif.latex?\hat{y}=ax&plus;b" title="\hat{y}=ax+b" />
データの中心化することで、切片bがなくなる。つまりaとbを求める必要があったものを、データの中心化することでbをなくすことができ、計算を簡略化できる。
データの中心(<img src="https://latex.codecogs.com/gif.latex?\overline{x}" />)を求めるには、データ全体の平均を求め、データの中心を原点に移動させる.

<img src="https://latex.codecogs.com/gif.latex?\overline{x}" />はxの平均  
<img src="https://latex.codecogs.com/gif.latex?\overline{y}" />はyの平均    

<br />

センタリング  

<img src="https://latex.codecogs.com/gif.latex?x_c=x-\overline{x}" />

<img src="https://latex.codecogs.com/gif.latex?y_c=y-\overline{y}" />
<br />
<br />
センタリングの計算   

|<img src="https://latex.codecogs.com/gif.latex?x" /> | <img src="https://latex.codecogs.com/gif.latex?\overline{x}" /> | <img src="https://latex.codecogs.com/gif.latex?x_c" /> |
|----|----|----|
| 1       | 3        | -2         |
| 3       | 3        | 0         |
| 5     | 3      | 2       |


（前提）データは中心化済みであれば、  
<img src="https://latex.codecogs.com/gif.latex?\widehat{y}=ax" />となり、切片bを省略できる。   
ちなみにaはパラメータ、cは記載省略することが多い
