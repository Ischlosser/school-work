skirrrt = input("Enter a sentence: ")
n = len(skirrrt)
k = skirrrt.count(' ')

print("Length: " + str(n))
print("Length without space:" + str(n-k))
print(skirrrt.upper())
print("First Character: "+ str(skirrrt[:1]))
print("Last Character: "+ str(skirrrt[n-1:]))
