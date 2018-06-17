## 「適切」を決める

「**評価関数**」を決める。評価関数は**損失関数**とも呼ばれる。  

<img src="https://latex.codecogs.com/gif.latex?y" /> :実際の家賃  
<img src="https://latex.codecogs.com/gif.latex?\widehat&space;y" /> :予測される家賃  

<img src="https://latex.codecogs.com/gif.latex?y" /> と<img src="https://latex.codecogs.com/gif.latex?\widehat&space;y" /> の差が小さいほうが良い  

差を求める:  
<img src="https://latex.codecogs.com/gif.latex?(y-\widehat&space;y)^2" />  

二乗することで、プラスマイナスを考慮しなくて良くなる  

これを「**二乗誤差**」と呼ぶ  

※絶対値ではなく２条にする理由は様々あるが、単回帰では絶対値だとグラフにするとグラフ線がVの字になり、底がなめらかにならず、微分で解を求める際に不都合なので、U字になるよう二乗するほうが都合が良い。  

評価関数:   
<img src="https://latex.codecogs.com/gif.latex?L=(y_1-\widehat&space;y_1)^2&plus;(y_2-\widehat&space;y_2)^2&plus;...&plus;(y_n-y_n^2)^2" />    
<img src="https://latex.codecogs.com/gif.latex?=\sum_{n=1}^{N}(y_n-\widehat&space;y_n)^2" />


n=サンプル数

