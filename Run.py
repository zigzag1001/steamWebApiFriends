import getDataAndWrite, findUser

choice = input("1 - getDataAndWrite\n2 - findUser\n")

if choice == "1":
	getDataAndWrite.main()
elif choice == "2":
	findUser.main()
else:
	print("haha poop")