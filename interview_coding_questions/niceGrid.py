def niceGrid(R, C):
    grid = [[0 for i in range(15)] for j in range(15)]
    for row in range(1, 15, 2):
        for col in range(1, 15, 2):
            if col >= row and col <= 15 - 1 - row and row % 2 == 1 and col % 2 == 1:
                grid[row][col] = 1
    print(grid)
    if grid[int(R)-1][int(C)-1] == 0:
        print('black')
    else:
        print('white')

if __name__ == "__main__":
    A, B = input().split()
    niceGrid(A, B)