def longest_c_word(filename):
    """Find and return the longest word starting with 'c' in a text file"""

    punctuation = ",.;:!?\"'()[]{}-*<>"
    longest = ""

    with open(filename) as fd:
        for line in fd:
            # strip punctuation by replacing each punctuation character with a space
            for p in punctuation:
                line = line.replace(p, " ")

            words = line.split()

            for word in words:
                # check if word starts with 'c' or 'C' and is longer than current longest
                if word.lower().startswith("c") and len(word) > len(longest):
                    longest = word

    return longest


print(longest_c_word("text.txt"))
