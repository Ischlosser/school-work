def palindromeChecker():
    sentence = input("Input your sentence: ")
    sentence = sentence.lower()
    sentence = sentence.replace(" ", "")
    for i in range(48):
        sentence = sentence.replace(chr(i), "")
    for i in range(58, 65):
        sentence = sentence.replace(chr(i), "")
    for i in range(94, 97):
        sentence = sentence.replace(chr(i), "")
    if sentence[::-1] == sentence:
        print("This is a palindrome.")
    else:
        print(f"{sentence} is not a palindrome.")

while True:
    palindromeChecker()