	trys = int(input("enter number of tries"))

	for i in range trys:
		alice = int(input("Enter alice's height")	)
		bob = int(input("Enter bob's height"))

		if alice > bob:
    			print("A")

		elif bob > alice:
    			print("B")

		else:
   			 bob = alice
    			print("ERROR,ERROR. TRY AGAIN LATER!!")

		if alice,bob < 100:
			print("ERROR,ERROR. TRY AGAIN LATER!!")

		else:
			alice,bob > 200
			print("ERROR,ERROR. TRY AGAIN LATER!!")
