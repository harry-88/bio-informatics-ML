# Sequence Classifier

This is a Python Flask web application that classifies sequences using a Support Vector Machine (SVM) model. It takes a sequence as input and returns the predicted classification result.

## Requirements

- Python 3.x
- Flask
- BioPython
- Flask-CORS
- NumPy
- scikit-learn

## Installation

1. Clone the repository or download the source code files.
2. Open a terminal or command prompt and navigate to the project directory.

   ```
   cd sequence-classifier
   ```

5. Install the required packages by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install all the necessary packages specified in the `requirements.txt` file.

6. Start the Flask server by running the following command:

   ```
   python app.py
   ```
   The server should start running on `http://localhost:5000`.

7. Open your web browser and navigate to `http://localhost:5000` to access the Sequence Classifier application.

## Usage

1. Enter a sequence in the text area provided on the web page.
2. Click the "Classify" button to submit the sequence for classification.
3. The predicted classification result will be displayed below the text area.

## Notes

- The Flask server runs in debug mode (`debug=True`) for development purposes. You may want to change this configuration when deploying the application in a production environment.
- Ensure that the `sequance.txt` file exists in the same directory as the `app.py` file, and it contains the valid sequence data in the FASTA format.
- The application uses Bootstrap CSS for styling and requires an internet connection to load the Bootstrap stylesheet from a CDN. If you want to use a local copy of the Bootstrap CSS, you can update the `<link>` tag in the HTML file accordingly.

Feel free to modify the application to suit your needs, such as customizing the styling, integrating with a different model, or expanding its functionality.