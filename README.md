# Face Detection Website

This project is a simple face detection web application built with Python, Flask, and OpenCV. Users can upload images through a web interface, and the app detects faces in the images and highlights them with rectangles.

## Features

- Upload images via a web form.
- Detect faces using OpenCV's Haar Cascade classifier.
- Display the processed image with detected faces highlighted.
- Simple and clean user interface.

## Project Structure

- `app.py`: Main Flask application with face detection logic.
- `templates/index.html`: HTML template for the frontend.
- `requirements.txt`: Python dependencies.
- `uploads/`: Directory where uploaded images are saved (not included in Git).
- `static/detected/`: Directory where processed images with detected faces are saved (not included in Git).
- `.gitignore`: Specifies files and folders to exclude from Git.

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. (Optional but recommended) Create and activate a Python virtual environment (Python 3.10 recommended):

   ```bash
   python -m venv face_detection_env
   face_detection_env\Scripts\activate   # On Windows
   source face_detection_env/bin/activate  # On macOS/Linux
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Run the Flask app with:

```bash
python app.py
```

The app will start on `http://127.0.0.1:5000`. Open this URL in your browser to access the face detection website.

## Usage

- Upload an image file using the form on the homepage.
- The app will process the image and display it with detected faces highlighted.
- Supported image formats include common types like JPG, PNG, etc.

## Notes

- Uploaded and processed images are saved locally in the `uploads/` and `static/detected/` folders respectively.
- These folders are excluded from version control via `.gitignore`.
- This app is intended for development and testing purposes. For production deployment, consider using a production-ready WSGI server.

## License

This project is open source and available under the MIT License.
