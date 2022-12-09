if __name__ == '__main__':
    count = 0
    my_list = []
    temp_list = []

    file = open('Day3.txt', 'r')
    for line in file:
        x = str(line.strip())
        my_list.append(x)
    for i in range(100):
        temp_list = my_list[:3]
        for char in temp_list[0]:
            if char in temp_list[1] and char in temp_list[2]:
                if char.isupper():
                    count = count + ord(char) - 38
                elif char.islower():
                    count = count + ord(char) - 96
                break
        del my_list[:3]
        temp_list.clear()

    print("The sum of the priorities is:", count)
