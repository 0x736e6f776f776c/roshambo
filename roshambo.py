import random

options = ["rock", "paper", "scissors"]
name = input("Enter your name: ")
print("Hello,", name)

result = ""

rating_file = open('rating.txt', 'r', encoding='utf-8')
if name in rating_file:
    for num, line in enumerate(rating_file):
        num = str(num).replace(name + ' ', '')
        score = int(num)
        old_score = str(num)
else:
    score = 0
ratingdata = rating_file.read()
rating_file.close()

def Rotate(list_, num): 
    output_list = [] 
      
    for i in range(len(list_) - num, len(list_)): 
        output_list.append(list_[i]) 
          
    for i in range(0, len(list_) - num):  
        output_list.append(list_[i]) 
    return output_list

alt_options = input("Enter alternative options (seperated by a comma) if you want to use any, otherwise just press enter: ").replace(",", " ").split()
print("Okay, let's start.")

if len(alt_options) > 3:
    options = alt_options   
    def winning_algorithm(chosen_option):
        index_option = int(options.index(chosen_option))
        if index_option != len(options) // 2:
            if index_option < len(options) // 2:
                rotate_num = len(options) // 2 - index_option
            else:
                rotate_num = index_option - len(options) // 2
            new_list = Rotate(options, rotate_num)
            
        else:
            new_list = options
        mid_index = new_list.index(chosen_option)
        left_list = new_list[0 : mid_index]
        right_list = new_list[mid_index + 1 : len(new_list) + 1]
        if computer_choice in right_list:
            print("You lose! Computer chose " + computer_choice + ".")
            result = "lose"            
        elif computer_choice in left_list:
            print("Well played! Computer chose " + computer_choice + " and lost.")
            result = "win"
            

while True:
    
    print("Enter what you want to play.")
    print("If you want to exit type '!exit' and to see your rating type '!rating'.")
    player_choice = input().strip()
    computer_choice = random.choice(options)

    if player_choice != "!exit" and player_choice != "!rating" and player_choice not in options:
        print("Invalid input")
        continue
    elif player_choice == "!exit":
        print("Bye, " + name + "!")
        if name in ratingdata:
            rfile = open('rating.txt', 'w')
            oldstr_ = name + " " + old_score
            new_score = str(score)
            newstr_ = name + " " + new_score
            ratingdata = ratingdata.replace(oldstr_, newstr_)
            rfile.write(ratingdata)
            rfile.close()
            break
        elif name not in ratingdata:
            rfile = open('rating.txt', 'a')
            new_score = str(score)
            newstr_ = name + " " + new_score
            rfile.append(newstr_)
            rfile.close()
            break
        
    elif player_choice == "!rating":
        print("Your rating:", score)
        continue
    elif player_choice == computer_choice:
        print("It's a draw! (" + player_choice + ")")  
        score += 50  
        continue
    elif len(alt_options) < 3:    
        if player_choice == "scissors":
            if computer_choice == "rock":
                print("You lose! Computer chose " + computer_choice + ".")
            else:
                print("Well played! Computer chose " + computer_choice + " and lost.")
                score += 100
        elif player_choice == "rock":
            if computer_choice == "paper":
                print("You lose! Computer chose " + computer_choice + ".")
            else:
                print("Well played! Computer chose " + computer_choice + " and lost.")
                score += 100
        elif player_choice == "paper":
            if computer_choice == "scissors":
                print("You lose! Computer chose " + computer_choice + ".")
            else:
                print("Well played! Computer chose " + computer_choice + " and lost.")
                score += 100
        continue
    elif len(alt_options) > 3:
        winning_algorithm(player_choice)
        score += 100
    continue
