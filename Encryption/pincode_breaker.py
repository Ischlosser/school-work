def password_breaker():
    max = 122
    min = 97
    counter = 0
    pw_guess = "      "
    guess_list = list(str(pw_guess))
    password = input("Enter an 6 character password with ASCII characters only: ")
    while password.isascii() != True or len(password) != 6:
        password = input("Enter an 6 character password with ASCII characters only: ")
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
                            print(answer)
                            counter += 1
                            if answer == password:
                                print("The answer is " + answer)
                                print("Count: " + str(counter))
                                return

password_breaker()