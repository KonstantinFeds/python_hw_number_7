import os.path
import zipfile

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIRECTORY, 'Resources')

def test_create_archive():

    if not os.path.exists(TMP_DIR):
        os.mkdir(TMP_DIR)
    with (zipfile.ZipFile(os.path.join(TMP_DIR, 'archive_resources.zip'),'w') as zf):
        for file in ['file_csv.csv',
                     'file_xlsx.xlsx',
                     'file_pdf.pdf']:
            add_file = os.path.join(CURRENT_DIRECTORY, file)
            zf.write(add_file,os.path.basename(add_file))















