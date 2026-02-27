# Car Evaluation Prediction Application

This repository contains a **Flask** web app built during a Northeastern MSCS MLOps lab. It evaluates car designs using a decision‑tree model trained on the UCI Car Evaluation dataset. The model and `LabelEncoder` objects are serialized with **joblib** and live in `artifacts/model.pkl` and `artifacts/encoders.pkl` respectively. Pandas is used for DataFrame handling, and all dependencies are pinned in `requirements.txt` so the same environment can be recreated locally or inside Docker.

## Table of Contents
- [Setup Instructions](#setup-instructions)
- [Running the Application Locally](#running-the-application-locally)
- [Using Docker](#using-docker)
- [Screenshots](#screenshots)
- [Storing and Accessing Docker Images](#storing-and-accessing-docker-images)

---

## Setup Instructions

### Prerequisites
1. Install Python (>= 3.10).
2. Install Docker.
3. Clone this repository to your local machine.

### Install Dependencies
1. Navigate to the project directory:
   ```bash
   cd MLOps_Docker
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application Locally

1. Navigate to the `src` directory:
   ```bash
   cd src
   ```
2. Start the Flask application:
   ```bash
   python app.py
   ```
3. Open your browser and go to:
   ```
   http://localhost:4000
   ```
4. Use the dropdowns to input car features and click "Predict" to see the evaluation.

---

## Using Docker

### Build the Docker Image
1. Ensure Docker is running on your system.
2. Build the Docker image:
   ```bash
   docker build -t car-evaluation-app .
   ```

### Run the Docker Container
1. Run the container:
   ```bash
   docker run -p 4000:4000 car-evaluation-app
   ```
2. Open your browser and go to:
   ```
   http://localhost:4000
   ```

### Storing the Docker Image
1. Tag the Docker image for your Docker Hub repository:
   ```bash
   docker tag car-evaluation-app <your-dockerhub-username>/car-evaluation-app:latest
   ```
2. Push the image to Docker Hub:
   ```bash
   docker push <your-dockerhub-username>/car-evaluation-app:latest
   ```
3. The image will be available at:
   ```
   https://hub.docker.com/r/<your-dockerhub-username>/car-evaluation-app
   ```

---

## Screenshots

Below are screenshots captured during development; the original PNG files are in the `Screenshots/` directory.

1. **Home page** showing the form with dropdown lists generated directly from the saved label encoders:
   ![Form view](Screenshots/image43.png)

2. **Prediction result** displaying a sample output after submitting values:
   ![Prediction result](Screenshots/image.png)

3. **Docker container log** confirming the Flask app started inside the container:
   ![Docker run](Screenshots/image435.png)

4. **Build output** when constructing the image:
   ![Docker build](Screenshots/image467.png)

Feel free to swap or rename these images as needed; just update the links accordingly.

---

## Notes
- Ensure the `artifacts` folder contains the `model.pkl` and `encoders.pkl` files.
- If you encounter issues, check the console logs for debugging information.

