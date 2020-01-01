
import tensorflow as tf
import os

# 默认情况，TF 会占用所有 GPU 的所有内存, 我们可以指定
# 只有 GPU0 和 GPU1 这两块卡被看到，从而达到限制其使用所有GPU的目的
os.environ['CUDA_VISIBLE_DEVICES'] = '0, 1'

# 打印 TF 可用的 GPU
print (os.environ['CUDA_VISIBLE_DEVICES'])
