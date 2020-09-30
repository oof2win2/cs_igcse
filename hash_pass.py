passwd = input("real password: ")
print(f"The hash of '{passwd}' is '{hash(passwd)}'")
while True:
	attempt = input("attempt password: ")
	print(f"the hash of '{attempt}' is '{hash(attempt)}'")
	if hash(attempt) == hash(passwd):
		print(f"the hash of {attempt} is equal to the hash of {passwd}, therefore the passwords are equal")
		break
	else:
		print("hashes are not the same. please try again")

