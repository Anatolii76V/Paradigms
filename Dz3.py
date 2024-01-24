board = [' '] * 9


def display_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


display_board()


def check_win(player):
    for i in range(3):
        if (board[i] == board[i + 3] == board[i + 6] == player) or \
                (board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player):
            return True
    if (board[0] == board[4] == board[8] == player) or \
            (board[2] == board[4] == board[6] == player):
        return True
    return False


def check_draw():
    return ' ' not in board


def play_game():
    current_player = 'X'

    while True:
        display_board()
        print(f"Ход игрока {current_player}")

        try:
            move = int(input("Введите номер ячейки (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = current_player
            else:
                print("Ячейка уже занята. Попробуйте еще раз.")
                continue
        except (ValueError, IndexError):
            print("Некорректный ввод. Попробуйте еще раз.")
            continue

        if check_win(current_player):
            display_board()
            print(f"Игрок {current_player} выиграл!")
            break
        elif check_draw():
            display_board()
            print("Ничья!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


play_game()

