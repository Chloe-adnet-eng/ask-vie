"Read pdf files."

from pathlib import Path

from pypdf import PdfReader

from src.constants import DOCS
from src.IOHandler.find_files import find_files_in_directory


def get_file_content(filename: str | Path) -> str:
    """Read the current pdf file."

    Args:
        - filename (str | Path): the pdf file to read

    Returns:
        - the content of the pdf file
    """
    reader = PdfReader(filename)
    content = ""
    for page in reader.pages:
        content += page.extract_text()
    return content


if __name__ == "__main__":  # pragma: no cover
    files = find_files_in_directory(DOCS)
    for filename in files:
        content = get_file_content(filename=filename)
        # print(content)
