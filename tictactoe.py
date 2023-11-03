###
# Tanggal Dibuat: 18/08/2023
# Author: FandyFr
# APP Version: v0.2
###

import os
import time
import webbrowser
os.system('cls' if os.name == 'nt' else 'clear')

time.sleep(3)
print("Loading data...")
time.sleep(5)

os.system('cls' if os.name == 'nt' else 'clear')

print("+=============================================+")
print(" APP BUATAN FANDY FATHURROHMAN")
print("*")
print("DIKEMBANGKAN MELALUI BAHASA PYTHON")
print("*")
print("JANGAN LUPA FOLLOW GITHUB SAYA: Fandyfr")
print("+=============================================+")

url='https://github.com/fandyfr'

webbrowser.open_new(url)

time.sleep(15)

os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(5)
print("Memuat Game...")
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(2)

square = [0,1,2,3,4,5,6,7,8,9]
def main():
    player = 1
    status = -1

    while status== -1:
        papan()
        
        if player%2 == 1:
            player = 1
        else:
            player = 2

        print('\nPlayer', player)
        choice = int(input('Pilih Angka Berapa:'))

        if player == 1:
            mark = 'X'
        else:
            mark = 'O'

        if choice == 1 and square[1] == 1:
            square[1] = mark
        elif choice == 2 and square[2] == 2:
            square[2] = mark
        elif choice == 3 and square[3] == 3:
            square[3] = mark
        elif choice == 4 and square[4] == 4:
            square[4] = mark
        elif choice == 5 and square[5] == 5:
            square[5] = mark
        elif choice == 6 and square[6] == 6:
            square[6] = mark
        elif choice == 7 and square[7] == 7:
            square[7] = mark
        elif choice == 8 and square[8] == 8:
            square[8] = mark
        elif choice == 9 and square[9] == 9:
            square[9] = mark
        else:
            print('Gerakan Tidak Sah! ')
            player -= 1
                
        status = game_status()
        player += 1
            
    print('HASIL PERMAINAN')    
    if status == 1:
        print('Player',player-1,'Menang')
    else:
        print('Kalian Berdua Seimbang')

def game_status():
    if square[1] == square[2] and square[2] == square[3]:
        return 1
    elif square[4] == square[5] and square[5] == square[6]:
        return 1
    elif square[7] == square[8] and square[8] == square[9]:
        return 1
    elif square[1] == square[4] and square[4] == square[7]:
        return 1
    elif square[2] == square[5] and square[5] == square[8]:
        return 1
    elif square[3] == square[6] and square[6] == square[9]:
        return 1
    elif square[1] == square[5] and square[5] == square[9]:
        return 1
    elif square[3] == square[5] and square[5] == square[7]:
        return 1
    elif square[1] != 1 and square[2] != 2 and square[3] != 3 and square[4] != 4 and square[5] != 5 and square[6] != 6 and square[7] != 7 and square[8] != 8 and square[9] != 9:
        return 0
    else:
        return -1

def papan():
    print('\n\n\tTic Tac Toe\n\n')

    print('Player 1 (X)  -  Player 2 (O)' ) 
    print()

    print('     |     |     ' )
    print(' ' ,square[1] ,' | ' ,square[2] ,' |  ' ,square[3] )

    print('_____|_____|_____' )
    print('     |     |     ' )

    print(' ' ,square[4] ,' | ' ,square[5] ,' |  ' ,square[6] )

    print('_____|_____|_____' )
    print('     |     |     ' )

    print(' ' ,square[7] ,' | ' ,square[8] ,' |  ' ,square[9] )

    print('     |     |     ' )

main()