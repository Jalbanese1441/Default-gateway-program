import os
import os.path
cls= lambda: os.system("cls")

# READ ME: The problem is that this program is using command prompt to access your network information.
# This can be flagged as a virus because it open command prompt, also depending on your computer, you may need to be in an admin account to open the command prompt.

def networkInfoFinder():
		file=open("Cmd Launcher Code.bat","w+") # Cerates the bat file that will be used to open cmd 
		file.write("start cmd /k ipconfig") 
		#This adds in the code. The language that I used here is DOS batch language. Which I taught my self in grade 9, it can’t do much, but it is useful for these applications
		file.close()
		os.startfile("Cmd Launcher Code.bat") # This opens the file
		cls()
		print("Press enter to be taken back to the stat or type e to exit the program.")
		print("Note: You will have to close the other window manually.")
		q=input()
		if q=="e": exit(0)

while True:# This keeps the program running 
	while True: # This keeps the user in a loop until they enter a valid ip address
		cls()
		print("Note: Please run this program in full screen mode\n")
		print("Welcome to the default gateway finder. In simple terms your default gateway makes it possible for devices on your network to communicate with devices on another network")
		print("Enter your IP V4 address below (then press enter) and it will be verified, then the computer will print out your default gateway")
		print("Note: If you have customised your network this may be different\nOr type e to exit\n")
		print("Alternatively, if you don’t know a thing about you network type in \"a\" and press enter and the program will find it al for you.\nNote: this may not work on some computers and you should read the comments in my code for a better explanation. ")
		possibleIp= input()
		if possibleIp=="a":
		   networkInfoFinder()
		   continue #  This ignores the  rest of the code in the loop and makes it restart
		if possibleIp=="e": exit(0) #Closes the program
		if len(possibleIp) >=8 and len(possibleIp) <=12:
			if possibleIp.replace(".","",3).isnumeric()==True:
		#This bit checks the ip against some standard rules, yes I realise that it can get more specific but this is a basic version and not designed to pick out custom network configurations
				break
			else:
				cls()
				print(possibleIp, "Is not a valid ip address, press enter to be taken back to the start")
				input()
		else:				
			cls()
			print(possibleIp, "Is not a valid ip address, press enter to be taken back to the start")
			input()
	cls()
	print("You entered a correct ip address, press enter to see the information")
	input()
	cls()
	print("Your device ip is:",possibleIp)
	print("Your default gateway is one of the addresses in this list:\n")
	#print(possibleIp,"Is a valid ip address")
	ipParts=possibleIp.split(".")# Breaks up the string at each “.”
	#print(ipParts[3])
	for i in range(25): 
		if i ==int(ipParts[3]): continue
		print(ipParts[0]+"."+ipParts[1]+"."+ipParts[2]+"."+str(i)) 
		#This recombines the string and adds in its new ending. As far as I know a default gateway can be between 0 and 24 and needs it’s own address (so no sharing end digits).
	print("\nNow that you have tried the basic version of the program, would you like to try the advanced version of this program?")
	print("Note: Depending on your computer’s firewall and account privilege, this may not work, if this happens please read my comments.")
	print("Type y to aces the advanced version, type n to go back to the start, or type e to exit (press enter after)")
	x=input()
	if x=="e": exit(0) # Closes the program
	if x=="y":
		cls()
		print("Good choice! I was hoping that you would try this. Once you press enter a window containing all of you network information should pop up. If it does not please read my comments in the code.")
		input()
		networkInfoFinder()


