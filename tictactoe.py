cells = "_________"
print("""---------
| _ _ _ | 
| _ _ _ |
| _ _ _ |
---------""")
global li
li = [[cells[j + i] for j in range(0, 3)] for i in range(0, 9, 3)]
def print_tic_tac():
    print("---------")
    print("| " + li[0][0] + " " + li[0][1] + " " + li[0][2] + " |")
    print("| " + li[1][0] + " " + li[1][1] + " " + li[1][2] + " |")
    print("| " + li[2][0] + " " + li[2][1] + " " + li[2][2] + " |")
    print("---------")

def X_wins(li):
    if li[0][0] == li[0][1] == li[0][2] == 'X' or li[1][0] == li[1][1] == li[1][2] == 'X' or li[2][0] == li[2][1] == \
            li[2][2] == 'X' or li[0][0] == li[1][0] == li[2][0] == 'X' or li[0][1] == li[1][1] == li[2][1] == 'X' or \
            li[0][2] == li[1][2] == li[2][2] == 'X' or li[0][0] == li[1][1] == li[2][2] == 'X' or li[0][2] == li[1][
        1] == li[2][0] == 'X':
        return True
    else:
        return False


def O_wins(li):
    if li[0][0] == li[0][1] == li[0][2] == 'O' or li[1][0] == li[1][1] == li[1][2] == 'O' or li[2][0] == li[2][1] == \
            li[2][2] == 'O' or li[0][0] == li[1][0] == li[2][0] == 'O' or li[0][1] == li[1][1] == li[2][1] == 'O' or \
            li[0][2] == li[1][2] == li[2][2] == 'O' or li[0][0] == li[1][1] == li[2][2] == 'O' or li[0][2] == li[1][
        1] == li[2][0] == 'O':
        return True
    else:
        return False


def contains_empty(li):
    for i in li:
        for j in i:
            if j == " " or j == "_":
                return True
    return False

def check_resutl(li):
    if X_wins(li) == False and O_wins(li) == False and contains_empty(li) == False:
        return "Draw"
    if X_wins(li) == True:
        return "X wins"
    if O_wins(li) == True:
        return "O wins"
    if X_wins(li) == True and O_wins(li) == True or abs(cells.count("X") - cells.count("O")) >= 2:
        return "Impossible"
    return False

def check_empty_cells(coordinates):
    if li[int(coordinates[0])-1][int(coordinates[2])-1] == " " or li[int(coordinates[0])-1][int(coordinates[2])-1] == "_":
        return True
    else:
        return False

def check_coordinates(coordinates):
    if coordinates[0].isdigit() and coordinates[2].isdigit():
        return True
    else:
        return False

def check_coordinates_value(coordinates):
    if int(coordinates[0]) <= 3 and int(coordinates[2]) <= 3 and int(coordinates[0]) >= 1 and int(coordinates[2]) >= 1:
        return True
    else:
        return False

count = 0
turn = ""
def update_tic_tac(coordinates, count):
    if count % 2 == 0:
        turn = "O"
    else:
        turn = "X"
    if check_coordinates(coordinates):
        if check_coordinates_value(coordinates):
            if check_empty_cells(coordinates):
                li[int(coordinates[0])-1][int(coordinates[2])-1] = turn
                print_tic_tac()
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")


while True:
    coordinates = input("Enter the coordinates:")
    count = count + 1
    update_tic_tac(coordinates, count)
    if check_resutl(li) != False:
        print(check_resutl(li))
        break
