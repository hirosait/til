# 偏微分

偏微分とは多変数の微分のこと。つまりxの数が増えていく。  
例： <img src="https://latex.codecogs.com/gif.latex?y" />   が家賃、<img src="https://latex.codecogs.com/gif.latex?x_1" /> が広さ、<img src="https://latex.codecogs.com/gif.latex?x_2" />が駅からの距離、<img src="https://latex.codecogs.com/gif.latex?x_3" />が治安等々
<br />
<br />

<img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;a}()" title="\frac{\partial }{\partial a}" />  

<img src="https://latex.codecogs.com/gif.latex?\partial" title="\partial" />は（ラウンド）ディーと呼ぶ。


```aで偏微分する = a以外を定数だと仮定して微分する```

### 例題
(1) <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;a}(3a^2)" />   
<br />
<br />
    <img src="https://latex.codecogs.com/gif.latex?=3*\frac{\partial&space;}{\partial&space;a}(a^2)" /> aをxと読み替える。aと関係ないところは外にだしてOK。3以外は微分の公式```(x^2) = 2x```と同じなので、  
    <img src="https://latex.codecogs.com/gif.latex?=3*\frac{\partial&space;}{\partial&space;x}(x^2)" />となる  
    <img src="https://latex.codecogs.com/gif.latex?=3*2a" />  
    <img src="https://latex.codecogs.com/gif.latex?=6a" />  
    
<br />
<br />
                                                                                                   
(2) <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;x^1}(4x_1+3x_2)" />  
足し算は分解しても良い  
<br />
<br />
 <img src="https://latex.codecogs.com/gif.latex?=\frac{\partial&space;}{\partial&space;a}(4x_1)+\frac{\partial&space;}{\partial&space;a}(3x_2)" /> <img src="https://latex.codecogs.com/gif.latex?x_1" />以外は外に出して良いので、  
 <img src="https://latex.codecogs.com/gif.latex?=4*\frac{\partial&space;}{\partial&space;a}(x_1)+3x_2*\frac{\partial&space;}{\partial&space;x_2}(1)" />    
 <img src="https://latex.codecogs.com/gif.latex?=4*1+3x_2*0" />  
 <img src="https://latex.codecogs.com/gif.latex?=4" />  
 
 ヒント：<img src="https://latex.codecogs.com/gif.latex?x_1" />と関係ないものは0になるので、最初から0としてしまっても良い
 
<br />
<br />

 (3) <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;a}(C_o-2C_1a+C_2a^2)" />   
<br />
<br />
<img src="https://latex.codecogs.com/gif.latex?=C_0*\frac{\partial&space;}{\partial&space;a}(1)-2C_1*\frac{\partial&space;}{\partial&space;a}(a)+C_2*\frac{\partial&space;}{\partial&space;a}(a^2)">    
<img src="https://latex.codecogs.com/gif.latex?=C_0*0-2C_1*1+2C_2a" />   
<img src="https://latex.codecogs.com/gif.latex?=-2C_1+2C_2a" />  
 
