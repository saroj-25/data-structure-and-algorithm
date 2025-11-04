# linear search in an array


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return print(f"Element found at {i}th position")
    return -1


def binary_search(arr, target):
    arr.sort()

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return print(f"Element found at {mid}th position")

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    print("Element not found")


choice = int(input(("Enter your choice \n 1. Linear search \n 2. Binary Search \n ")))


arr = [10, 29, 23, 43, 22, 23]
target = 43

# call

match (choice):
    case 1:
        linear_search(arr, target)
    case 2:
        binary_search(arr, target)
    case default:
        print("Invalid choice")
