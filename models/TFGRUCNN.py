import tensorflow as tf


class TFGRUCNN:
    def __init__(self, n_classes=1):
        # Get model hyperparameters
        self.n_classes = n_classes

    def build_model(self,
                    input_shape,
                    dropout=0.25,
                    cnn_filters=32,
                    cnn_kernel_size=3,
                    cnn_pool_size=2,
                    unit=128
                    ):

        inputs = tf.keras.Input(shape=input_shape)
        x = inputs

        # LSTM Layer
        x = tf.keras.layers.GRU(units=unit, activation="tanh", return_sequences=True)(x)
        x = tf.keras.layers.Dropout(dropout)(x)
        
        # CNN Layer
        x = tf.keras.layers.Conv1D(filters=cnn_filters, kernel_size=cnn_kernel_size, activation='relu')(x)
        x = tf.keras.layers.MaxPooling1D(pool_size=cnn_pool_size)(x)
        x = tf.keras.layers.Flatten()(x)

        # output layer
        outputs = tf.keras.layers.Dense(self.n_classes)(x)

        return tf.keras.Model(inputs, outputs)
