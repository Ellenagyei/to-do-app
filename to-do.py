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
  #   add an a task
      add_input = input('Add to-do: \n')
      user_list.append(add_input)
      print(f'{add_input} has been added to your to-do successfully')
      # while loop(infinity loop)
    elif user_option ==2:
      if not user_list:
        print('your todo list is empty ')
      # for add_input in user_list:
      else:
       print('to do list')
       for index,item in enumerate(user_list, start =1):
         print(f'{index}.{item}')
    elif user_option ==3:
      pass
    elif user_option == 4:
      if not user_list:
        print("there's no item to delete")
      else:
        try:
          task_number = int(input('enter task number you want to delete! \n'))
          user_list.pop(task_number-1)
          print(f'{add_input} has succefully deleted ')
        except(ValueError, IndexError):
          print('invalid task number')
    elif user_option == 5:
      pass 
    elif user_option == 6:
      print('Good bye...')
      exit()
    else:
      print('wrong entry')
 