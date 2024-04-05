import os
import pytest


@pytest.fixture(autouse=True)
def prepare_text_file(tmp_path):
    target_file = os.path.join(tmp_path, 'test.txt')
    with open(target_file, 'w') as file:
        lines = ["Hello world dear python\n",
                 "Hello world dear python\n",
                 "Hello world dear\n",
                 "Hello world\n",
                 "Hello world\n",
                 "Hello world\n",
                 "Bb world",]
        file.writelines(lines)
    return target_file


@pytest.fixture(autouse=True)
def prepare_output_file(tmp_path):
    return os.path.join(tmp_path, 'output.txt')
