def count_names(filename):
    try:
        with open(filename, 'r') as file:
            names = file.readlines()
            num_names = len(names)
            print("Number of names in the file:", num_names)
    except IOError:
        print("Error: File not found or could not be opened.")


count_names("names.txt")
