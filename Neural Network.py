import numpy as np
import tensorflow as tf

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
print(type(x_train))
print(type(y_train))

print(x_train.shape)
print(x_test.shape)

print(x_train[9832])
print(y_train[9832])

x_train = np.reshape(x_train, (x_train.shape[0], 784)) / 255
x_test = np.reshape(x_test, (x_test.shape[0], 784)) / 255

y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)
print(y_train[9832])


class NeuralNetwork:
    def __init__(self, layers):  # [784,128,128,10]
        self.layers = layers
        self.length = len(layers)
        self.features = layers[0]
        self.classes = layers[-1]

        self.W = {}
        self.b = {}

        self.dW = {}
        self.db = {}

        for i in range(1, self.length):
            self.W[i] = tf.Variable(
                tf.random.normal(shape=(self.layers[i], self.layers[i - 1]))
            )
            self.b[i] = tf.Variable(tf.random.normal(shape=(self.layers[i], 1)))

    def train(self, x_train, y_train, epochs, steps_per_epoch, batch_size, lr):

        history = {"val_loss": [], "train_loss": []}

        for epoch in range(0, epochs):
            epoch_train_loss = 0
            for i in range(0, steps_per_epoch):
                x_batch = x_train[i * batch_size : (i + 1) * batch_size]
                y_batch = y_train[i * batch_size : (i + 1) * batch_size]

                batch_loss = self.train_my_batch(x_batch, y_batch, lr)
                epoch_train_loss += batch_loss

                if i % int(steps_per_epoch / 10) == 0:
                    print(".")

            val_A = self.forward_propagation(x_test)
            val_loss = self.calculate_loss(val_A, y_test)
            history["val_loss"].append(val_loss)

            print(f"val loss: {val_loss}")

    def train_my_batch(self, x_batch, y_batch, lr):
        x_batch = tf.convert_to_tensor(x_batch, dtype=tf.float32)
        y_batch = tf.convert_to_tensor(y_batch, dtype=tf.float32)

        with tf.GradientTape(persistent=True) as tape:
            activation = self.forward_propagation(x_batch)
            batch_loss = self.calculate_loss(activation, y_batch)

            for i in range(1, self.length):
                self.dW[i] = tape.gradient(batch_loss, self.W[i])
                self.db[i] = tape.gradient(batch_loss, self.b[i])

        del tape
        self.update_with_lr(lr)
        return batch_loss.numpy()

    def forward_propagation(self, x_batch):
        result = tf.convert_to_tensor(x_batch, dtype=tf.float32)

        for i in range(1, self.length):
            intermediate = tf.matmul(result, tf.transpose(self.W[i])) + tf.transpose(
                self.b[i]
            )

            if i != self.length - 1:
                result = tf.nn.sigmoid(intermediate)
            else:
                result = intermediate

        return result

    def calculate_loss(self, activation, y_batch):
        loss = tf.nn.softmax_cross_entropy_with_logits(y_batch, activation)
        return tf.reduce_mean(loss)

    def update_with_lr(self, lr):
        for i in range(1, self.length):
            self.W[i].assign_sub(lr * self.dW[i])
            self.b[i].assign_sub(lr * self.db[i])


nn = NeuralNetwork([784, 128, 128, 10])
epochs = 10
batch_size = 10
steps_per_epoch = int(x_train.shape[0] / batch_size)
lr = 3e-3
nn.train(x_train, y_train, epochs, steps_per_epoch, batch_size, lr)