import os
import zipfile
from pypdf import PdfReader

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIRECTORY, 'Resources')

def test_pdf_into_archive():

    archive_path = os.path.join(TMP_DIR,'archive_resources.zip')

    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        with zip_ref.open('file_pdf.pdf') as pdf_file_in_zip:
                pdf_content = PdfReader(pdf_file_in_zip)
                text_from_pdf = pdf_content.pages[0].extract_text()

                assert 'Тестовый PDF-документ' in text_from_pdf
