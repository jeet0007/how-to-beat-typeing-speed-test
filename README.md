# OCR and Text Input

This script uses optical character recognition (OCR) to extract text from a selected region of the screen, and then types the text using a virtual keyboard.

## Requirements

- Python 3.7 or later
- pytesseract 0.3.4 or later
- Pillow 7.1.2 or later
- pynput 1.7.1 or later

## Usage
1. Clone this repository and navigate to the project directory:
2. Run the script to install requirements
    ```bash
    pip install -r requirements.txt
    ```
4. Select the region of the screen to perform OCR on by moving mouse to the top-left corner of the region, 
5. Wait 5 seconds
6. If the extracted text is correct, press `y` to confirm. Otherwise, press `n` and repeat step 3.
7. The extracted text will be typed out using a virtual keyboard.

## Notes

- The script uses the `say` command to provide instructions for selecting the region of the screen to perform OCR on. This command is only available on macOS. If you are using a different operating system, you will need to modify the script to provide instructions in a different way.
- The script saves the screenshot of the selected region of the screen to a file named `screenshot.png` in the same directory as the script. This file is overwritten each time the script is run.
- The script uses the default OCR engine and language pack provided by pytesseract. You can specify a different OCR engine or language pack by setting the `pytesseract.pytesseract.tesseract_cmd` and `tessdata_dir_config` configuration values.
