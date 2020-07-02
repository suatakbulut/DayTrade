import numpy as np
# from keras.layers import Conv2D, Dense, Flatten, MaxPooling2D, Dropout
from keras.layers import Dense, Flatten
from keras.models import Sequential 

cnn = Sequential() 

cnn.add(Flatten( input_shape=(44, 44, 3) )) 
cnn.add(Dense(44, activation = 'relu')) 
cnn.add(Dense(44, activation = 'relu')) 
cnn.add(Dense(44, activation = 'relu')) 
cnn.add(Dense(22, activation = 'relu')) 
cnn.add(Dense(22, activation = 'relu')) 
cnn.add(Dense(22, activation = 'relu')) 
cnn.add(Dense(3, activation = 'softmax')) 

cnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) 
print(cnn.summary())

parameters = {'color_mode' : 'rgb', 
              'shuffle' : True, 
              'batch_size': 128, 
              'target_size' : (44, 44)
              }
from keras.preprocessing.image import ImageDataGenerator
# Create train data generator
train_datagen = ImageDataGenerator(rescale = 1./255) 
train_generator = train_datagen.flow_from_directory(
        'images_separated/train_data', **parameters)

# Create validation data generator
validation_datagen = ImageDataGenerator(rescale = 1./255)  
validation_generator = validation_datagen.flow_from_directory(
        'images_separated/validation_data', **parameters)

# Fit the model
history  = cnn.fit_generator(
        train_generator,
        epochs= 20,
        validation_data=validation_generator
        ) 

test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
        'images_separated/test_data', **parameters)

# Calculate the accuracy of the model's predictions on the test data
test_loss, test_acc = cnn.evaluate_generator(test_generator, verbose=2)
print("Test Accuracy is {} %".format(round(100*test_acc,2)))

labels_true = test_generator.classes
labels_pred_probs = cnn.predict_generator(test_generator) 
labels_pred = np.argmax(labels_pred_probs, axis=1)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_true, labels_pred)
print(cm) 