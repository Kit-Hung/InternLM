# 训练自己的小助手认知
![img.png](images/img.png)

![img_1.png](images/img_1.png)

![img_2.png](images/img_2.png)

![img_3.png](images/img_3.png)

## 常规训练
![img_4.png](images/img_4.png)

## 使用 deepspeed 来加速训练
![img_5.png](images/img_5.png)

## 模型转换
![img_6.png](images/img_6.png)

![img_7.png](images/img_7.png)

## 模型整合
![img_8.png](images/img_8.png)

![img_9.png](images/img_9.png)

## 对话测试
### 使用微调后的模型
![img_10.png](images/img_10.png)


### 使用原模型
![img_11.png](images/img_11.png)


### 使用 --adapter 参数与完整的模型进行对话
![img_12.png](images/img_12.png)


## Web demo 部署
![img_13.png](images/img_13.png)



# XTuner多模态训练与测试
按照教程安装出来的 transformers 版本为 4.41.2，在执行 1.3.4.3 开始 Finetune 时会报如下的错
![img.png](images/img_14.png)

修复方法如下，安装 4.39.3 版本：
```shell
pip install transformers==4.39.3
```

已提交 pr 增加版本限制

## Finetune 前
![img_1.png](images/img_15.png)

## Finetune后
![img_2.png](images/img_16.png)