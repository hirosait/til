# 微分

- 微分は「何」が求まるのか？
	- **「接線の傾き」** が求まる。
	グラフ：y = ax^2  
	接線：y = ax + b   
	a は傾き、bは切片  
	右肩上がりの接線の傾きは正の数値になる。これが微分で求まる。  例：+3  
	ちなみに右肩下がりの接線の傾きは、負の数値になる。例：-2

	予測する際に、実際の家賃と予測家賃の差＝「誤差」を小さくしたい。仮に１万円の誤差より３００円の誤差のほうが良い予測になる。最も誤差の少ない接線の関数を求めたい場合、傾きがX軸と平行な「傾き０」の箇所が最も誤差が少ないところになる。

- 微分は「何」に使えるのか？
	- 「傾き０」を利用することで、ある関数（例：誤差）が最小（もしくは最大）となる点が求まる。
	- 良い予測＝少ない誤差＝傾き０を求めれば良い。

## 微分（導関数）を求める１

2つの点を通る線の傾きを求める
２つの点を通る線の式は、y = ax + bで、 aが傾き、bが切片だった
 **傾き** を求めるには、```f(x)の増加量 / xの増加量``` で求まる。

傾き=<img src="https://latex.codecogs.com/gif.latex?\frac{f(x2)-f(x1)}{x2-x1}" title="\frac{f(x2)-f(x1)}{x2-x1}" />

## 微分（導関数）を求める２

**極限について**  

極限： <img src="https://latex.codecogs.com/gif.latex?\lim&space;_{x\rightarrow&space;0}3x" title="\lim _{x\rightarrow 0}3x" />

x->0 は**条件**、3xは計算の**対象**  
これはxをゼロに近づけるという計算  
しかし機械学習では、単にxにゼロを代入すると考えてもOK  
x = 0なので、対象は3 x 0 = 0  

例題：<img src="https://latex.codecogs.com/gif.latex?\lim&space;_{h\rightarrow&space;0}(2x&plus;h)" title="\lim _{h\rightarrow 0}(2x+h)" />  

答え：2x + 0 = 2x  


問題： 1つの点を通る傾きを求めなさい  

答え：  
<img src="https://latex.codecogs.com/gif.latex?\lim&space;_{h\rightarrow&space;0}\frac{f(x&plus;h)&space;-&space;f(x)}{(x&plus;h)-x}" title="\lim _{h\rightarrow 0}\frac{f(x+h) - f(x)}{(x+h)-x}" />  
<img src="https://latex.codecogs.com/gif.latex?\lim&space;_{h\rightarrow&space;0}\frac{f(x&plus;h)&space;-&space;f(x)}{h}" title="\lim _{h\rightarrow 0}\frac{f(x+h) - f(x)}{h}" />

解説：２点ではなく、１点なので、増加量が取れない場合、仮想の点を作る。  
仮想点の横：x+h, 仮想点の高さ：f(x+h)(hが縦横の増加量)  
つまりこの仮想点を元の点に近づける（増加したhを限りなく0に近づける）ことで、２点を通る線から１点を通る線になる。  

### 導関数のまとめ
微分(導関数)：  
<img src="https://latex.codecogs.com/gif.latex?f'(x)&space;=&space;\lim&space;_{h\rightarrow&space;0}\frac{f(x&plus;h)&space;-&space;f(x)}{h}" title="f'(x) = \lim _{h\rightarrow 0}\frac{f(x+h) - f(x)}{h}" />  
f'(x)の'はダッシュと読む。 **ダッシュは微分を表す**。

---
# 微分の公式
(1) <img src="https://latex.codecogs.com/gif.latex?(1)'=0" title="(1)'=0" />  
(2) <img src="https://latex.codecogs.com/gif.latex?(x)'=1" title="(x)'=1" />  
(3) <img src="https://latex.codecogs.com/gif.latex?(x^2)'=2x" title="(x^2)'=2x" />  

記号:
<img src="https://latex.codecogs.com/gif.latex?()'=\frac{d}{dx}()" title="()'=\frac{d}{dx}()" />  これも同じ意味

例題：  
(3)の式を導出する  

 <img src="https://latex.codecogs.com/gif.latex?(x^2)'=2x" title="(x^2)'=2x" />  

<img src="https://latex.codecogs.com/gif.latex?(x^2)" />を微分すると、本当に2xになるのだろうか  

導関数の公式を使う：  
<img src="https://latex.codecogs.com/gif.latex?f'(x)&space;=&space;\lim&space;_{h\rightarrow&space;0}\frac{f(x&plus;h)&space;-&space;f(x)}{h}" title="f'(x) = \lim _{h\rightarrow 0}\frac{f(x+h) - f(x)}{h}" />  

<img src="https://latex.codecogs.com/gif.latex?f(x)=x^2" />
   
<img src="https://latex.codecogs.com/gif.latex?f(x+h)=(x+h)^2" />   

<img src="https://latex.codecogs.com/gif.latex?=x^2+2xh+h^2" />  

<img src="https://latex.codecogs.com/gif.latex?(x^2)'&space;=&space;\lim&space;_{h\rightarrow&space;0}\frac{(x^2&plus;2xh&plus;h^2)-x^2}{h}" title="(x^2)' = \lim _{h\rightarrow 0}\frac{(x^2+2xh+h^2)-x^2}{h}" />

<img src="https://latex.codecogs.com/gif.latex?=&space;\lim&space;_{h\rightarrow&space;0}\frac{2xh&plus;h^2}{h}" title="= \lim _{h\rightarrow 0}\frac{2xh+h^2}{h}" />

<img src="https://latex.codecogs.com/gif.latex?=&space;\lim&space;_{h\rightarrow&space;0}\(2x&plus;h)&space;=&space;2x&plus;0" title="= \lim _{h\rightarrow 0}\(2x+h) = 2x+0" />

<img src="https://latex.codecogs.com/gif.latex?=2x" />

### 練習
微分の公式に分解して、答えを求める  

(1) (3x^2)' = 3x(x^2)' 関係ないのは外出OK  
            = 3 x 2x = 6x  
(2) (4x + 3)' = (4x)' + (3)'  足し算は微分を分けてもOK  
              = 4 x (x)' + 3 x (1)'  
              = 4 x 1 + 3 x 0  
              + 4  
(3) (3x^2 + 4x + 7)' = 3 x (x^2)' + 4 x (x)' + 7 x (1)'   
                     = 3 x 2x + 4 x 1 + 7 x 0  
                     = 6x + 4 + 0  
                     = 6x + 4  
                     