# Model Information

The Blood Cancer Detection Web App uses a Convolutional Neural Network (CNN) model implemented using Keras. The model architecture is as follows:

- Convolutional layer with 32 filters, a kernel size of 3x3, input shape of 64x64x3, and 'relu' activation function.
- MaxPooling layer with pool size of 2x2.
- Another Convolutional layer with 32 filters, a kernel size of 3x3, and 'relu' activation function.
- Another MaxPooling layer with pool size of 2x2.
- Flatten layer to flatten the tensor output from the previous layer.
- Dense layer with 128 units and 'relu' activation function.
- Output Dense layer with 1 unit and 'sigmoid' activation function.

The model is compiled with 'adam' optimizer, 'binary_crossentropy' loss function, and 'accuracy' as the metric.

The model takes an image of size 64x64x3 as input and outputs a single value between 0 and 1 indicating the probability of the image being blood cancer.
