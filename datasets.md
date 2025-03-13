# Datasets
Datasets recommended for an assessment (CW) preparation
## Fashion MNIST (Clothing Classification)
* Used for demo-version of the course work - **do not pick this one**.

## CIFAR-10 (Object Recognition)
* 10 categories of color images (32×32, RGB)

To import:
```
from tensorflow.keras.datasets import cifar10

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

print(X_train.shape, X_test.shape)  # Output: (50000, 32, 32, 3) (10000, 32, 32, 3)
```
## CIFAR-100 (More Complex Object Recognition)
* CIFAR-100 (More Complex Object Recognition)

To import:
```
from tensorflow.keras.datasets import cifar100

(X_train, y_train), (X_test, y_test) = cifar100.load_data()

print(X_train.shape, X_test.shape)  # Output: (50000, 32, 32, 3) (10000, 32, 32, 3)
```
## MNIST (Handwritten Digit Classification)
* The MNIST dataset (Modified National Institute of Standards and Technology) is a classic dataset used for handwritten digit classification.
* It contains grayscale images of digits 0-9, each 28×28 pixels in size.
```
from tensorflow.keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

print(X_train.shape, X_test.shape)  # Loads the dataset and splits it into training (60,000 images) and testing (10,000 images)
```
## Kuzushiji-MNIST (KMNIST)
* A dataset of 28x28 grayscale images representing 10 classes of cursive Japanese (Kuzushiji) characters
* It serves as a more challenging drop-in replacement for MNIST
* Size: 70,000 images (60,000 training and 10,000 testing)
* [GitHub repo](https://github.com/rois-codh/kmnist)

## notMNIST
* Contains images of letters A-J taken from different fonts, formatted similarly to MNIST
* Size: 500,000 images across 10 classes
* [Source](https://yaroslavvb.blogspot.com/2011/09/notmnist-dataset.html)

## Street View House Numbers (SVHN)
* Contains over 600,000 32x32 color images of house numbers (digits 0-9) extracted from Google Street View images
* It's similar in format to **MNIST** but includes color images and more variability
* Size: Over 600,000 images.
* [Source](http://ufldl.stanford.edu/housenumbers/)
