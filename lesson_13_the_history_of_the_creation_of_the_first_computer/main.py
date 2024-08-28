import pdfplumber as plumber
from gtts import gTTS

def get_single_line_text():
    file_name = "text.pdf"
    with plumber.open(file_name) as pdf_file:
        extracted_text = [page.extract_text() for page in pdf_file.pages]
        pdf_text = " ".join(extracted_text)
        single_line_text = pdf_text.replace("\n", " ")
    return single_line_text


def get_text_to_audio(pdf_file):
    language = "ru"
    audio = gTTS(text=pdf_file, lang=language, slow=False)
    audio.save("audio.mp3")


def main():
    pdf_file = get_single_line_text()
    get_text_to_audio(pdf_file)
    
if __name__ == "__main__":
    main()