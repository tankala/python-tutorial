stars_count_list = [3, 1, 2, 4, 2]

for stars_count in stars_count_list:
    print("Level Started")
    for star_index in range(stars_count):
        print(f"Star {star_index+1} collected")
    print("Level completed. Congrats!!! You promoted to next level")