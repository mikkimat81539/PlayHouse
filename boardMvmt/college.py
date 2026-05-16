import random

def scholarship():
	dice = random.randint(1, 20)
	print(dice)	
	if dice <= 10:
		print("You did not receive the scholarship reward.")
	elif 10 < dice <= 15:
		print("You received partial scholarship")

	else:
		print("You got a full ride scholarship")	
		


def main():
	print("You graduate high school, and start college.\n")
	print("The tuition for university is $106,000.\n\nSelect your payment option.")

	print("-Apply for scholarship\n-Ask parents\n-Take out a loan\n")

	paymentOption = input("SELECT: Scholarship, Loan, Parents: ").upper()

	if paymentOption == "SCHOLARSHIP":
		scholarship()

	elif paymentOption == "LOAN":
		pass

	elif paymentOption == "PARENTS":
		pass

	else:
		print("Invalid Input")

main()
