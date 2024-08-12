

def display_menu():
    """
    Display the menu options for list operations.
    """
    print("\nChoose a list operation:")
    print("1. Append")
    print("2. Extend")
    print("3. Insert")
    print("4. Remove")
    print("5. Pop")
    print("6. Clear")
    print("7. Index")
    print("8. Count")
    print("9. Sort")
    print("10. Reverse")
    print("11. Copy")
    print("12. Exit")


def handle_append(lst):
    """
    Append a value to the list.

    Args:
    - lst (list): The list to append to.
    """
    value = input("Enter the value to append: ")
    lst.append(value)
    print(f"Updated list: {lst}")


def handle_extend(lst):
    """
    Extend the list with additional values.

    Args:
    - lst (list): The list to extend.
    """
    values = input("Enter values to extend the list (comma-separated): ")
    lst.extend(values.split(','))
    print(f"Updated list: {lst}")


def handle_insert(lst):
    """
    Insert a value at a specific index in the list.

    Args:
    - lst (list): The list to modify.
    """
    try:
        index = int(input("Enter the index to insert the value: "))
        value = input("Enter the value to insert: ")
        lst.insert(index, value)
        print(f"Updated list: {lst}")
    except ValueError:
        print("Invalid index. Please enter a valid number.")


def handle_remove(lst):
    """
    Remove the first occurrence of a value from the list.

    Args:
    - lst (list): The list to modify.
    """
    value = input("Enter the value to remove: ")
    try:
        lst.remove(value)
        print(f"Updated list: {lst}")
    except ValueError:
        print(f"Value '{value}' not found in the list.")


def handle_pop(lst):
    """
    Pop a value from the list at a specified index.

    Args:
    - lst (list): The list to modify.
    """
    index_input = input("Enter the index to pop (leave blank to pop last item): ")
    try:
        if index_input:
            index = int(index_input)
            lst.pop(index)
        else:
            lst.pop()
        print(f"Updated list: {lst}")
    except IndexError:
        print("Index out of range.")
    except ValueError:
        print("Invalid index. Please enter a valid number.")


def handle_clear(lst):
    """
    Clear all items from the list.

    Args:
    - lst (list): The list to clear.
    """
    lst.clear()
    print(f"List cleared. Updated list: {lst}")


def handle_index(lst):
    """
    Find the index of the first occurrence of a value in the list.

    Args:
    - lst (list): The list to search.
    """
    value = input("Enter the value to find the index of: ")
    try:
        index = lst.index(value)
        print(f"Index of '{value}': {index}")
    except ValueError:
        print(f"Value '{value}' not found in the list.")


def handle_count(lst):
    """
    Count the number of occurrences of a value in the list.

    Args:
    - lst (list): The list to search.
    """
    value = input("Enter the value to count: ")
    count = lst.count(value)
    print(f"Count of '{value}': {count}")


def handle_sort(lst):
    """
    Sort the list in ascending order.

    Args:
    - lst (list): The list to sort.
    """
    try:
        lst.sort()
        print(f"List sorted. Updated list: {lst}")
    except TypeError:
        print("List contains non-comparable items and cannot be sorted.")


def handle_reverse(lst):
    """
    Reverse the order of the list.

    Args:
    - lst (list): The list to reverse.
    """
    lst.reverse()
    print(f"List reversed. Updated list: {lst}")


def handle_copy(lst):
    """
    Create a shallow copy of the list.

    Args:
    - lst (list): The list to copy.
    """
    copied_list = lst.copy()
    print(f"Copied list: {copied_list}")


def main():
    """
    Main function to interact with the user and perform list operations.
    """
    initial_values = input("Enter initial list values (comma-separated): ")
    lst = initial_values.split(',')

    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")
        if choice == '1':
            handle_append(lst)
        elif choice == '2':
            handle_extend(lst)
        elif choice == '3':
            handle_insert(lst)
        elif choice == '4':
            handle_remove(lst)
        elif choice == '5':
            handle_pop(lst)
        elif choice == '6':
            handle_clear(lst)
        elif choice == '7':
            handle_index(lst)
        elif choice == '8':
            handle_count(lst)
        elif choice == '9':
            handle_sort(lst)
        elif choice == '10':
            handle_reverse(lst)
        elif choice == '11':
            handle_copy(lst)
        elif choice == '12':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
