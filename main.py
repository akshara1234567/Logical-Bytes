trys = int(input("enter number of tries : "))


if trys > 1000:
		print("ERROR,ERROR. TRY AGAIN LATER!!")

elif trys < 1:
	print("ERROR,ERROR. TRY AGAIN LATER!!")

else:
    for i in range (trys):
        X = int(input("enter amount to pay :"))

        if X > 1000:
             print("ERROR,ERROR. TRY AGAIN LATER!!")

        elif X < 1:
            print("ERROR,ERROR. TRY AGAIN LATER!!")

        else:
            coins = X%10
            print("You have to pay: ",coins,"coins")
            total = X//10
            print("TRY NUMBER",i + 1,":: You have to pay: ",total,"rupee notes and",coins,"coins")

