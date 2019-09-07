from IPython.display import clear_output
def display(input_list):
    print("   |   |   ");
    print(" "+input_list[6]+" |"+" "+input_list[7]+" |"+" "+input_list[8]+" ")
    print("   |   |   ");
    print("-----------");
    print("   |   |   ");
    print(" "+input_list[3]+" |"+" "+input_list[4]+" |"+" "+input_list[5]+" ")
    print("   |   |   ");
    print("-----------");
    print("   |   |   ");
    print(" "+input_list[0]+" |"+" "+input_list[1]+" |"+" "+input_list[2]+" ")
    print("   |   |   ");
def no_win(input_list):
    return input_list.count(' ');
def player_names():
     player=['',''];
     player[0]=input("Enter Your name- ");
     player[1]=input("Enter Opponent Name- ");
     return player;
def player_choice(player):
    choice=input(player[0]+" play as X or 0 : ");
    choice=input_validation(player[0],choice,"Choice");
    choice_dict=['X','O'];
    #dictionary can not use as name used as key which can't be duplicate
    if(choice.upper()=='O'):
        choice_dict[0]='O';
        choice_dict[1]='X';
    return choice_dict;
def occupy_check(input_list,player_num,choice):
    if(str(input_list[choice-1]).count(' ')==0):
        choice= input(player_num+" this position is already occupied by other player please enter valid input: ");
        choice= input_validation(player_num,choice,"Turn");
        choice= occupy_check(input_list,player_num,int(choice));
    return choice;
def input_validation(player_num,user_input,v_flag):
    if(v_flag=="Turn"):
        try:
            if(int(user_input)>=10):
                user_input= input(player_num+" please enter only Valid turn between 1-9: ");
                user_input=input_validation(player_num,user_input,v_flag);
        except:
            user_input= input(player_num+" please enter only Valid turn between 1-9: ");
            user_input=input_validation(player_num,user_input,v_flag);
    elif(v_flag=="Choice"):
        if(not (user_input.upper()=="X" or user_input.upper()=="O")):
            user_input= input(player_num+" please enter Choice in X and O only: ");
            user_input=input_validation(player_num,user_input,v_flag);
    elif(v_flag=="Replay"):
        if(not (user_input.upper()=='Y' or user_input.upper()=='N')):
            user_input= input("Please enter Replay Option in Y and N only: ");
            user_input=input_validation(player_num,user_input,v_flag);
    return user_input;
def player_input(input_list,player_num):
    choice=input("its "+player_num+"'s turn - Please enter input from 1-9 : ");
    choice=input_validation(player_num,choice,"Turn");
    choice=occupy_check(input_list,player_num,int(choice));
    return int(choice);
def result_calculation(input_list):
    if(input_list[6]+input_list[7]+input_list[8]=="XXX" or input_list[6]+input_list[7]+input_list[8]=="OOO"):
        return True;
    elif(input_list[3]+input_list[4]+input_list[5]=="XXX" or input_list[3]+input_list[4]+input_list[5]=="OOO"):
        return True;
    elif(input_list[0]+input_list[1]+input_list[2]=="XXX" or input_list[0]+input_list[1]+input_list[2]=="OOO"):
        return True;2
    elif(input_list[6]+input_list[3]+input_list[0]=="XXX" or input_list[6]+input_list[3]+input_list[0]=="OOO"):
        return True;
    elif(input_list[8]+input_list[5]+input_list[2]=="XXX" or input_list[8]+input_list[5]+input_list[2]=="OOO"):
        return True;
    elif(input_list[7]+input_list[1]+input_list[4]=="XXX" or input_list[7]+input_list[1]+input_list[4]=="OOO"):
        return True;
    elif(input_list[6]+input_list[4]+input_list[2]=="XXX" or input_list[6]+input_list[4]+input_list[2]=="OOO"):
        return True;
    elif(input_list[8]+input_list[4]+input_list[0]=="XXX" or input_list[8]+input_list[4]+input_list[0]=="OOO"):
        return True;
def main_method():
    player=player_names();
    replay='Y';
    while(replay.upper()=='Y'):
        flag=0;
        players_choice=player_choice(player);
        print("sample dashboard ");
        display(['1','2','3','4','5','6','7','8','9']);
        input_list = [' ',' ',' ',' ',' ',' ',' ',' ',' '];
        while(True):
            input_num=player_input(input_list,player[flag]);
            clear_output();
            input_list[input_num-1]=players_choice[flag];
            display(input_list);
            if(result_calculation(input_list)):
                print(player[flag]+" win this match");
                break;
            elif(no_win(input_list)==0):
                print("Board is full!!Match is draw");
                break;
            if(flag == 0):
                flag = 1;
            else:
                flag= 0;
        replay = input("Do You Want To Replay if Yes press 'Y' else 'N': ");
        replay = input_validation('',replay,"Replay");
        clear_output();
main_method();