import time

def passcode_breaker():
    start = time.time()
    max = 57
    min = 48
    counter = 0
    pw_guess = "      "
    guess_list = list(str(pw_guess))
    password = input("Enter an 6 digit passcode: ")
    while password.isdigit() != True or len(password) != 6:
        password = input("Enter an 6 character password with digits only: ")
    for i1 in range(min, max+1):
        guess_list[0] = chr(i1)
        for i2 in range(min, max+1):
            guess_list[1] = chr(i2)
            for i3 in range(min, max+1):
                guess_list[2] = chr(i3)
                for i4 in range(min, max+1):
                    guess_list[3] = chr(i4)
                    for i5 in range(min, max+1):
                        guess_list[4] = chr(i5)
                        for i6 in range(min, max+1):
                            guess_list[5] = chr(i6)
                            answer = ''.join(guess_list)
                            #print(answer)
                            counter += 1
                            if answer == password:
                                end = time.time()
                                print("The answer is " + answer)
                                print("Count: " + str(counter))
                                print("Time: " + str(end - start))
                                return answer



def password_breaker():
    start = time.time()
    max = 122
    min = 48
    counter = 0
    pw_guess = "        "
    guess_list = list(str(pw_guess))
    password = input("Enter an 8 character password: ")
    while password.isascii() != True or len(password) != 8:
        password = input("Enter an 8 character password with ASCII characters only: ")
    for i1 in range(min, max+1):
        guess_list[0] = chr(i1)
        for i2 in range(min, max+1):
            guess_list[1] = chr(i2)
            for i3 in range(min, max+1):
                guess_list[2] = chr(i3)
                for i4 in range(min, max+1):
                    guess_list[3] = chr(i4)
                    for i5 in range(min, max+1):
                        guess_list[4] = chr(i5)
                        for i6 in range(min, max+1):
                            guess_list[5] = chr(i6)
                            for i7 in range(min, max+1):
                                guess_list[6] = chr(i7)
                                for i8 in range(min, max+1):
                                    guess_list[7] = chr(i8)
                                    answer = ''.join(guess_list)
                                    #print(answer)
                                    counter += 1
                                    if answer == password:
                                        end = time.time()
                                        print("The answer is " + answer)
                                        print("Count: " + str(counter))
                                        print("Time: " + str(end - start))
                                        return answer
x = int(input("Would you like to crack a passcode(0) or a password(1)? "))
if x == 0:
    print(passcode_breaker())
elif x == 1:
    print(password_breaker())
else:
    print("error")