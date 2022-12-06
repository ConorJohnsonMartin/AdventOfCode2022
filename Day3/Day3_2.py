if __name__ == '__main__':
    count = 0
    compartment1 = []
    compartment2 = []

    with open('Day3.txt', 'r') as infile:
        lines = [line for line in infile][:3]
        for line in lines:
            line.strip()
        print(lines)
    print("The sum of the priorities is:", count)
