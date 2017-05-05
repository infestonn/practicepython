def draw_board(row=3, col=3):
    for i in range(0, row):
        print(" ---"*col)
        print("|   "*(col + 1))
    print(" ---"*col)

if __name__ == "__main__":
    row = int(raw_input("Input number of rows: "))
    col = int(raw_input("Input number of columns: "))
    draw_board(row=row, col=col)
