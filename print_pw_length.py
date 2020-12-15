#Print Pw length

username = input('Enter the Username: \n')
password = input('Enter the Password: \n')

pw_length = len(password)
pw_masked = '*' * pw_length

print(f'Hey {username}, your password {pw_masked} is {pw_length} letters long')
