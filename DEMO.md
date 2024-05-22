# Demo

This document provides a step-by-step demonstration of how to use the Blood Cancer Detection Web App.

## Step 1: Launch the App

Run the Streamlit app using the command `streamlit run app.py`. The app will open in your default web browser.

## Step 2: Upload an Image

On the app's main page, you'll see a file uploader. Click "Browse files" and select an image of a blood smear from your computer. The image should be in JPEG format and ideally 64x64 pixels in size.

## Step 3: View the Prediction

After you've uploaded an image, the app will process the image and feed it into the trained CNN model. The model will predict the likelihood of the image indicating blood cancer.

The prediction result will be displayed on the app. If the predicted probability is greater than 0.5, the app will display "Blood Cancer Detected" along with the predicted probability. Otherwise, it will display "Blood Cancer Not found".

## Step 4: Upload a Different Image (Optional)

If you want to test the app with a different image, simply click "Browse files" again and select a new image. The app will process the new image and display the new prediction result.

That's it! You've now seen how to use the Blood Cancer Detection Web App. If you have any questions or encounter any issues, please check the FAQ or open an issue on GitHub.
