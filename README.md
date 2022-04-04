# Birdcall Recognition

Final project of McGill AI Society Intro to ML Bootcamp (Winter 2022). [Demo hosted on Heroku](https://birdcall-recognition.herokuapp.com/).

## Project Description

This project is a web application that classifies birdcall recordings of twenty different species using mel spectrograms and a convolutional neural network. The classifier utilized the `efficientnet_pytorch` implementation of `EfficientNet-B7` and was trained on a subset of the [Cornell Birdcall Identification](https://www.kaggle.com/competitions/birdsong-recognition/data) dataset. The model was built using PyTorch, and the web app using Flask. Data preprocessing and augmentation was done through the `torchvision` package.

## Running the Application

Clone or otherwise download the repository. You may need to install [Git Large File Storage](https://git-lfs.github.com/).

### Using Docker

Using a terminal, navigate to the `/app` subdirectory and run
```
docker build -t birdcall-recognition .
```

Start the app container with
```
docker run -dp 8000:8000 birdcall-recognition -e PORT="8000"
```

### Without Docker

Using a terminal, navigate to the `/app` subdirectory and run

#### On Linux/Unix/MacOS
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
waitress-serve --listen=0.0.0.0:8000 app:app
```

#### On Windows
```
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install -r requirements.txt
waitress-serve --listen=0.0.0.0:8000 app:app
```

Navigate to [http://0.0.0.0:8000](http://0.0.0.0:8000) to view the application.

## Repository Organization

This repository contains the source code used to train the model and build the web application.

- `app/` - The source code for the web application
  - `static/` - Static CSS and JavaScript files
  - `templates/` - Jinja2 template for landing page
  - `.dockerignore` - Files/directories to ignore when building Docker images
  - `Dockerfile` - Commands used to build Docker image
  - `app.py` - The Flask web application
  - `audio_utils.py` - Audio preprocessing functions
  - `predictor.py` - The classification model
  - `requirements.txt` - Python dependencies
  - `weights.py` - Pretrained model weights
- `deliverables/` - Deliverables submitted to bootcamp organizers
- `training/` - Contains the Jupyter notebook used to train the model
