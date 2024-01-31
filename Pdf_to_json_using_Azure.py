import json
import requests
import time

def concatenate_text(json_data):
    """
    Concatenate text from the current page.
    """
    extracted_text = ""
    for page in json_data.get("analyzeResult", {}).get("readResults", []):
        for line in page.get("lines", []):
            extracted_text += " ".join(word["text"] for word in line.get("words", [])) + "\n"
    return extracted_text

def send_pdf_to_azure_ocr(api_key, pdf_path):
    """
    Send PDF to Azure OCR and retrieve extracted text and JSON data.
    """
    # Azure OCR API endpoint
    api_url = "https://ocrassignmentinstance.cognitiveservices.azure.com/vision/v3.0/read/analyze"

    # Prepare headers with API key
    headers = {
        "Content-Type": "application/octet-stream",
        "Ocp-Apim-Subscription-Key": api_key,
    }

    # Initialize extracted text
    extracted_text = ""

    # Read the PDF file
    with open(pdf_path, "rb") as pdf_file:
        # Prepare the request payload
        files = {"file": pdf_file}

        # Make the API request
        response = requests.post(api_url, headers=headers, files=files)

        # Check if the request was successful (HTTP status code 202)
        if response.status_code == 202:
            # Retrieve the operation location from the response headers
            operation_location = response.headers.get("Operation-Location")

            # Poll for the status of the operation
            while True:
                time.sleep(5)  # Wait for 5 seconds before checking the status again
                status_response = requests.get(operation_location, headers=headers)

                if status_response.status_code == 200:
                    # The operation is completed, concatenate text from all pages
                    json_data = status_response.json()
                    extracted_text = concatenate_text(json_data)
                    break
                elif status_response.status_code == 202:
                    # The operation is still in progress, continue polling
                    continue
                else:
                    # Print the error message if the request failed
                    print(f"Error while polling status: {status_response.status_code} - {status_response.text}")
                    return None

    print("Successfully extracted text.")
    return extracted_text, json_data  # Return both extracted_text and json_data

# Replace 'YOUR_API_KEY' with your actual Azure OCR API key
api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Replace 'path/to/your/file.pdf' with the path to the PDF file you want to process
pdf_path = 'Christmas_Carol_Charles_Dickens.pdf'

# Send PDF to Azure OCR and get extracted text and JSON data
extracted_text, json_data = send_pdf_to_azure_ocr(api_key, pdf_path)

# Save the JSON data to a file
with open('result_json_azure.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=2)

# Comment out the print statement for extracted text
# print("Extracted Text:\n", extracted_text)
