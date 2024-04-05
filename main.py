import os


def read_file(input_file: str) -> str:
    """Reads the file and returns the text in lowercase.
    Args:
        input_file (str): The path to the file.
    Returns:
        str: The text in lowercase.
    """
    with open(input_file, 'r') as file:
        text = file.read().lower()
    return text


def count_words(words: list) -> dict:
    """Counts the number of occurrences of each word.
    Args:
        words (list): A list of words.
    Returns:
        dict: A dictionary with the words as keys and the number of
        occurrences as values.
    """
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


def get_top_of_words(word_count: dict, number_of_words: int = 10) -> tuple:
    """Returns the top n words in a tuple.
    Args:
        word_count (dict): A dictionary with the words as keys and the
        number of occurrences as values.
        number_of_words (int): The number of words to return.
    Returns:
        tuple: A tuple with the top n words.
    """
    sorted_word_count = sorted(word_count.items(),
                               key=lambda x: x[1],
                               reverse=True)
    top_of_words = sorted_word_count[:number_of_words]
    return top_of_words


def write_to_file(output_file: str, top_of_words: tuple) -> None:
    """Writes the top words to a file.
    Args: output_file (str): The path to the output file.
        top_of_words (tuple): A tuple with the top words.
    Returns:
        None
    """
    with open(output_file, 'w') as output:
        for word, count in top_of_words:
            output.write(f"{word}: {count}\n")


def main(input_file, output_file):
    """The main function. Reads the file, counts the words, gets the top"""
    text = read_file(input_file)

    words = text.split()
    word_count = count_words(words)

    top_of_words = get_top_of_words(word_count, 10)

    write_to_file(output_file, top_of_words)


if __name__ == '__main__':
    input_file = os.path.join('files', 'input.txt')
    output_file = os.path.join('files', 'output.txt')
    main(input_file, output_file)
