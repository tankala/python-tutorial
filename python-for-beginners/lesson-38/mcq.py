#Please install openpyxl package before running this program

from test_organizer import start_test_and_give_score

user_name = input("Please give your name: ")
score = start_test_and_give_score()
print(f"Hey {user_name}, You got {score} in test")