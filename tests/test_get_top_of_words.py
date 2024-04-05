import pytest
from main import get_top_of_words


@pytest.mark.parametrize(
    'word_count, number_of_words, expected_output',
    [
        ({'hello': 2, 'world': 1}, 2, [('hello', 2), ('world', 1)]),
        ({'one': 2, 'two': 1, 'three': 3}, 2, [('three', 3), ('one', 2)]),
        ({'one': 2, 'two': 1, 'three': 3}, 1, [('three', 3)]),
        ({}, 10, []),
    ],
)
def test_get_top_of_words(word_count, number_of_words, expected_output):
    assert get_top_of_words(word_count, number_of_words) == expected_output
