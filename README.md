# WeBQA
针对于百度WebQA数据集，利用TF-IDF等模型构建的问答系统。数据集是苏剑林经过处理后的，地址：<br>
[link](https://spaces.ac.cn/archives/4338)<br>
代码来源：[代码](https://github.com/WenRichard/QAmodel-for-Retrievalchatbot/tree/master/QAdemo_base1)<br>

# 依赖
```
gensim
jieba
```

# 运行
```python
python model1.py 
```
或者
```python
python model2.py
```

# 结果展示
```shell
请输入问题(q退出): 火影忍者作者
亲，我们给您找到的答案是： 岸本齐史
same questions： 火影忍者的作者是谁？？,                score： 1.0
same questions： 火影忍者的作者是谁?,                score： 1.0
same questions： 火影忍者的作者是谁？,                score： 1.0
same questions： 火影忍者的作者是谁,                score： 1.0
same questions： 火影忍者作者是谁？bhuach,                score： 1.0
Time cost: 0.16709041595458984 s
请输入问题(q退出): 世界最高的山峰
亲，我们给您找到的答案是： 珠穆朗玛峰
same questions： 世界上最高的山峰是什么,                score： 1.0
same questions： 世界上最高的山峰,                score： 1.0
same questions： 世界上最高的山峰是什么？,                score： 1.0
same questions： 中国最高的山峰在哪里,                score： 0.8592539429664612
same questions： 世界上第二大山峰是什么峰？,                score： 0.6894765496253967
Time cost: 0.16444110870361328 s
```
