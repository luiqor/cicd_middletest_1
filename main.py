def read_file(input_file: str) -> str:
    with open(input_file, 'r') as file:
        text = file.read().lower()
    return text


def count_words(words: list) -> dict:
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


def get_top_of_words(word_count: dict, number_of_words: int = 10) -> tuple:
    sorted_word_count = sorted(word_count.items(),
                               key=lambda x: x[1],
                               reverse=True)
    top_of_words = sorted_word_count[:number_of_words]
    return top_of_words


def write_to_file(output_file: str, top_of_words: tuple) -> None:
    with open(output_file, 'w') as output:
        for word, count in top_of_words:
            output.write(f"{word}: {count}\n")


def main(input_file, output_file):
    text = read_file(input_file)

    words = text.split()
    word_count = count_words(words)

    top_of_words = get_top_of_words(word_count, 10)

    write_to_file(output_file, top_of_words)


if __name__ == '__main__':
    main('input.txt', 'output.txt')
