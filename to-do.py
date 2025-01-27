print('*******Welcome to my to-do app*******')
user_option= int(input('choose an option below: \n'
                      '1.Add\n'
                      '2.View \n'
                      '3.Edit \n'
                      '3.Delete\n'))
user_list =[]
if user_option == 1:
#   add an a task
    add_input = input('Add to-do: \n')
    user_list.append(add_input)
    print(f'{add_input} has been added to your to-do successfully')
    # while loop(infinity loop)
elif user_option ==2:
  pass
elif user_option ==3:
  pass
elif user_option == 4:
  pass
else:
  print('wrong options')
