from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

import numpy as np
import tensorflow as tf
from tensorflow.python.keras.backend import sigmoid

np.random.seed(3)
tf.random.set_seed(3)

# min-max norm 코드
tf.keras.constraints.MinMaxNorm(
    min_value=0.0, max_value=1.0, rate=1.0, axis=0
)

Data_set = np.loadtxt("C:\\Users\\윤창주\PYTHONWORKTABLE\\gilbutITbook080228\\deeplearning\\dataset\\ThoraricSurgery.csv", delimiter=",")

X = Data_set[:,0:17]
Y = Data_set[:,17]



model = Sequential()
model.add(Dense(30, input_dim=17, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=100, batch_size=10, validation_split=0.2)

