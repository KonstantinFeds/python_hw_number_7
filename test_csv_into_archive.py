import os
import csv
import zipfile

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIRECTORY, 'Resources')

def test_pdf_into_archive():

    archive_path = os.path.join(TMP_DIR,'archive_resources.zip')

    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        with zip_ref.open('file_csv.csv') as csv_file_in_zip:
            csv_content = csv_file_in_zip.read().decode('windows-1251')
            csv_reader = list(csv.reader(csv_content.splitlines(), delimiter=';'))
            second_row = csv_reader[0]
            assert second_row[0] == 'Январь'