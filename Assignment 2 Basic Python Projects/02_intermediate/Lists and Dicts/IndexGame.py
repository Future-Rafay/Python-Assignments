my_list = ['apple', 20, '', 'True', False]

# Accessing Elements
def get_elem(lst: list, index: int):
    if index < 0 or index >= len(lst):
        return "Please enter a correct index"
    return lst[index]

# Modifying Elements
def replace_elem(lst: list, index: int, new_value):
    if index < 0 or index >= len(lst):
        return "Please enter a correct index"
    lst[index] = new_value
    return lst

# Slicing the list
def slice_list(lst: list, start: int, end: int):
    return lst[start:end]

# Getting list from user
def list_input_from_user():
    user_input: str = input("Please Enter Elements Separated by spaces: ")
    my_list: list = user_input.split()
    print("Your list:", my_list)
    return my_list

# Interactive menu
def index_game():
    lst: list = list_input_from_user()
    actions: list = ["access", "modify", "slice"]

    print("\nSelect an action:")
    for i in actions:
        print(f"-> {i}")

    user_input: str = input("\nYour choice: ").strip().lower()

    if user_input == "access":
        index = int(input("Enter index to access: "))
        result = get_elem(lst, index)
        print("Result:", result)

    elif user_input == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        result = replace_elem(lst, index, new_value)
        print("Modified list:", result)

    elif user_input == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        result = slice_list(lst, start, end)
        print("Sliced list:", result)

    else:
        print("Invalid action. Please choose from 'access', 'modify', or 'slice'.")

def main():
    index_game()

if __name__ == "__main__":
    main()
