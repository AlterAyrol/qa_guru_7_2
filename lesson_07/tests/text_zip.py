import os
import zipfile
from conftest import RESOURCES_DIR


def test_zip_file_list():
    with zipfile.ZipFile(os.path.join(RESOURCES_DIR, 'resources.zip')) as zip_file:
        filenames = [i.filename for i in zip_file.filelist]

    assert filenames == ['file_example_XLSX_50.xlsx', 'docs-pytest-org-en-latest.pdf', 'file_example_XLS_10.xls']
