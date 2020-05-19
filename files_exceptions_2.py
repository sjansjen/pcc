def count_words(filename):
    try:
        with open(filename, encoding="utf8") as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words")


filenames = ["alice.txt", "little_women.txt", "moby_dick.txt", "siddhartha.txt"]
for filename in filenames:
    count_words(filename)