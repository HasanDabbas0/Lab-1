RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
GREEN = '\u001b[48;5;34m'
YELLOW = '\u001b[48;5;11m'
BLACK = '\u001b[48;5;16m'
END = '\u001b[0m'
if __name__ == '__main__':
    def draw_dual_romb(side = 8):
        
            for i in range(side):
                if i < side//2:
                    print(f'{"  "*(side-i)}{BLACK}{"  "*(i*2)}{END}{"  "*((side//2-i)-1)}{"  "*(side//2-i)}{BLACK}{"  "*(i*2)}{END}')
                if i >= side//2:
                    print(f'{"  "*(i)}{BLACK}{"  "*((side-i)*2)}{END}{"  "*((i-side//2)-1)}{"  "*(i-side//2)}{BLACK}{"  "*((side-i)*2)}{END}')
                    
                    
    draw_dual_romb(16)
