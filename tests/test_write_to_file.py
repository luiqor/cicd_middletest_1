from main import write_to_file


def test_write_to_file(prepare_output_file):
    top_of_words = [("hello", 2), ("world", 1)]
    expected_output = "hello: 2\nworld: 1\n"

    write_to_file(prepare_output_file, top_of_words)

    with open(prepare_output_file, 'r') as file:
        actual_output = file.read()

    assert actual_output == expected_output
