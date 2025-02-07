from functions import *

print('*******Welcome to my to-do app*******')

user_list =[]                   
while True:  
    user_option= int(input('choose an option below: \n'
                        '1.Add\n'
                        '2.View \n'
                        '3.Edit \n'
                        '4.Delete\n'
                        '5.clear\n'
                        '5.Exit \n'))                    
    if user_option == 1:
     add_todo()
      # while loop(infinity loop)
    elif user_option ==2:
      view_todo()
    elif user_option ==3: 
      edit_todo()
    elif user_option == 4:
     delete_todo()
    elif user_option == 5:
     clear_todo()
    elif user_option == 6:
      exit_todo()
    else:
      print('wrong entry')
 