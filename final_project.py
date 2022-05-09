from os import cpu_count, name
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Isolation Game")
visited_node_button=[]
visited_node_button_name=[]
player_moves=[]
player_move_button=[]
computer_moves=[]
computer_moves_button=[]

def check_constraint_player(button_name):
    current_node_name=player_moves[-1]
    
            
    if(current_node_name=='b1' or current_node_name=='b4' or current_node_name=='b7'):
        current_node_number=int(current_node_name[-1])
        button_name_number=int(button_name[-1])
        if(button_name_number==current_node_number+1 or button_name_number==current_node_number+3 or button_name_number==current_node_number-3):
            return True
                    
    if(current_node_name=='b2' or current_node_name=='b5' or current_node_name=='b8'):    
        current_node_number=int(current_node_name[-1])
        button_name_number=int(button_name[-1])
        if(button_name_number==current_node_number+1 or button_name_number==current_node_number-1 or button_name_number==current_node_number+3 or button_name_number==current_node_number-3):
            return True     
                   
                     
    if(current_node_name=='b3' or current_node_name=='b6' or current_node_name=='b9'):    
        current_node_number=int(current_node_name[-1])
        button_name_number=int(button_name[-1])
        if( button_name_number==current_node_number-1 or button_name_number==current_node_number+3 or button_name_number==current_node_number-3):
            return True              

                
    if(current_node_name=='b1' or current_node_name=='b4' or current_node_name=='b7'):
        current_node_number=int(current_node_name[-1])
        button_name_number=int(button_name[-1])
        if(button_name_number==current_node_number+4 or button_name_number==current_node_number-2 ):
            return True 
                    
    if(current_node_name=='b2' or current_node_name=='b5' or current_node_name=='b8'):
        current_node_number=int(current_node_name[-1])
        button_name_number=int(button_name[-1])
        if(button_name_number==current_node_number+2 or button_name_number==current_node_number+4 or button_name_number==current_node_number-4 or button_name_number==current_node_number-2):
            return True 
                        
    if(current_node_name=='b3' or current_node_name=='b6' or current_node_name=='b9'):
        current_node_number=int(current_node_name[-1])
        button_name_number=int(button_name[-1])
        if(button_name_number==current_node_number-4 or button_name_number==current_node_number+2 ):
            return True 
                
    if(current_node_name=='b1'):
        if(button_name=='b3'):
            if 'b2' not in visited_node_button_name:
                return True 
                    
        elif(button_name=='b7'):
            if 'b4' not in visited_node_button_name:
                return True
                        
        elif(button_name=='b9'):
            if 'b5' not in visited_node_button_name:
                return True                                       
            
    if(current_node_name=='b2'):
        if(button_name=='b8'):
            if 'b5' not in visited_node_button_name:
                return True                
                                        
    if(current_node_name=='b3'):
        if(button_name=='b1'):
            if 'b2' not in visited_node_button_name:
                return True 
                        
        elif(button_name=='b7'):      
            if 'b5' not in visited_node_button_name:
                return True 
                            
        elif(button_name=='b9'):      
            if 'b6' not in visited_node_button_name:
                return True                         
                
    if(current_node_name=='b4'):
        if 'b5' not in visited_node_button_name:
            if(button_name=='b6'):
                return True 
                        
    if(current_node_name=='b6'):
        if(button_name=='b4'):
            if 'b5' not in visited_node_button_name:
                return True 
                        
    if(current_node_name=='b7'):
        if(button_name=='b1'):
            if 'b4' not in visited_node_button_name:
                return True 
                        
        elif(button_name=='b3'):
            if 'b5' not in visited_node_button_name:
                return True 
        elif(button_name=='b9'):
            if 'b8' not in visited_node_button_name:
                return True 
    
    if(current_node_name=='b8'):
        if(button_name=='b2'):
            if 'b5' not in visited_node_button_name:
                return True 
            
    if(current_node_name=='b9'):
        if(button_name=='b1'):
            if 'b5' not in visited_node_button_name:
                return True 
        elif(button_name=='b3'):
            if 'b6' not in visited_node_button_name:
                return True                 
        elif(button_name=='b7'):
            if 'b8' not in visited_node_button_name:
                return True 


def check_constraint_computer(button_name):
    current_node_name=computer_moves[-1]
    
            
    if(current_node_name=='b1' or current_node_name=='b4' or current_node_name=='b7'):
        current_node_number=int(current_node_name[-1])
        button_name_number=int(button_name[-1])
        if(button_name_number==current_node_number+1 or button_name_number==current_node_number+3 or button_name_number==current_node_number-3):
            return True
                    
    if(current_node_name=='b2' or current_node_name=='b5' or current_node_name=='b8'):    
        current_node_number=int(current_node_name[-1])
        button_name_number=int(button_name[-1])
        if(button_name_number==current_node_number+1 or button_name_number==current_node_number-1 or button_name_number==current_node_number+3 or button_name_number==current_node_number-3):
            return True     
                   
                     
    if(current_node_name=='b3' or current_node_name=='b6' or current_node_name=='b9'):    
        current_node_number=int(current_node_name[-1])
        button_name_number=int(button_name[-1])
        if( button_name_number==current_node_number-1 or button_name_number==current_node_number+3 or button_name_number==current_node_number-3):
            return True              

                
    if(current_node_name=='b1' or current_node_name=='b4' or current_node_name=='b7'):
        current_node_number=int(current_node_name[-1])
        button_name_number=int(button_name[-1])
        if(button_name_number==current_node_number+4 or button_name_number==current_node_number-2 ):
            return True 
                    
    if(current_node_name=='b2' or current_node_name=='b5' or current_node_name=='b8'):
        current_node_number=int(current_node_name[-1])
        button_name_number=int(button_name[-1])
        if(button_name_number==current_node_number+2 or button_name_number==current_node_number+4 or button_name_number==current_node_number-4 or button_name_number==current_node_number-2):
            return True 
                        
    if(current_node_name=='b3' or current_node_name=='b6' or current_node_name=='b9'):
        current_node_number=int(current_node_name[-1])
        button_name_number=int(button_name[-1])
        if(button_name_number==current_node_number-4 or button_name_number==current_node_number+2 ):
            return True 
                
    if(current_node_name=='b1'):
        if(button_name=='b3'):
            if 'b2' not in visited_node_button_name:
                return True 
                    
        elif(button_name=='b7'):
            if 'b4' not in visited_node_button_name:
                return True
                        
        elif(button_name=='b9'):
            if 'b5' not in visited_node_button_name:
                return True                                       
            
    if(current_node_name=='b2'):
        if(button_name=='b8'):
            if 'b5' not in visited_node_button_name:
                return True                
                                        
    if(current_node_name=='b3'):
        if(button_name=='b1'):
            if 'b2' not in visited_node_button_name:
                return True 
                        
        elif(button_name=='b7'):      
            if 'b5' not in visited_node_button_name:
                return True 
                            
        elif(button_name=='b9'):      
            if 'b6' not in visited_node_button_name:
                return True                         
                
    if(current_node_name=='b4'):
        if(button_name=='b6'):
            if 'b5' not in visited_node_button_name:
                return True 
                        
    if(current_node_name=='b6'):
        if(button_name=='b4'):
            if 'b5' not in visited_node_button_name:
                return True 
                        
    if(current_node_name=='b7'):
        if(button_name=='b1'):
            if 'b4' not in visited_node_button_name:
                return True 
                        
        elif(button_name=='b3'):
            if 'b5' not in visited_node_button_name:
                return True 
        elif(button_name=='b9'):
            if 'b8' not in visited_node_button_name:
                return True 
    
    if(current_node_name=='b8'):
        if(button_name=='b2'):
            if 'b5' not in visited_node_button_name:
                return True 
            
    if(current_node_name=='b9'):
        if(button_name=='b1'):
            if 'b5' not in visited_node_button_name:
                return True 
        elif(button_name=='b3'):
            if 'b6' not in visited_node_button_name:
                return True                 
        elif(button_name=='b7'):
            if 'b8' not in visited_node_button_name:
                return True 




def check_for_win_loose(buttton_name):
    b1=['b2','b5','b4']
    b2=['b1','b4','b5','b6','b3']
    b3=['b2','b5','b6']
    b4=['b1','b2','b5','b8','b7']
    b5=['b1','b2','b3','b4','b6','b7','b8','b9']
    b6=['b2','b3','b5','b8','b9']
    b7=['b4','b5','b8']
    b8=['b7','b4','b5','b6','b9']
    b9=['b5','b6','b8']
    
    if(buttton_name=='b1'):
        len_b1=len(b1)
        flag=0
        for i in b1 :
            if i in visited_node_button_name:
                flag=flag+1
        
        if(flag==len_b1):
            return True
        else:
            return False
    
    if(buttton_name=='b2'):
        len_b2=len(b2)
        flag=0
        for i in b2 :
            if i in visited_node_button_name:
                flag=flag+1
        
        if(flag==len_b2):
            return True
        else:
            return False    
            
    if(buttton_name=='b3'):
        len_b3=len(b3)
        flag=0
        for i in b3 :
            if i in visited_node_button_name:
                flag=flag+1
        
        if(flag==len_b3):
            return True
        else:
            return False    
    
    if(buttton_name=='b4'):
        len_b4=len(b4)
        flag=0
        for i in b4 :
            if i in visited_node_button_name:
                flag=flag+1
        
        if(flag==len_b4):
            return True
        else:
            return False    
                    
    if(buttton_name=='b5'):
        len_b5=len(b5)
        flag=0
        for i in b5 :
            if i in visited_node_button_name:
                flag=flag+1
        
        if(flag==len_b5):
            return True
        else:
            return False    
    
    if(buttton_name=='b6'):
        len_b6=len(b6)
        flag=0
        for i in b6 :
            if i in visited_node_button_name:
                flag=flag+1
        
        if(flag==len_b6):
            return True
        else:
            return False    
    
    if(buttton_name=='b7'):
        len_b7=len(b7)
        flag=0
        for i in b7 :
            if i in visited_node_button_name:
                flag=flag+1
        
        if(flag==len_b7):
            return True
        else:
            return False    
     
    if(buttton_name=='b8'):
        len_b8=len(b8)
        flag=0
        for i in b8 :
            if i in visited_node_button_name:
                flag=flag+1
        
        if(flag==len_b8):
            return True
        else:
            return False    
    
    if(buttton_name=='b9'):
        len_b9=len(b9)
        flag=0
        for i in b9 :
            if i in visited_node_button_name:
                flag=flag+1
        
        if(flag==len_b9):
            return True
        else:
            return False

board=['b1','b2','b3','b4','b5','b6','b7','b8','b9']


def quit():
    global root
    root.destroy()


def computer_move():
    bestScore = -800
    bestMove = 0
    temp=Button()
    for key in board:
        if key not in visited_node_button_name:
            if((len(computer_moves))>0):
                if(check_constraint_computer(key)):
                    computer_moves.append(key)
                    visited_node_button_name.append(key)
                    score = minimax(0, False)
                    computer_moves.pop()
                    visited_node_button_name.pop()
                    if (score > bestScore):
                        bestScore = score
                        bestMove = key
            else:
                computer_moves.append(key)
                visited_node_button_name.append(key)
                score = minimax(0, False)
                computer_moves.pop()
                visited_node_button_name.pop()
                if (score > bestScore):
                    bestScore = score
                    bestMove = key
                

    if(bestMove=='b1'):
        temp=b1
    elif(bestMove=='b2'):
        temp=b2
    elif(bestMove=='b3'):
        temp=b3
    elif(bestMove=='b4'):
        temp=b4
    elif(bestMove=='b5'):
        temp=b5
    elif(bestMove=='b6'):
        temp=b6
    elif(bestMove=='b7'):
        temp=b7
    elif(bestMove=='b8'):
        temp=b8
    elif(bestMove=='b9'):
        temp=b9

    if(len(computer_moves)==0):
        temp.config(text="c")
        temp.config(bg='gray')
        computer_moves.append(bestMove)
        computer_moves_button.append(temp)
        visited_node_button_name.append(bestMove)
        visited_node_button.append(temp)
    else:
        temp_button=Button()
        temp_button=computer_moves_button[-1]
        temp_button.config(text=" ")
        temp.config(text="c")
        temp.config(bg='gray')
        computer_moves.append(bestMove)
        computer_moves_button.append(temp)
        visited_node_button_name.append(bestMove)
        visited_node_button.append(temp)
    
    current_button=player_moves[-1]
    if(check_for_win_loose(current_button)):
        for i in player_moves:
            print(i)
            
        for i in computer_moves:
            print(i)
        
        messagebox.showinfo("Information","Computer won")
        quit()
    return
    


def minimax(depth, isMaximizing):
    
   
    current_button=computer_moves[-1]
    if(check_for_win_loose(current_button)):
       return -1
   
    current_button=player_moves[-1]
    if(check_for_win_loose(current_button)):
       return 1
   
  
    if (isMaximizing):
        bestScore = -192
        for key in board:
            if key not in visited_node_button_name:
                if(check_constraint_computer(key)):
                    computer_moves.append(key)
                    visited_node_button_name.append(key)
                    score = minimax(depth + 1, False)
                    computer_moves.pop()
                    visited_node_button_name.pop()
                    if (score > bestScore):
                        bestScore = score
        return bestScore
                    
    else:
        bestScore = 192
        for key in board:
            if key not in visited_node_button_name:
                if(check_constraint_player(key)):
                    player_moves.append(key)
                    visited_node_button_name.append(key)
                    score = minimax(depth + 1, True)
                    player_moves.pop()
                    visited_node_button_name.pop()
                    if (score < bestScore):
                        bestScore = score
        return bestScore






def  player_move(button_name,button):
    if(len(player_moves)==0):
        button.config(text="p")
        button.config(bg='gray')
        player_moves.append(button_name)
        player_move_button.append(button)
        visited_node_button.append(button)
        visited_node_button_name.append(button_name)
        computer_move()
    else:
            if button in visited_node_button:
                messagebox.showerror("Error", "Already Occupied")
            else:
                check_value=check_constraint_player(button_name)
                if(check_value):
                    temp_button=Button()
                    temp_button=player_move_button[-1]
                    temp_button.config(text=" ")
                    button.config(text="p")
                    button.config(bg='gray')
                    player_moves.append(button_name)
                    player_move_button.append(button)
                    visited_node_button.append(button)
                    visited_node_button_name.append(button_name)
                    
                    
                    current_button=computer_moves[-1]
                    if(check_for_win_loose(current_button)):
                        for i in player_moves:
                            print(i)
            
                        for i in computer_moves:
                            print(i)
        
                        messagebox.showinfo("Information","Player won")
                        quit()
                    else:
                        computer_move()
                    
 
b1= Button(root, text=" ", height=3 , width=6,bg="SystemButtonFace" ,command=lambda: player_move('b1',b1))
b2= Button(root, text=" ", height=3 , width=6,bg="SystemButtonFace", command=lambda: player_move('b2',b2))
b3= Button(root, text=" ", height=3 , width=6,bg="SystemButtonFace", command=lambda: player_move('b3',b3))

b4= Button(root, text=" ", height=3 , width=6,bg="SystemButtonFace", command=lambda: player_move('b4',b4))
b5= Button(root, text=" ", height=3 , width=6,bg="SystemButtonFace", command=lambda: player_move('b5',b5))
b6= Button(root, text=" ", height=3 , width=6,bg="SystemButtonFace", command=lambda: player_move('b6',b6))

b7= Button(root, text=" ", height=3 , width=6,bg="SystemButtonFace", command=lambda: player_move('b7',b7))    
b8= Button(root, text=" ", height=3 , width=6,bg="SystemButtonFace", command=lambda: player_move('b8',b8))
b9= Button(root, text=" ", height=3 , width=6,bg="SystemButtonFace", command=lambda: player_move('b9',b9))

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)
root.mainloop()
