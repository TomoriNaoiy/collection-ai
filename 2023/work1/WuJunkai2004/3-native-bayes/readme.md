### 采用朴素贝叶斯来识别mnist数据集

~ 本来写好了dataset和dataload的版本，但是跑不通了 ~  
通过对数字切割区块，统计各区块像素密度，以概率学和统计学的方式预测mnist数据集。

### 复现方法
```cmd
run.bat
```

### 初步总结
在我测试过的所有密度区分中，`[0.125] * 8`是表现最优的，对测试集有近60%的正确率。  
密度区分并非越高越好， `[0.1] * 10` 的表现反而不佳。  
可以在 `param.py` 里面更改密度的参数。  

### 其他
> 附部分测试数据的密度参数与结果

train one  
0.35 0.25 0.2 0.2  
  
train two  
0.2 0.2 0.2 0.2 0.2  

train three  
0.3, 0.14, 0.14, 0.14, 0.14, 0.14  

train four  
[0.2, 0.2, 0.15, 0.15, 0.1, 0.1, 0.1]  
correct: 5769  
wrong: 4231  
accuracy: 0.5769  

train five  
[0.125] * 8  
correct: 5904  
wrong: 4096  
accuracy: 0.5904  

train six  
[0.100000000001] * 10  
accuracy: 0.58  