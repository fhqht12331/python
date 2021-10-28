import pandas as pd
import numpy
import tensorflow as tf


from tensorflow.keras.models import Sequential
from sklearn.svm import SVC
from sklearn import svm
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from tensorflow.python.ops.gen_math_ops import sigmoid

# seed 값 설정
numpy.random.seed(3)
tf.random.set_seed(3)

# 데이터 입력
df = pd.read_csv('C:\\Users\\윤창주\\PYTHONWORKTABLE\\gilbutITbook080228\\deeplearning\\dataset\\sonar.csv', header=None)
'''
# 데이터 개괄 보기
print(df.info())

# 데이터의 일부분 미리 보기
print(df.head())
'''
dataset = df.values
X = dataset[:,0:60].astype(float)
Y_obj = dataset[:,60]

from sklearn.preprocessing import StandardScaler

standardizer = StandardScaler().fit(X)
X_sc = standardizer.transform(X)

# 문자열 변환
e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)

# 모델 설정
svm_model = svm.SVC(kernel='linear')
svm_model.fit(X, Y)

# 결과 출력
print("Accuracy: %.2f%%" % (svm_model.score(X_sc, Y)* 100))