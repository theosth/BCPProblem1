import tensorflow as tf
import numpy as np
import os

# Generate sample data
X = np.random.random((1000, 10))
Y = np.random.random((1000, 1))

# Create a simple TensorFlow model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X, Y, epochs=10, batch_size=32)

# Save the trained model
model.save('model')

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# Move the model folder to the output directory
os.rename('model', 'output/model')
