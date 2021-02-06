notes = [2000, 500, 200, 100]
withdrawl_amount = int(input("Please Enter Amount: "))

for note in notes:
    # We need whole number that's why we need to convert number of votes to integer
    number_of_notes = int(withdrawl_amount / note)
    remaining_amount = withdrawl_amount % note
    # If the number of notes equal to zero then there is no point of printing that's why we are printing the notes which are not equal to 0
    if number_of_notes != 0:
        print(f"{number_of_notes} note(s) of {note}")
    if remaining_amount == 0:
        break
    else:
        withdrawl_amount = remaining_amount