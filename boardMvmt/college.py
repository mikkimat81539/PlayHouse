import random

class STATS:
	def __init__(self, name):
		self.name = name
		self.age = 18
		self.major = "undecided"
		self.debt = 0	

def scholarship():
	dice = random.randint(1, 20)
	if dice <= 10:
		print("You did not receive the scholarship reward.")
	elif 10 < dice <= 17:
		print("You received partial scholarship")

	else:
		print("You got a full ride scholarship")	
		

def loan(player, tuition):
	player.debt = tuition

	return tuition

def parents():
	dice = random.randint(1, 20)
	if dice <= 10:
		print("Your parents chose not to support you.")
	elif 10 < dice <= 17:
		print("Your parents agreed to pay half")

	else:
		print("Your parents covered the full cost of your tuition")	
 

def main():
	print("PLAYER STATS\n")

	player = STATS("Alex")

	tuition = 106000

	print(f"Name: {player.name}\n")
	print(f"Age: {player.age}\n")
	print(f"Major: {player.major}\n")
	print(f"Debt: {player.debt}\n")


	print("You graduate high school, and start college.\n")
	print("The tuition for university is $106,000.\n\nSelect your payment option.")

	print("-Apply for scholarship\n-Ask parents\n-Take out a loan\n")

	paymentOption = input("SELECT: Scholarship, Loan, Parents: ").upper()

	if paymentOption == "SCHOLARSHIP":
		scholarship()

	elif paymentOption == "LOAN":
		DEBT = loan(player, tuition)
		
		print(f"updated debt is {DEBT}")

	elif paymentOption == "PARENTS":
		parents()

	else:
		print("Invalid Input")

main()
