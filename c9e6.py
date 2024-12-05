def readWordsFromFile(filename):
    """ Read all words from the file and return them as a set, maintaining case sensitivity. """
    try:
        with open(filename, 'r') as file:
            # Read all lines, strip leading/trailing whitespace, and split by whitespace to get words
            words = set(file.read().strip().split())
        return words
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return set()

def main():
    # Filenames (replace 'file1.txt' and 'file2.txt' with your actual file names)
    filename1 = 'file1.txt'
    filename2 = 'file2.txt'

    # Read words from files
    wordsInFile1 = readWordsFromFile(filename1)
    wordsInFile2 = readWordsFromFile(filename2)

    # Perform set operations
    allUniqueWords = wordsInFile1.union(wordsInFile2)
    commonWords = wordsInFile1.intersection(wordsInFile2)
    wordsOnlyInFile1 = wordsInFile1.difference(wordsInFile2)
    wordsInOneButNotBoth = wordsInFile1.symmetric_difference(wordsInFile2)

    # Display the results
    print("All unique words from both files:")
    print(allUniqueWords)
    print("\nWords that appear in both files:")
    print(commonWords)
    print("\nWords that appear in the first file but not the second:")
    print(wordsOnlyInFile1)
    print("\nWords that appear in either the first or second file, but not both:")
    print(wordsInOneButNotBoth)

if __name__ == "__main__":
    main()
