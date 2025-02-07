user_list = []
def add_todo():
 # add an a task
    add_input = input('Add to-do: \n')
    user_list.append(add_input)
    print(f'{add_input} has been added to your to-do successfully')
    
def view_todo():
    if not user_list:
        print('your todo list is empty ')
      # for add_input in user_list:
    else:
       print('to do list')
       for index,item in enumerate(user_list, start =1):
         print(f'{index}.{item}')
         
def edit_todo():
    if not user_list:
        print('there are no list to edit')
    else:
        for index,item in enumerate(user_list, start=1):
          print(f'{index}. {item}')
        try:
          task_number= int(input('Enter your task number to edit: \n'))
          if 1 <= task_number <= len(user_list):
            new_user_list = input('Enter your new user list to edit: \n')
            user_list[task_number-1] = new_user_list
            print(f'task number{task_number} has been edited ')
          else:
            print('wrong number')
        except(ValueError,IndexError):
          print('Invalid task number')
          
def delete_todo(add_input):
     if not user_list:
        print("there's no item to delete")
     else:
        try:
          task_number = int(input('enter task number you want to delete! \n'))
          if 1 <= task_number <= len(user_list):
           user_list.pop(task_number-1)
           print(f'{add_input} has succefully deleted ')
          else:
              print('wrong entry')
        except(ValueError, IndexError):
          print('invalid task number')

def clear_todo():
     if not user_list:
        print('your to-do list is empty')
     else:
        user_list .clear()
        print('all list has been cleared')

def exit_todo():
    print('Good bye...')
    exit()
  