## 評価関数を「最小化」する

誤差が小さいのが一番良い予測である　

### 微分する

評価関数：L  
<img src="https://latex.codecogs.com/gif.latex?y=ax&plus;b" title="y=ax+b" />  家賃を予測する式.


横軸はなにか？  
何かをうまく調整できないと、誤差が大きくなってしまう。何をうまく調整すると誤差が小さくなる。何かとはなにか？  
家賃を求める予測値<img src="https://latex.codecogs.com/gif.latex?\widehat&space;y=ax" />  
なにかとは、aかxのどちらか。  
xは部屋の広さというデータなので、調整できない。調整できるものがパラメータなので、aをパラメータとして使う。  

微分で、誤差が最小となる「傾向きが０」を求める  
「傾き＝０」が求まるaを求める  

微分すると、傾き＝０が求まる  
傾きは微分すると出せる  
<img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;[]}[]" />  []に何をいれるか？何を何で微分するのか？  
右の[]には縦軸(評価関数)を入れる。分母の[]には横軸(a)を入れる。  
つまりこの例だと<img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;a}(L)=0"/>  を求める。  
<img src="https://latex.codecogs.com/gif.latex?L=\sum_{n=1}^{N}(y_n-\widehat&space;y_n)^2" />　①これで解くがaがないので、式変形を行う  
<img src="https://latex.codecogs.com/gif.latex?\widehat&space;y_n=ax_n" />  ②  
①に②を代入  
<img src="https://latex.codecogs.com/gif.latex?L=\sum_{n=1}^{N}(y_n-ax_n)^2" />　  
<img src="https://latex.codecogs.com/gif.latex?=\sum_{n=1}^{N}(y_n^2-2y_nax_n+a^2x_n^2)" />　  
<img src="https://latex.codecogs.com/gif.latex?=\sum_{n=1}^{N}(y_n^2-2(\sum_{n=1}^{N}x_ny_n)a+(\sum_{n=1}^{N}x_n^2)a^2)" />　  
aで微分したいが、aには関係ないところは別の記号にしてしまう. <img src="https://latex.codecogs.com/gif.latex?C_o,C_1,C_2" />と略す。  
<img src="https://latex.codecogs.com/gif.latex?=C_o-2C_1a+C_2a^2" />　 これが最終的な評価関数  
<img src="https://latex.codecogs.com/gif.latex?=>\frac{\partial&space;}{\partial&space;a}(L)=0" />   
<img src="https://latex.codecogs.com/gif.latex?=>\frac{\partial&space;}{\partial&space;a}(C_o-2C_1a+C_2a^2)=0" />  足し算は分離してもOKなので  
<img src="https://latex.codecogs.com/gif.latex?=>\frac{\partial&space;}{\partial&space;a}(C_o)-\frac{\partial&space;}{\partial&space;a}(2C_1a)+\frac{\partial&space;}{\partial&space;a}(C_2a^2)=0" />     
<img src="https://latex.codecogs.com/gif.latex?=>-2C_1+2C_2a=0" />  
<img src="https://latex.codecogs.com/gif.latex?=>C_2a=c_1" />  
<img src="https://latex.codecogs.com/gif.latex?=>a=\frac{c_2}{c_1}=\frac{\sum_{n=1}^{N}x_ny_n}{\sum_{n=1}^{N}x_n^2}" />  
これで最低なパラメータaを求められる  
xの値とyの値  

| x  | y  |
|----|----|
|1   |2   |
|2   |3.9 |
|3   |6.1 |

一旦、センタリングしてから、aを求める。  
a = 1.325 ??
