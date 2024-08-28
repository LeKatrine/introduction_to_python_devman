win_state = False
counter = 0
player = ""
board = list(range(1, 10))
all_win_coords = ((0, 1, 2), (3, 4, 5), 
                  (6, 7, 8), (0, 3, 6),
                  (1, 4, 7), (2, 5, 8), 
                  (0, 4, 8), (6, 4, 2))

while win_state == False:
    if counter % 2 == 0:
        player = "O"
    else:
        player = "X"
    print(f"\nХод игрока {player}\n")

    for step in range(0,7,3):
        print("|", board[step], 
              "|", board[step + 1], 
              "|", board[step + 2], "|")
    
    move = int(input(f"\nИгрок {player}, куда хотите сделать ход? (от 1 до 9)"))
    if move < 1 or move > 9:
        print("Вероятно вы опечатались. На поле нет ячейки с таким номером")
    elif move not in board:
        print("Такой ход уже был!")
    else:
        board[move - 1] = player
        counter += 1
        if counter > 4:
            for first_box, second_box, third_box in all_win_coords:
                if board[first_box] == board[second_box] == board[third_box]:
                    win_state = True
                    print(f"Игрок {player} - вы победили!")
                    
        if counter > 8 and not win_state:
            print("Победила дружба!")
            win_state = True