number_of_times_studied = 0
encouragement_count = 5

while number_of_times_studied <= 15:
    print("Student: Master I studied")
    number_of_times_studied += 1
    if number_of_times_studied % 5 != 0:
        continue
    print("Teacher: Good job")