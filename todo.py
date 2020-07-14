#!/usr/bin/env python3
user_input = "Random"
def show_menu():
    print('Menu: ')
    menu = ['1). Add an Item', '2). Mark item as done',
      '3). View completed item',  '4). Exit']
    for item in menu:
        print(item)
    

while user_input != '4':
    show_menu()
    user_input = input('Enter your choice:')

    todo_list = []
    if user_input == '1':
        items = input('Enter your list seprated by comma').split(',')
        todo_list.extend(items)
        print('Items added: ', items)
    elif user_input == '2' and len(todo_list) > 1:
        print('Mark as done')
    elif user_input == '3':
        for l in todo_list:
        print(l)
    elif user_input == 'Exit':
        print('Goodbye')
    else:
        print('Please enter one of 1, 2, 3, or 4')
