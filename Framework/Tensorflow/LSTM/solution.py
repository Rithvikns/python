import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Define the model
model = Sequential()

# LSTM Layer: 28 neurons, each with 2 memory units
model.add(LSTM(units=28, return_sequences=False, activation='tanh', recurrent_activation='sigmoid', recurrent_dropout=0.0))

# Fully Connected Neural Network (FCNN)
model.add(Dense(30, activation='relu'))
model.add(Dense(30, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='softmax'))  # Assuming classification task

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Print model summary
model.summary()
