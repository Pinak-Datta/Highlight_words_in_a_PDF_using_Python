# Introduction:

In this scenario, the task is highlighting specified words in a PDF document. 

**I have come up with two different approaches**. 

The **first approach utilizes a Python script with the PyMuPDF** library. 

The **second approach leverages Microsoft Azure OCR** (Optical Character Recognition) API Services. Both approaches aim to modify the PDF by highlighting or underlining particular words based on certain criteria.

# Approach 1: PyMuPDF Script

In the first approach, a Python script ([Without_using_Azure.py](https://github.com/Pinak-Datta/Highlight_words_in_a_PDF_using_Python/blob/main/Without_using_Azure.py)) is written using the PyMuPDF library to handle the PDF manipulation. 

The process involves:

### Initialization:

The script initializes a PDFHighlighter class, opening the specified PDF document using the PyMuPDF (fitz) library.

### Highlighting Words:

For each page in the PDF, the script extracts information about words on that page.
It iterates through each word and checks if it matches any of the specified words to highlight.
A highlight annotation is added to the PDF if a match is found.

The modified new PDF is saved as [highlighted_output_without_using_azure.pdf](https://github.com/Pinak-Datta/Highlight_words_in_a_PDF_using_Python/blob/main/highlighted_output_without_using_azure.pdf).

A glimpse of the new PDF:

<p align="center">
  <img src="https://i.imgur.com/JaAFv3I.png" alt="without_azure_pdf"  />
</p>

## Conclusion for Approach 1:

This approach is efficient for small to medium-sized PDFs.
It directly manipulates the PDF using a Python library without relying on external services.
Suitable for scenarios where manual control over the highlighting process is required.

# Approach 2: Using Azure OCR API

The second approach involves using Microsoft Azure OCR API services to extract text and information from the PDF, followed by modifying the PDF based on the extracted data. 

The process can be divided into two steps:

## PDF to JSON Conversion:

Using the [Pdf_to_json_using_Azure.py](https://github.com/Pinak-Datta/Highlight_words_in_a_PDF_using_Python/blob/main/Pdf_to_json_using_Azure.py) the PDF is sent to the Azure OCR API, and the extracted text and bounding box information of each word are obtained in JSON format.
The JSON data ([result_json_azure.json](https://github.com/Pinak-Datta/Highlight_words_in_a_PDF_using_Python/blob/main/result_json_azure.json)),  contains details about words and their positions on each page.

We save this JSON for future uses.

## Underlining Words using JSON information:

The script [Highlight_words_using_Json_from_OCR.py
](https://github.com/Pinak-Datta/Highlight_words_in_a_PDF_using_Python/blob/main/Highlight_words_using_Json_from_OCR.py) reads the JSON data that we previously generated using the API and iterates through the words.

For specified words to underline, it calculates the position (from the boundary values) just below the baseline and simulates underlining by adding rectangles to the PDF.

Finally, we also save the modified new pdf ([Underlined_using_Azure.pdf](https://github.com/Pinak-Datta/Highlight_words_in_a_PDF_using_Python/blob/main/Underlined_using_Azure.pdf)).

A glimpse of the new PDF:

<p align="center">
  <img src="https://i.imgur.com/MB21kg0.png" alt="without_azure_pdf"  />
</p>

## Conclusion for Approach 2:

This approach leverages cloud-based OCR services for text extraction, providing detailed information about words and their positions.
Suitable for scenarios where dynamic text extraction and manipulation are required.
Offers flexibility in handling large or complex PDF documents.

# Overall Summary:

**Approach 1 is a straightforward and direct method using a Python library** for PDF manipulation.

**Approach 2 showcases the power of cloud-based OCR services, offering detailed information** about the PDF content.

The **choice between the approaches depends on the specific requirements of the task, such as manual control, scalability, and the need for advanced text extraction capabilities.** Both approaches successfully modify the PDF to highlight or underline specified words, providing flexibility in addressing different use cases.
