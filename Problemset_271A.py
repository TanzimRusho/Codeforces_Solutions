year = input()

while True:
    year = int(year)
    year += 1
    year = str(year)
    if year[0] != year[1] != year[2] != year[3]:
        print(year)
        break
