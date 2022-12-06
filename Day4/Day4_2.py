import re

if __name__ == '__main__':
    count = 0
    file = open('Day4.txt', 'r')

    for line in file:
        new_line = str(line.strip())
        range_list = re.split(r',|-', new_line)
        x1 = int(range_list[0])
        y1 = int(range_list[1])
        x2 = int(range_list[2])
        y2 = int(range_list[3])
        range1 = range(x1-1, y1, 1)
        print(range1)
        range2 = range(x2-1, y2, 1)
        print(range2)
        for num in range1:
            if num in range2:
                count = count + 1
                break

    print("The number of assignment pairs in which the ranges overlap is:", count)
