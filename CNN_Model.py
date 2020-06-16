from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.models import Sequential 

cnn = Sequential()
cnn.add(Conv2D(44, kernel_size=(5,5), input_shape=(64,64,1), padding='same', activation='relu'))
cnn.add(MaxPooling2D(pool_size=(4,4)))
cnn.add(Conv2D(44, kernel_size=(5,5), padding='same', activation='relu'))
cnn.add(MaxPooling2D(pool_size=(4,4)))
cnn.add(Dropout(0.2))
cnn.add(Flatten())
cnn.add(Dense(14, activation = 'softmax')) 

cnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print(cnn.summary())

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
        'images_separated/train_data',
        target_size=(64, 64),
        color_mode = 'grayscale',
        batch_size=16)

validation_datagen = ImageDataGenerator(rescale=1./255) 
validation_generator = validation_datagen.flow_from_directory(
        'images_separated/validation_data',
        target_size=(64, 64),
        color_mode = 'grayscale',
        batch_size=16)

cnn.fit_generator(
        train_generator,
        steps_per_epoch=5000,
        epochs=10,
        validation_data=validation_generator,
        validation_steps=2000)

test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
        'images_separated/test_data',
        target_size=(64, 64),
        color_mode = 'grayscale',
        batch_size=16)

print(cnn.evaluate_generator(test_generator))