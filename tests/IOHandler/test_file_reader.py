from src.IOHandler.file_reader import get_file_content


def test_get_file_content_():
    filename = "docs/mock.pdf"
    content = get_file_content(filename=filename)
    content = " ".join(content.strip().split())
    assert content == "Mock file February 11, 2026"
