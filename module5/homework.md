# 使用Transformer库运行模型
![img.png](images/img.png)


# 使用LMDeploy与模型对话
![img_1.png](images/img_1.png)


# LMDeploy模型量化(lite)
## 设置最大KV Cache缓存大小
### 不加 --cache-max-entry-count 参数
![img_2.png](images/img_2.png)


### 加 --cache-max-entry-count 0.5 参数
![img_3.png](images/img_3.png)


### 加 --cache-max-entry-count 0.01 参数
![img_4.png](images/img_4.png)


## 使用W4A16量化
### 不加 --cache-max-entry-count 参数
![img_5.png](images/img_5.png)

![img_6.png](images/img_6.png)


### 加 --cache-max-entry-count 0.01 参数
![img_7.png](images/img_7.png)


# LMDeploy服务(serve)
## 启动API服务器
![img_8.png](images/img_8.png)


## 命令行客户端连接API服务器
![img_9.png](images/img_9.png)


## 网页客户端连接API服务器
![img_10.png](images/img_10.png)


# Python代码集成
## Python代码集成运行1.8B模型
![img_11.png](images/img_11.png)


## 向TurboMind后端传递参数
![img_12.png](images/img_12.png)


# 拓展部分
## 使用LMDeploy运行视觉多模态大模型llava
### 使用pipeline推理 llava-v1.6-7b
![img_13.png](images/img_13.png)


### 通过 Gradio 来运行 llava 模型
![img_14.png](images/img_14.png)


## 定量比较LMDeploy与Transformer库的推理速度差异
### Transformer 库推理 Internlm2-chat-1.8b
![img_15.png](images/img_15.png)


### LMDeploy的推理速度
![img_16.png](images/img_16.png)

