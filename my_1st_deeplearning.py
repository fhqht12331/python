# 필요한 라이브러리를 불러옵니다.
import numpy as np
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt 

# 실행할 때마다 같은 결과를 출력하기 위해 설정하는 부분입니다.
np.random.seed(3)
tf.random.set_seed(3)

# 준비된 수술 환자 데이터를 불러들입니다.
Data_set = np.loadtxt("ThoraricSurgery.csv", delimiter=",")

# 환자의 기록과 수술 결과를 X와 Y로 구분하여 저장합니다.
# 검증 셋 추가
X_train = Data_set[:320,0:17]
Y_train = Data_set[:320,17]
X_val = Data_set[320:, 0:17]
Y_val = Data_set[320:,17]
X_test = Data_set[400:, 0:17]
Y_test = Data_set[400:, 17]

X_train

pd.DataFrame(X_train) #X의 데이터를 한번 나열해본다. 이 데이터셋의 문제점이 무엇인지 생각해본다.

# min-max norm 코드
tf.keras.constraints.MinMaxNorm(
    min_value=0.0, max_value=1.0, rate=1.0, axis=0
)

# 딥러닝 구조를 결정합니다(모델을 설정하고 실행하는 부분입니다).
#model = Sequential()
#model.add(Dense(30, input_dim=17, activation='relu'))
#model.add(Dense(1, activation='sigmoid'))
from tensorflow import keras

model= keras.Sequential([
    keras.layers.Dense(30, input_dim=17, activation='relu'),
    keras.layers.Dense(30, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

# 딥러닝을 실행합니다.
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, Y_train, epochs=100, batch_size=10, validation_data=(X_val, Y_val)) # 검증 셋을 같이 실행

Y_pred=model.predict(X_test)

pd.DataFrame(Y_pred) #예측값이 0과 1이 아닌 값이 나온 이유를 고민해봅시다.

pd.DataFrame(Y_test)

X_test_table=pd.DataFrame(X_test) #엑셀파일로 내보내기 불러오기 

X_test_table.to_excel('X_test.xlsx', index=False)

X_test_table_read= pd.read_excel('X_test.xlsx')

X_test_table_read