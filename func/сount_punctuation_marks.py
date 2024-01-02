

def count_punctuation_marks(string):
    punctuation_marks = ['.', ',', ';', ':', '!', '?', '-', '—', '(', ')', '[', ']', '{', '}', '\"', '\'', '/', '\\', '»']
    count = {}

    for char in string:
        if char in punctuation_marks:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

    return count




