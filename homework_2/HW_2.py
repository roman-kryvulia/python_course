def game_ttt():
    gameboard = [1,2,3,4,5,6,7,8,9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

   
    def print_board():
        print ("-------------")
    
        for i in range(3):
            print( "|", gameboard[0+i*3], "|", gameboard[1+i*3], "|", gameboard[2+i*3], "|")
            print("-------------")
  
    def player_1():
        n = choose_number()
        if gameboard[n] == "X" or gameboard[n] == "O":
            print("\nYou can't go there. Try again")
            player_1()
        else:
            gameboard[n] = "X"

    def player_2():
        n = choose_number()
        if gameboard[n] == "X" or gameboard[n] == "O":
            print("\nYou can't go there. Try again")
            player_2()
        else:
            gameboard[n] = "O"

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nThat's not on the board. Try again")
                        continue
                except ValueError:
                   print("\nThat's not a number. Try again")
                   continue

    def check_board():
        count = 0
        for a in win_commbinations:
            if gameboard[a[0]] == gameboard[a[1]] == gameboard[a[2]] == "X":
                print("Player 1 Wins!\n")
                print("Congratulations!\n")
                return True

            if gameboard[a[0]] == gameboard[a[1]] == gameboard[a[2]] == "O":
                print("Player 2 Wins!\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if gameboard[a] == "X" or gameboard[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a draw\n")
                return True

    while not end:
        print_board()
        end = check_board()
        if end == True:
            break
        print("Player 1 choose where to place a cross")
        player_1()
        print()
        print_board()
        end = check_board()
        if end == True:
            break
        print("Player 2 choose where to place a zero")
        player_2()
        print()

    if input("Play again (y/n)\n") == "y":
        print()
        game_ttt()

game_ttt()



