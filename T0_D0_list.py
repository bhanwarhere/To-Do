# To-Do List
to_do_list = []
def add_task(task):
    to_do_list.append(task)
    print(f"Task '{task}' added.")
    print("Current To-Do List:")
    for i, task in enumerate(to_do_list, 1):
        print(f"{i}. {task}")
        print()
        def remove_task(task):
            if task in to_do_list:
                to_do_list.remove(task)
                print(f"Task '{task}' removed.")
            else:
                print(f"Task '{task}' not found.")

                #Example Usage
                add_task("Buy groceries")
                remove_task("Buy groceries")

                print("Current To-Do List:")
                for i, task in enumerate(to_do_list, 1):
                    print(f"{i}. {task}")
                print()

#Creating-list
fruits = ['apple', 'banana', 'cherry', 'date']
print(fruits)

#Adding elements to list
fruits.append('elderberry')
print(fruits)
fruits.insert(1, 'blueberry')
print(fruits)
fruits.extend(['fig', 'grape'])
print(fruits)

#Removing Elemtents from list
fruits.remove('date')
print(fruits)
fruits.pop(2)
print(fruits)
fruits.clear()
print(fruits)

#Common_List 
numbers = [1, 2, 3, 4, 5]
print(numbers)

#Adding elements to list
numbers.append(6)
print(numbers)
numbers.insert(2, 2.5)
print(numbers)
numbers.extend([7, 8])
print(numbers)

#Removing Elements from list
numbers.remove(4)
print(numbers)
numbers.pop(1)
print(numbers)
numbers.clear()
print(numbers)

#Shorting and reverseing a list
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#copying a list
numbers_copy = numbers.copy()
print(numbers_copy)
