def read_file(input_file: str) -> str:
    with open(input_file, 'r') as file:
        text = file.read().lower()
    return text


def count_words(words: str) -> dict:
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


def get_top_10_words(word_count: dict, number_of_words: int = 10) -> dict:
    pass


def write_to_file(output_file: str, top_10_words: dict) -> None:
    with open(output_file, 'w') as output:
        for word, count in top_10_words:
            output.write(f"{word}: {count}\n")


def main(input_file, output_file):
    text = read_file(input_file)

    words = text.split()
    word_count = count_words(words)

    top_10_words = get_top_10_words(word_count, 10)

    write_to_file(output_file, top_10_words)


if __name__ == '__main__':
    main('input.txt', 'output.txt')
