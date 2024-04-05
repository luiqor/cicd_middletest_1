from main import read_file


def test_read_file(prepare_text_file):
    expected_output = (
        "hello world dear python\n"
        "hello world dear python\n"
        "hello world dear\n"
        "hello world\n"
        "hello world\n"
        "hello world\n"
        "bb world"
    )
    assert read_file(prepare_text_file) == expected_output
