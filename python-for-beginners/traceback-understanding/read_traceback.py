def print_sequential(number):
    for num in range(1, number+1):
        print(num)

def main():
    stop = int(input("Give me a number until that you want to print numbers sequentially: "))
    print_sequential(stop)

main()