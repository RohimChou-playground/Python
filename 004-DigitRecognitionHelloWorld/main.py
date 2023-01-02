import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from keras.optimizers import Adam

import util

# train_images 圖檔們 (60000,28,28), train_images_labels 圖檔的標籤 (60000)
# test_images 驗證用的圖檔們 (10000,28,28), test_images_labels 驗證用的圖檔們的標籤 (10000)
(train_images, train_images_labels), (test_images, test_images_labels) = mnist.load_data()

# load previously trained model, if already exist
model_name = 'savedmodels/model1'
cnn_model = util.load_model_or_default(model_name)

if cnn_model is None:
    # Define and fit the model
    cnn_model = Sequential()

    cnn_model.add(Conv2D(32, 3, 3, input_shape=(28,28,1), activation='relu'))
    cnn_model.add(MaxPooling2D(pool_size = (2,2)))
    cnn_model.add(Flatten())
    cnn_model.add(Dense(32, activation='relu'))
    cnn_model.add(Dense(10, activation='sigmoid'))

    cnn_model.compile(loss ='sparse_categorical_crossentropy', optimizer=Adam(learning_rate=0.001), metrics =['accuracy'])
    cnn_model.fit(train_images, train_images_labels, batch_size=512, epochs=30, verbose=1, validation_data=(test_images, test_images_labels))
    cnn_model.save(model_name) # create a savedmodels/model1 folder to save model model1

# check the model
cnn_model.summary()

# Make a prediction and validate it
predictions = cnn_model.predict(test_images)
print(predictions[0])
print(np.argmax(predictions[0]))
util.showSomeImages(test_images, test_images_labels, random=False)
plt.show()