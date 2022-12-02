if __name__ == '__main__':
    points = 0

    elfList = list()
    file = open('day2.txt', 'r')
    for line in file:
        if "X" in line:
            if "A" in line:
                points += 3
            if "B" in line:
                points += 1
            if "C" in line:
                points += 2
        if "Y" in line:
            points += 3
            if "A" in line:
                points += 1
            if "B" in line:
                points += 2
            if "C" in line:
                points += 3
        if "Z" in line:
            points += 6
            if "A" in line:
                points += 2
            if "B" in line:
                points += 3
            if "C" in line:
                points += 1
    print(points)
