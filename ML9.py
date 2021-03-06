from scipy.io import loadmat
import pandas as pd
import matplotlib.pyplot as plt

mnist_raw = loadmat("mnist-original.mat")
mnist = {
    "data": mnist_raw["data"].T,
    "target": mnist_raw["label"][0]
}

# traing, set
# 1 - 60000
# 60001 - 70000
x, y = mnist["data"], mnist["target"]
# train & test set
# class 0 - 9
x_train, x_test, y_train, y_test = x[:60000], x[60000:], y[:60000], y[60000:]

# 0 - 9
# 5000
# 5
# True, False

# class 0 ບໍ່ແມ່ນ class 0
# ຂໍ້ມູນຄ່າ 5000 -> model -> class 0 ຫຼືບໍ? True : False
# y_train = [0,0,........,9....,9]
predict_number = 5000
y_train_0 = (y_train == 0)
y_test_0 = (y_test == 0)

# y_train_0 = [true,true,........,false....,false]

print(y_train_0.shape, y_train_0)
print(y_test_0.shape, y_test_0)
