import os
import tempfile
from pathlib import Path

from src.constants import EXTENTIONS
from src.IOHandler.find_files import find_files_in_directory


def test_find_files_in_directory_none_extentions():
    with tempfile.TemporaryDirectory() as temp_dir:
        test_files = ["test.pdf", "test.txt", "test.py", "other.doc"]
        for file in test_files:
            Path(temp_dir, file).touch()

        files = find_files_in_directory(directory=temp_dir, extentions=None)
        expected_files = [
            os.path.join(temp_dir, f)
            for f in test_files
            if any(f.endswith(ext) for ext in EXTENTIONS)
        ]
        assert set(files) == set(expected_files)
