def height():
	trys = int(input("enter number of tries"))
	if trys > 1000:
		print("ERROR,ERROR. TRY AGAIN LATER!!")
	elif trys < 1:
		print("ERROR,ERROR. TRY AGAIN LATER!!")
	else:
		for i in range (trys):
			alice = int(input("Enter Alice's height"))
			if alice < 100:
				print("ERROR,ERROR. TRY AGAIN LATER!!")
				break
			elif alice > 200:
				print("ERROR,ERROR. TRY AGAIN LATER!!")
				break
			else:
				bob = int(input("Enter Bob's height"))
			if bob < 100:
					print("ERROR,ERROR. TRY AGAIN LATER!!")
					break
			elif  bob > 200:
				print("ERROR,ERROR. TRY AGAIN LATER!!")
				break
			elif bob == alice:
				print("ERROR,ERROR. TRY AGAIN LATER!!")
				break
			else:
				if alice > bob:
  						print("A")

				else:
						bob > alice
						print("B")

height()
