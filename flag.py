GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
RED = '\u001b[41m'
END = '\u001b[0m'

rows = 10
cols = 30 


for _ in range(rows):
    if _ < rows // 2:
        print(GREEN + "  " * (cols // 3) + YELLOW + "  " * (2 * cols // 3) + END)
    else:
        print(GREEN + "  " * (cols // 3) + RED + "  " * (2 * cols // 3) + END)