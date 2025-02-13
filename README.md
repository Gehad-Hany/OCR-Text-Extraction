# OCR Text Extraction App 📝

This is a simple OCR (Optical Character Recognition) text extraction application built using Streamlit and EasyOCR. The app allows users to upload an image containing numbers, and the model will extract the text from the image.

## Features

- Upload an image in PNG, JPG, or JPEG format.
- Display the uploaded image.
- Extract text from the image using EasyOCR.
- Display the extracted text.
- Download the extracted text as a `.txt` file.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/ocr-text-extraction-app.git
    cd ocr-text-extraction-app
    ```

2. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

    Make sure your `requirements.txt` includes the following packages:

    ```
    streamlit
    easyocr
    pillow
    numpy
    ```

## Usage

1. Run the Streamlit app:

    ```sh
    streamlit run [project2_cv.py](http://_vscodecontentref_/0)
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload an image containing numbers.

4. Wait for the model to extract the text.

5. View the extracted text and download it as a `.txt` file.

## File Structure

- `project2_cv.py`: The main application file.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [Pillow](https://python-pillow.org/)
- [NumPy](https://numpy.org/)

## License

This project is licensed under the MIT License.