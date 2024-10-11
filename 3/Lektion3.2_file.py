# file = open("log.txt", 'r')
# print(file.read())

def search_attempt(filename, word = "Failed login attempt"):
    with open("log.txt", 'r') as file: #'r' is for reading the file
        attempt = file.readlines() # Read the file line by line
        for i, line in enumerate(attempt, start=1):
            if word in line:
                print("**************")               
                print(f"The log {word} was found in line {i}.\nHere's how it looks like: \n{line.strip()}")# Strip removes trailing newlines
                print("**************")
search_attempt("log.txt")  # This will search for "Failed login attempt"


#Another method without enumerate:
# def search_attempt(filename, word="Failed login attempt"):
#     with open(filename, 'r') as file:
#         line_number = 1  # Manual line counter
#         for line in file:  # Iterating over the file object directly
#             if word in line:  # Check if the word is in the current line
#                 print(f"The log '{word}' was found in line {line_number}")
#             line_number += 1  # Increment the line number after each iteration

#another method with re
# import re

# def search_attempt(filename, pattern="Failed login attempt"):
#     with open(filename, 'r') as file:
#         line_number = 1
#         for line in file:
#             if re.search(pattern, line):  # Using regex search
#                 print(f"The pattern '{pattern}' was found in line {line_number}")
#             line_number += 1