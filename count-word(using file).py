def find_duplicate_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
            seen_words = set()
            duplicate_words = set()

            for word in words:
                if word in seen_words:
                    duplicate_words.add(word)
                else:
                    seen_words.add(word)
            
            print("Duplicate words found:")
            for word in duplicate_words:
                count = words.count(word)
                print(f"{word}: {count} occurrences")
            
            print("\n\nNon-duplicate words:")
            for word in seen_words - duplicate_words:
                count = words.count(word)
                print(f"{word}: {count} occurrences")
            
            if not duplicate_words and not seen_words:
                print("No words found in the file.")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Replace 'input.txt' with the actual file name
find_duplicate_words('input.txt')
