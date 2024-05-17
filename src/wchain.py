def find_the_longest_chain(words):
    dp_chain_length = {}

    for word in words:
        dp_chain_length[word] = 1
    words_sorted_by_length = sorted(words, key=len)

    for word in words_sorted_by_length:
        for i in range(len(word)):
            previous = word[:i] + word[i+1:]
            if previous in dp_chain_length:
                new_length = dp_chain_length[previous] + 1
                if new_length > dp_chain_length[word]:
                    dp_chain_length[word] = new_length

    return max(dp_chain_length.values())

def read_file_from_input(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        if not lines:
            raise ValueError("file are empty")
        N = int(lines[0].strip())
        if not (1 <= N <= 10**5):
            raise ValueError("incorrect number of words")
        else:
            words = [line.strip() for line in lines[1:N+1]]
            for word in words:
                if not (1 <= len(word) <= 50):
                    raise ValueError('incorrect word length')
                if not word.islower() or not word.isalpha():
                    raise ValueError('incorrect word')
    return words

def result_file(output_file, result):
    with open(output_file, 'w') as file:
        file.write(str(result))