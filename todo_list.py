#s=input()
'''meals=['pasta','pizza','cafe']
for meal in meals:
    print(meal)
    print(meal.capitalize())'''

#bug fixing

'''buttons = ["cancel", "reply", "submit"]
for i in buttons:
    print(i.capitalize())'''

#Match-Case Assignment
'''country = "Italy"

match country:
    case "USA":
        print("Hello")
    case "Italy":
        print("Ciao")
    case "Germany":
        print("Hallo")'''
#Match-case with bitwise operator
'''country = "USA"

match country:
    case "USA" | "United States":
        print("Hello")
    case "Italy":
        print("Ciao")
    case "Germany":
        print("Hallo")


todos=[]

while True:
    user_action=input("Type add, show, edit or exit:")
    user_action=user_action.strip()

    match user_action:
        case "add":
            todo= input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            num= int(input("Enter a number: "))
            num = num-1
            new_todo= input("Enter a todo")
            todos[number]= new_todo
        case "exit":
            break
print("Bye")
'''

#enumerate func

todos=[]

while True:
    user_action=input("Type add, show, edit or exit:")
    user_action=user_action.strip()

    match user_action:
        case "add":
            todo= input("Enter a todo: ")
            todos.append(todo)
            file=open('todos.txt','w')
            file.writelines(todos)
            file.close()
        case "show":
            for index,item in enumerate(todos):
                print(index, '-', item)
        case "edit":
            num= int(input("Enter a number: "))
            num = num-1
            new_todo= input("Enter a todo")
            todos[num]= new_todo
        case "exit":
            break
print("Bye")

'''
for i, j in enumerate("Diju Sharon"):
    print(i, j)
'''
#Debugging
'''
menu = ["pasta", "pizza", "salad"]

user_choice = int(input("Enter the index of the item: "))

message = f"You chose {menu[user_choice]}."
print(message)
'''
