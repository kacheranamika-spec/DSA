for i in range(1, 6):
    if i == 3:
        continue

    for j in range(10, 5, -1):
        if j == 8:
            continue

        if i + j == 11:
            print(i, j)