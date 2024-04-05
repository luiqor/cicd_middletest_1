import pytest
from main import count_words


@pytest.mark.parametrize(
    'words, expected_output',
    [
        (['hello', 'world', 'hello'], {'hello': 2, 'world': 1}),
        (['one', 'one', 'two', 'three', 'three', 'three'],
         {'one': 2, 'two': 1, 'three': 3}),
        ([], {}),
        (['single'], {'single': 1}),
        (['duplicate', 'duplicate'], {'duplicate': 2}),
    ],
)
def test_count_words(words, expected_output):
    assert count_words(words) == expected_output
