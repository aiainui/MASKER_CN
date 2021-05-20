# #coding: utf-8
# #author: dengyulong
# #date:   2021/2/2 3:22 下午
# #IDE:    PyCharm
#
# import pandas as pd
# from sklearn.model_selection import train_test_split
#
# # 0. 将eval.csv改为test.csv
# # 1. 合并 测试集、训练集、验证集
# # 2. 将合并后的数据集划分为训练集和验证集 6：2
#
# # 1
# data_path = '../test_data/new/usual/'
# all_train_data = []
# df1 = pd.read_csv(data_path + 'dev1.csv')
# df2 = pd.read_csv(data_path + 'test.csv')
# df3 = pd.read_csv(data_path + 'train1.csv')
# data1 = df1.values.tolist()
# data2 = df2.values.tolist()
# data3 = df3.values.tolist()
# all_train_data.extend(data1)
# all_train_data.extend(data2)
# all_train_data.extend(data3)
#
# header = list(df1.columns)
# df = pd.DataFrame(data=all_train_data, columns=header, index=None)
# df.to_csv('new_data.csv')
#
# # 2
# x = []
# y = []
# for i in all_train_data:
#     x.append(i)
#     y.append(i[0])
#
# X_train, X_dev, y_train, y_dev = train_test_split(x, y, test_size=0.25, random_state=0)
#
# df = pd.DataFrame(data=X_train, columns=header, index=None)
# df.to_csv('train1.csv')
#
# df = pd.DataFrame(data=X_dev, columns=header, index=None)
# df.to_csv('dev1.csv')