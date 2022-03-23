def removeDuplicatesFromFile(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    lines = dict.fromkeys(lines)

    BookURLsFile = open(file_name, "w")
    BookURLsFile.write("")
    BookURLsFile.close()

    BookURLsFile = open(file_name, "a")
    for line in lines:
        BookURLsFile.write(line)

    BookURLsFile.close()
    print(f"Duplicate lines removed from{file_name}")
    print("**Please check that the last line in the file is not a duplicate\n")
    
removeDuplicatesFromFile("stats.txt")
