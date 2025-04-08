from collections import Counter

def word_count(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            words = text.split()
            word_counts = Counter(words)
            for word in sorted(word_counts):
                print(f"{word}: {word_counts[word]}")
    except FileNotFoundError:
        print("File not found. Make sure the file path is correct.")

# Example usage
file_path = input("Enter the text file path: ")
word_count(file_path)
