````markdown
# MNIST Handwritten Digit Recognizer

A beginner deep-learning project that recognizes handwritten digits using a neural network trained on the MNIST dataset.

This is my first project using deep learning. The main goal of this project was to understand the basic workflow of training, evaluating, experimenting with, saving, and using a neural network for image classification.

**Completed:** 5 September 2026

## Project Overview

The model is trained on the MNIST handwritten digit dataset, which contains low-resolution grayscale images of handwritten digits from 0 to 9.

The project includes:

- Training a neural network on MNIST
- Evaluating the model on training, validation, and test data
- Running controlled experiments with different training configurations
- Comparing the results of each experiment
- Saving the final trained model
- Loading the saved model in `main.py`
- Preprocessing a handwritten image
- Using the trained model to predict a digit

## Model

The model is a basic neural network designed for the MNIST dataset.

It was trained specifically on the type of low-resolution images used by MNIST. Therefore, the model performs best when the input image has a similar appearance and structure.

For example, handwritten digits should ideally be:

- Low resolution
- Grayscale
- Centered
- Clearly visible
- Similar in scale to MNIST digits
- Black digits on a white background

The application includes basic preprocessing to crop, resize, center, and normalize an input image before sending it to the model.

## Important Limitation

This model is **primarily designed for MNIST-style, low-resolution handwritten digit images**.

It is not intended to recognize arbitrary handwritten digits from photographs, documents, or images with significantly different visual characteristics.

For example, a digit drawn with a very thin brush, unusual positioning, or a very different scale may be classified incorrectly because the input differs from the data the model was trained on.

Improving recognition on a wider variety of real-world handwriting would require additional training data, preprocessing techniques, or a more advanced architecture such as a Convolutional Neural Network (CNN).

## Experiments

Controlled experiments were performed to understand how different training configurations affected the model.

The experiments included changes to training parameters such as:

- Number of epochs
- Batch size
- Other training configurations

The final model was selected based on its validation and test performance.

The experiment results are documented in:

`experiments_report.txt`

## Project Structure

```text
Project_08/
│
├── data/
│   └── mnist.npz
│
├── models/
│   └── digit_recognizer_model.pkl
│
├── notebooks/
│   └── experimentation.ipynb
│
├── main.py
├── README.md
├── requirements.txt
├── sample_digit.png
├── .gitignore
└── experiments_report.txt
````

## How It Works

The application follows this basic pipeline:

```text
Handwritten Image
       ↓
Grayscale Conversion
       ↓
Image Inversion
       ↓
Digit Detection / Cropping
       ↓
Resize
       ↓
Center on 28×28 Canvas
       ↓
Normalization
       ↓
Neural Network
       ↓
Predicted Digit
```

## Running the Project

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

The application loads the trained model and processes the input image before displaying the predicted digit.

## Technologies Used

* Python
* NumPy
* Pillow
* TensorFlow / Keras
* Joblib
* Matplotlib
* Jupyter Notebook

## Learning Outcome

This project helped me understand the basic deep-learning workflow:

**Data → Preprocessing → Model → Training → Evaluation → Experimentation → Saving → Inference**

It serves as my first practical introduction to deep learning and image classification.

```
