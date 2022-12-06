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
        print(y1)
        if x1 <= x2 and y1 >= y2:
            count = count + 1
        elif x2 <= x1 and y2 >= y1:
            count = count + 1
    print("The number of assignment pairs in which one fully contains the other is:", count)
