import fitz

class PDFHighlighter:
    def __init__(self, pdf_path):
        # Open the PDF document upon object initialization
        self.doc = fitz.open(pdf_path)

    def highlight_words(self, words_to_highlight, output_path='highlighted_output.pdf'):
        # Iterate through each page in the PDF
        for page_number in range(self.doc.page_count):
            page = self.doc[page_number]
            
            # Extract words information from the page
            words = page.get_text("words")

            # Iterate through each word on the page
            for word_info in words:
                word = word_info[4]

                # Check if the lowercase version of the word is in the lowercase words_to_highlight list
                if word.lower() in [w.lower() for w in words_to_highlight]:
                    # Create a rectangle using word_info and add a highlight annotation to the page
                    rect = fitz.Rect(word_info[:4])
                    highlight = page.add_highlight_annot(rect)

        # Save the modified PDF to the specified output path
        self.doc.save(output_path)

        # Close the PDF document
        self.doc.close()

# Example usage
pdf_path = 'Christmas_Carol_Charles_Dickens.pdf'
words_to_highlight = ['hi', 'this', 'hello', '23', 'I']

# Create a PDFHighlighter instance and highlight the specified words
highlighter = PDFHighlighter(pdf_path)
highlighter.highlight_words(words_to_highlight)
