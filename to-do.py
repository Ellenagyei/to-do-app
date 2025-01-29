print('*******Welcome to my to-do app*******')

user_list =[]                   
while True:  
    user_option= int(input('choose an option below: \n'
                        '1.Add\n'
                        '2.View \n'
                        '3.Edit \n'
                        '4.Delete\n'
                        '5.Exit \n'))                    
    if user_option == 1:
  #   add an a task
      add_input = input('Add to-do: \n')
      user_list.append(add_input)
      print(f'{add_input} has been added to your to-do successfully')
      # while loop(infinity loop)
    elif user_option ==2:
    # if user_list:
      # print('your todo list: ')
      # for add_input in user_list:
      print(user_list)
    elif user_option ==3:
      pass
    elif user_option == 4:
      pass
    elif user_option == 5:
      print('Good bye...')
      exit()
    else:
      print('wrong entry')
 