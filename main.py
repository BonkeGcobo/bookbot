def countChars(file_contents):
    charsDict = {chr(char): 0 for char in range(ord('a'), ord('z')+1)}
    lowered_string = file_contents.lower()
    for char in charsDict:
        count = file_contents.count(char)
        charsDict[char]=count

    sorted_dict = dict(sorted(charsDict.items()))    
    return sorted_dict

def countWords(textFromBook):
    return len(textFromBook.split())

def sortByOccurances(charsDict):
    for char in charsDict:
        print("The",char,"character was found",charsDict[char],"times")
           

def main():
    print ("--- Begin report of books/frankenstein.txt ---")
    print("")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(countWords(file_contents)," words found in the document")
        print("")
        charsReport=countChars(file_contents)
        sorted_dict = dict(sorted(charsReport.items(), key=lambda x: x[1], reverse=True))

        print(sortByOccurances(sorted_dict))
        print("")
        print("--- End report ---")


main()