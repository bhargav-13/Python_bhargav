email = input("Enter Email: ")

index = email.index("@")

username = email[ : index]

domain = email[index + 1 :]

print(f"your usename is: {username}\nyour domain is: {domain}" )