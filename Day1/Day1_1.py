if __name__ == '__main__':
    count = 0
    elfList = list()
    file = open('day1.txt', 'r')

    for line in file:
        if not line.isspace():
            count += int(line)
        if line.isspace():
            elfList.append(count)
            count = 0

    elfList.sort()
    print("Largest element is:", elfList[-1])