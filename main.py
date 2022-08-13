alice = int(input("Enter alice's height"))
bob = int(input("Enter bob's height"))

if alice > bob:
    print("A")

elif bob > alice:
    print("B")

else:
    bob = alice
    print("ERROR,ERROR. TRY AGAIN LATER!!")
