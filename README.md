# Image Classification App

## Introduction
This image classification app is a simple, user-friendly tool that allows users to upload an image and have it classified into one of the CIFAR-10 categories. The app is built using Streamlit and TensorFlow. Additionally, the repository contains a Jupyter Notebook with the code used to train the model.

## Getting Started

### Prerequisites for the App
Before running the app, you need to have Python installed on your system. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

### Installation for the App
To run this app, you need to install several Python libraries. The required libraries are listed below:

- Streamlit
- PIL (Python Imaging Library)
- NumPy
- TensorFlow

You can install these libraries using pip. Run the following command to install all required libraries at once:

```bash
pip install streamlit Pillow numpy tensorflow
```

### Running the App
1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/LouisChislett/Image_Classification_App.git
   ```

2. Navigate to the cloned repository:

   ```bash
   cd Image_Classification_App
   ```

3. Run the app using Streamlit:

   ```bash
   streamlit run app.py
   ```

4. The app should now be running on your local server. Streamlit will provide a local URL which you can open in your web browser.


### Usage
- Once the app is running, you will see an option to upload an image.
- Upload a `.jpg`, `.jpeg`, or `.png` image file.
- The app will display the uploaded image and predict its category among the CIFAR-10 classes (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck).

### Jupyter Notebook
The repository also includes a Jupyter Notebook that contains the code for training the image classification model. To run this notebook, you will need to install the following libraries:

- NumPy
- Matplotlib
- TensorFlow
- Seaborn
- Pandas
- Scikit-learn

These libraries can be installed via pip as follows:

```bash
pip install numpy matplotlib tensorflow seaborn pandas scikit-learn
```

## Contact
For more information, you can contact me on LinkedIn at https://www.linkedin.com/in/louis-chislett-4ba82919b/
