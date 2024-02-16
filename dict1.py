#1 write a program that needs a sentence and counts the number of times each word appears. 
#use a dictionary to store the word counts. 
def count_words(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Create an empty dictionary to store word counts
    word_counts = {}

    # Count the occurrences of each word
    for word in words:
        # Convert the word to lowercase to ensure case-insensitivity
        word = word.lower()

        # Update the word count in the dictionary
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

# Get input sentence from the user
input_sentence = input("Enter a sentence: ")

# Call the function to count words
result = count_words(input_sentence)

# Display the word counts
for word, count in result.items():
    print(f"{word}: {counts}")
