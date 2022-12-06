if __name__ == '__main__':
    count = 0
    compartment1 = []
    compartment2 = []
    file = open('Day3.txt', 'r')
    for line in file:
        new_line = str(line.strip())
        compartment_size = len(new_line) // 2
        compartment1 = new_line[0:compartment_size]
        compartment2 = new_line[compartment_size:len(new_line)]
        for char in compartment1:
            if char in compartment2:
                if char.isupper():
                    count = count + ord(char)-38
                elif char.islower():
                    count = count + ord(char)-96
                break
    print("The sum of the priorities is:", count)
    