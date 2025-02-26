from IPython.display import clear_output 
import keyboard
import random

def display_board(board):
    
    print(board[1],"|",board[2],"|",board[3])
    print(board[4],"|",board[5],"|",board[6])
    print(board[7],"|",board[8],"|",board[9])



 
def player_one_input():
    marker_accept = ['X','O']
    marker = ''
    while marker not in marker_accept:
     marker = input("Player One choose to be X or O: (Press ESC to exit) ").upper()
     
     if keyboard.is_pressed("esc"):
        print("\nGame exited by user.")
        break
     
     if marker == 'X':
        print("Player One will be X and Player Two will be O")
        return 'X'
     elif marker == 'O':
        print("Player One will be O and Player Two will be X")
        return 'O'
     else:
        print("Invalid choice. Please enter 'X' or 'O'.(Press ESC to exit)")
     



def player_two(player_one_marker):
    if player_one_marker == 'X':
        return 'O'
    else:
        return 'X'
    

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    winning = [(1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
    (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
    (1, 5, 9), (3, 5, 7)]

    for combo in winning:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == marker:
            return "Congratulations you have won!"
    return False


def choose_first():
    
    player_one = random.randint(1,10)
    player_two = random.randint(1,10)
    if player_one > player_two:
        print("Player One goes first!")
        return 1
    else:
        print("Player Two goes first!")
        return 2
    
def choose_player():
    print("Choose who will be Player One and Player Two!")

def space_check(board, position):
     return board[position] not in ['X', 'O']

def full_board_check(board):
    return all(space in ['X', 'O'] for space in board[1:10])

def player_choice(board):
    accepted_positions = [1,2,3,4,5,6,7,8,9]
    position = None
    while position not in accepted_positions:
        try:
            position = int(input("Please choose a number position from (1-9)"))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        if position not in accepted_positions:
            print("Invalid position. Choose a number from 1 to 9.")
    
    
    if not space_check(board, position):
        print(f"That position is occupied with {board[position]}")
        return player_choice(board)
        
    return position

def replay():
    
    user_choice = ''
    choices = ['Y','N']
    while user_choice not in choices:
      user_choice = input("Do you want to play again? (Y or N)")
      if user_choice == 'Y':
         return True
      else:
         return False
      




def tic():
  print('Welcome to Tic Tac Toe!\n')

  print("Choose who will be Player One and Player Two!")
  print()
  

  player_one_marker = player_one_input()
  player_two_marker = player_two(player_one_marker)
  
  player_turn = choose_first()
  board = ['#','','','','','','','','','']

  while True:
    
    
    if player_turn == 1:
      clear_output(wait=True)
      display_board(board)
      print(f"Player {player_turn}'s turn ({player_one_marker})")
      chosen_position = player_choice(board)
      if space_check(board,chosen_position):
          board[chosen_position] = player_one_marker
                    
      if win_check(board,player_one_marker):        
        clear_output(wait=True)
        display_board(board)
        print("Player One Wins!")
        break
  
      if full_board_check(board):        
        clear_output(wait=True)
        display_board(board)
        print("It's a tie!")
        break

      player_turn = 2        
          
      
  
    else:
        clear_output(wait=True)
        display_board(board)
        print(f"Player {player_turn}'s turn ({player_two_marker})")
        chosen_position = player_choice(board)
        if space_check(board,chosen_position):
          board[chosen_position] = player_two_marker
        if win_check(board,player_two_marker):
         clear_output(wait=True)
         display_board(board)
         print("Player Two Wins!")
         break
      
        if full_board_check(board):
         clear_output(wait=True)
         display_board(board)
         print("It's a tie!")
         break
      
        player_turn = 1
        
  if replay():
    tic()
  else:
    print("Thanks for playing!")

tic()