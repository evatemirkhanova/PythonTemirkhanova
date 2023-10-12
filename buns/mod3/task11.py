# НАХОЖДЕНИЕ ПОБЕДИТЕЛЯ
def find_game_winner(board):
    k = len(board) # СТОРОНА МАТРИЦЫ
    for i in range(k):
        # пробегаемся по строке
        # если первый символ не пробел и КАЖДЫЙ СИМВОЛ строки равен ему, то он победный
        if all( (board[i][j] == board[i][0]) and (board[i][0] != "_") for j in range(1,k) ):
            return board[i][0] 
    for j in range(k):
        # теперь пробегаемся по столбцам
        # если первый символ не пробел и КАЖДЫЙ СИМВОЛ столбца равен ему, то он победный
        if all( (board[i][j] == board[0][j]) and (board[0][j] != "_") for i in range(1,k) ):
            return board[0][j]
    # идем по главной диагонали матрицы
    # если первый символ не пробел и КАЖДЫЙ СИМВОЛ главной диагонали равен ему, то он победный
    if all( (board[i][i] == board[0][0]) and (board[0][0] != "_") for i in range(1,k) ):
        return board[0][0]
    # идем по побочной диагонали матрицы
    # если первый символ не пробел и КАЖДЫЙ СИМВОЛ побочной диагонали равен ему, то он победный
    if all( (board[i][k-i-1] == board[0][k-1]) and (board[0][k-1] != "_") for i in range(1,k) ):
        return board[0][k-1]
    return "Ничья"

# ВВОД 1-Й СТРОКИ (от ее размера зависит кол-во строк и столбцов в матрице)
row = input().split()
game_matrix = []
game_matrix.append(row)

# СТОРОНА МАТРИЦЫ
k = len(row)

# ЗАПИСАТЬ В МАТРИЦУ ОСТАВШИЕСЯ СТРОКИ
for i in range(k-1):
    row = input().split()
    game_matrix.append(row)
    
# ВЫВОД ПОБЕДИТЕЛЯ
print(find_game_winner(game_matrix))
