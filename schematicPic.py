#from schemdraw import logic


#logic.Nand(inputs=3)

#%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt
#from IPython.display import Image, display
import tensorflow as tf


import keras_lmu

seed = 0
tf.random.set_seed(seed)
np.random.seed(seed)
rng = np.random.RandomState(seed)

(train_images, train_labels), (
    test_images,
    test_labels,
) = tf.keras.datasets.mnist.load_data()


train_images = train_images / 255
test_images = test_images / 255

plt.figure()
plt.imshow(np.reshape(train_images[0], (28, 28)), cmap="gray")
plt.axis("off")
plt.title(f"Sample image of the digit '{train_labels[0]}'")
plt.show()

train_images = train_images.reshape((train_images.shape[0], -1, 1))
test_images = test_images.reshape((test_images.shape[0], -1, 1))

# we'll display the sequence in 8 rows just so that it fits better on the screen
plt.figure()
plt.imshow(train_images[0].reshape(8, -1), cmap="gray")
plt.axis("off")
plt.title(f"Sample sequence of the digit '{train_labels[0]}' (reshaped to 98 x 8)")
plt.show()

perm = rng.permutation(train_images.shape[1])
train_images = train_images[:, perm]
test_images = test_images[:, perm]

plt.figure()
plt.imshow(train_images[0].reshape(8, -1), cmap="gray")
plt.axis("off")
plt.title(f"Permuted sequence of the digit '{train_labels[0]}' (reshaped to 98 x 8)")
plt.show()

X_train = train_images[:50000]
X_valid = train_images[50000:]
X_test = test_images

Y_train = train_labels[:50000]
Y_valid = train_labels[50000:]
Y_test = test_labels

print(
    f"Training inputs shape: {X_train.shape}, "
    f"Training targets shape: {Y_train.shape}"
)
print(
    f"Validation inputs shape: {X_valid.shape}, "
    f"Validation targets shape: {Y_valid.shape}"
)
print(f"Testing inputs shape: {X_test.shape}, Testing targets shape: {Y_test.shape}")

n_pixels = X_train.shape[1]

lmu_layer = keras_lmu.LMU(
    memory_d=1,
    order=256,
    theta=n_pixels,
    hidden_cell=tf.keras.layers.SimpleRNNCell(212),
    hidden_to_memory=False,
    memory_to_memory=False,
    input_to_hidden=True,
    kernel_initializer="ones",
)

# TensorFlow layer definition
inputs = tf.keras.Input((n_pixels, 1))
lmus = lmu_layer(inputs)
outputs = tf.keras.layers.Dense(10)(lmus)

# TensorFlow model definition
model = tf.keras.Model(inputs=inputs, outputs=outputs)
model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer="adam",
    metrics=["accuracy"],
)
model.summary()

do_training = True
batch_size = 100
epochs = 10

saved_weights_fname = "./psMNIST-weights.hdf5"
callbacks = [
    tf.keras.callbacks.ModelCheckpoint(
        filepath=saved_weights_fname, monitor="val_loss", verbose=1, save_best_only=True
    ),
]

if do_training:
    result = model.fit(
        X_train,
        Y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(X_valid, Y_valid),
        callbacks=callbacks,
    )
    
if do_training:
    plt.figure()
    plt.plot(result.history["val_accuracy"], label="Validation")
    plt.plot(result.history["accuracy"], label="Training")
    plt.legend()
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("Post-epoch training accuracies")
    plt.xticks(np.arange(epochs), np.arange(1, epochs + 1))
    plt.ylim((0.85, 1.0))  # Restrict range of y axis to (0.85, 1) for readability
    plt.savefig("psMNIST-training.png")

    val_loss_min = np.argmin(result.history["val_loss"])
    print(
        f"Maximum validation accuracy: "
        f"{round(result.history['val_accuracy'][val_loss_min] * 100, 2):.2f}%"
    )

else:
    print ("Look at image psMNIST-training.png")
#    display(Image(filename="psMNIST-training.png"))


model.load_weights(saved_weights_fname)
accuracy = model.evaluate(X_test, Y_test)[1] * 100
print(f"Test accuracy: {round(accuracy, 2):0.2f}%")