import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# 1. 下载数据（以特斯拉 TSLA 为例）
df = yf.download('TSLA', start='2020-01-01', end='2024-01-01')
data = df[['Close']].values

# 2. 数据归一化
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# 3. 创建训练数据（时间步长为60天）
X_train, y_train = [], []
time_step = 60
for i in range(time_step, len(scaled_data)):
    X_train.append(scaled_data[i-time_step:i, 0])
    y_train.append(scaled_data[i, 0])

X_train, y_train = np.array(X_train), np.array(y_train)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# 4. 构建 LSTM 模型
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
    LSTM(50, return_sequences=False),
    Dense(25),
    Dense(1)
])
model.compile(optimizer='adam', loss='mean_squared_error')

# 5. 训练模型
model.fit(X_train, y_train, epochs=10, batch_size=32)

# 6. 预测并还原价格
predicted_price = model.predict(X_train)
predicted_price = scaler.inverse_transform(predicted_price)

# 7. 可视化
plt.plot(df.index[time_step:], data[time_step:], label="Actual Price")
plt.plot(df.index[time_step:], predicted_price, label="Predicted Price")
plt.legend()
plt.show()
