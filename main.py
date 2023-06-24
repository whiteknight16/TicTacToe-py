import math,random
random_number_array=[1,2,3,4,5,6,7,8,9]
game_arr=[["[1]","[2]","[3]"],
          ["[4]","[5]","[6]"],
          ["[7]","[8]","[9]"],]
result="Draw"
def is_game_over():
    # Check rows
    if (game_arr[0][0]==game_arr[0][1]==game_arr[0][2]):
        result=game_arr[0][0]
        return False,result
    if (game_arr[1][0]==game_arr[1][1]==game_arr[1][2]):
        result=game_arr[1][0]
        return False,result
    if (game_arr[2][0]==game_arr[2][1]==game_arr[2][2]):
        result=game_arr[2][0]
        return False,result
    # Check diagonals
    if (game_arr[0][0]==game_arr[1][1]==game_arr[2][2]):
        result=game_arr[0][0]
        return False,result
    if (game_arr[2][0]==game_arr[1][1]==game_arr[0][2]):
        result=game_arr[2][0]
        return False,result
    # Check Columns
    if (game_arr[0][0]==game_arr[1][0]==game_arr[2][0]):
        result=game_arr[0][0]
        return False,result
    if (game_arr[0][1]==game_arr[1][1]==game_arr[2][1]):
        result=game_arr[0][1]
        return False,result
    if (game_arr[2][0]==game_arr[2][1]==game_arr[2][2]):
        result=game_arr[2][0]
        return False,result
    else :
        return True,"Draw"


def print_board():
    for i in range(3):
        for j in range(3):
            print(game_arr[i][j],end="")
        print()
print("Printing Game Board")
print_board()

def game_function():
    # Player Turn
    player_choice=int(input("Enter where to place X: "))
    if (game_arr[int((player_choice-1)/3)][int((player_choice-1)%3)]==f"[{player_choice}]"):
        game_arr[int((player_choice-1)/3)][int((player_choice-1)%3)]="[X]"
        random_number_array.remove(player_choice)
    else:
        print("Please make a valid entry")
        game_function()
    # Computer Turn
    computer_choice=random.choice(random_number_array)
    if (game_arr[int((computer_choice-1)/3)][int((computer_choice-1)%3)]==f"[{computer_choice}]"):
        game_arr[int((computer_choice-1)/3)][int((computer_choice-1)%3)]="[O]"
        random_number_array.remove(computer_choice)
    print_board()

game=True
while(game and len(random_number_array)>0):
    game_function()
    game,result=is_game_over()

if (result=="[X]"):
    print("User won")
elif (result=="[O]"):
    print("System won")
else:
    print("It is a draw")