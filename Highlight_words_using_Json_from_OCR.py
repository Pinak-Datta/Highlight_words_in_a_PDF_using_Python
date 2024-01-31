import fitz  
import json


def underline_words(pdf_path, json_data, words_to_underline, output_path):
    """
    Underline specified words in a PDF based on JSON data.
    """
    doc = fitz.open(pdf_path)

    for page_number in range(len(doc)):
        page = doc[page_number]

        for line_info in json_data["analyzeResult"]["readResults"][page_number]["lines"]:
            for word_info in line_info["words"]:
                word_text = word_info["text"]
                bounding_box = word_info["boundingBox"]

                # Check if the word in JSON data matches any word in the list to underline
                if word_text in words_to_underline:
                    x0, y0, x1, y1 = [coord * 72 for coord in
                                      bounding_box[:4]]  # Convert to points (1 inch = 72 points)

                    # Calculate the position just below the baseline
                    underline_y = y1 + 10  # Adjust this value for proper positioning

                    # Draw a filled rectangle just below the baseline to simulate underlining
                    page.draw_rect(fitz.Rect(x0, underline_y, x1, underline_y + 1), color=(1, 0, 0))

    doc.save(output_path)
    doc.close()


if __name__ == "__main__":
    
    # Declarations
    json_file_path = 'result_json_azure.json'
    pdf_file_path = 'Christmas_Carol_Charles_Dickens.pdf'
    output_path = 'Underlined_using_Azure.pdf'

    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    words_to_underline = ["I", "This", "12", "hi", "The"]  # Replace with your array of strings of your choice

    underline_words(pdf_file_path, json_data, words_to_underline, output_path)
