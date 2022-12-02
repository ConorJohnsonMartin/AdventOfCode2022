if __name__ == '__main__':
    points = 0

    elfList = list()
    file = open('day2.txt', 'r')
    for line in file:
        if "X" in line:
            points += 1
            if "A" in line:
                points += 3
            elif "C" in line:
                points += 6
        if "Y" in line:
            points += 2
            if "B" in line:
                points += 3
            elif "A" in line:
                points += 6
        if "Z" in line:
            points += 3
            if "C" in line:
                points += 3
            elif "B" in line:
                points += 6
    print(points)
