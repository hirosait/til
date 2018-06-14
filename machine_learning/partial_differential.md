# 偏微分

多変数の微分。つまりxの数が増えていく。  
例：yが家賃、x1が広さ、x2が駅からの距離、x3が治安とうとう

<img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;a}()" title="\frac{\partial }{\partial a}" />  

<img src="https://latex.codecogs.com/gif.latex?\partial" title="\partial" />は（ラウンド）ディーと呼ぶ。


aで偏微分する = a以外を定数だと仮定して微分する  

### 例題
(1) <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;a}(3a^2)" />   
    = 3 x <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;a}(a^2)" /> aをxと読み替える。aと関係ないところは外にだしてOK。3以外は(x^2) = 2xと同じなので、
    = 3 x <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;a}(a^2)" /> 
                                                                                                      = 3 x 2a 
                                                                                                      = 6a
                                                                                                      
(2) <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;x^2}(4x_1+3x_2)" /> 足し算は分解しても良い  
 = <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;a}(4x_1)+\frac{\partial&space;}{\partial&space;a}(3x_2)" />   
 = <img src="https://latex.codecogs.com/gif.latex?4*\frac{\partial&space;}{\partial&space;a}(x_1)+3x_2*\frac{\partial&space;}{\partial&space;x_2}(1)" />   
 = 4 x 1 + 3x2 x 0 + 0  
 = 4  
 x1と関係ないものは0になるので、最初から0としてしまっても良い
 
 (3) <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;a}(C_o-2C_1a+C_2a^2)" />   
 = <img src="https://latex.codecogs.com/gif.latex?C_0*\frac{\partial&space;}{\partial&space;a}(1)-2C_1*\frac{\partial&space;}{\partial&space;a}(a)+C_2*\frac{\partial&space;}{\partial&space;a}(a^2)">  
 = <img src="https://latex.codecogs.com/gif.latex?C_0*0-2C_1*1+2C_2a" />   
 = <img src="https://latex.codecogs.com/gif.latex?-2C_1+2C_2a" />   
 
