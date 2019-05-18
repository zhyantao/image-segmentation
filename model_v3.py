from keras.models import *
from keras.layers import *
from keras.optimizers import *

IMG_SIZE_Width = 512  # cols
IMG_SIZE_Height = 64  # rows

def unet(pretrained_weights=None, input_size=(IMG_SIZE_Height, IMG_SIZE_Width, 1),num_class=2):
    inputs = Input(input_size)
    conv1 = conv3D(32, 3, activation='relu', padding='same', kernel_initializer='he_normal')(inputs)
    conv1 = conv3D(32, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

    conv2 = conv3D(64, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool1)
    conv2 = conv3D(64, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)

    conv3 = conv3D(128, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool2)
    conv3 = conv3D(128, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)

    conv4 = conv3D(256, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool3)
    conv4 = conv3D(256, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv4)
    pool4 = MaxPooling2D(pool_size=(2, 2))(conv4)

    conv5 = conv3D(512, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool4)
    conv5 = conv3D(512, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv5)
    drop5 = Dropout(0.5)(conv5)
    pool5 = MaxPooling2D(pool_size=(2, 2))(drop5)

    conv6 = conv3D(1024, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool5)
    conv6 = conv3D(1024, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv6)
    drop6 = Dropout(0.5)(conv6)

    up7 = conv3D(512, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
        UpSampling2D(size=(2, 2))(drop6))
    merge7 = concatenate([drop5, up7], axis=3)
    conv7 = conv3D(512, 3, activation='relu', padding='same', kernel_initializer='he_normal')(merge7)
    conv7 = conv3D(512, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv7)

    up8 = conv3D(256, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
        UpSampling2D(size=(2, 2))(conv7))
    merge8 = concatenate([conv4, up8], axis=3)
    conv8 = conv3D(256, 3, activation='relu', padding='same', kernel_initializer='he_normal')(merge8)
    conv8 = conv3D(256, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv8)

    up9 = conv3D(128, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
        UpSampling2D(size=(2, 2))(conv8))
    merge9 = concatenate([conv3, up9], axis=3)
    conv9 = conv3D(128, 3, activation='relu', padding='same', kernel_initializer='he_normal')(merge9)
    conv9 = conv3D(128, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv9)

    up10 = conv3D(64, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
        UpSampling2D(size=(2, 2))(conv9))
    merge10 = concatenate([conv2, up10], axis=3)
    conv20 = conv3D(64, 3, activation='relu', padding='same', kernel_initializer='he_normal')(merge10)
    conv20 = conv3D(64, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv20)
	
    up11 = conv3D(32, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
        UpSampling2D(size=(2, 2))(conv20))
    merge11 = concatenate([conv1, up11], axis=3)
    conv21 = conv3D(32, 3, activation='relu', padding='same', kernel_initializer='he_normal')(merge11)
    conv21 = conv3D(32, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv21)
    conv21 = conv3D(num_class, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv21)

    if num_class == 2:
        conv22 = conv3D(1, 1, activation='sigmoid')(conv21)
        loss_function = 'binary_crossentropy'
    else:
        conv22 = conv3D(num_class, 1, activation='softmax')(conv21)
        loss_function = 'categorical_crossentropy'
    model = Model(input=inputs, output=conv22)

    model.compile(optimizer=Adam(lr=1e-4), loss=loss_function, metrics=["accuracy"])
    model.summary()

    if (pretrained_weights):
        model.load_weights(pretrained_weights)
    return model
