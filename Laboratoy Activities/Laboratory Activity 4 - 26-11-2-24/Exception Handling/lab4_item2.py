def main():
    try:
        size = int(input("Enter the size of the array: "))

        if size <= 0:
            print("The size must be greater than 0")
            return
        
        arr = [0.0] * size

        print("Enter the elements of the array: ")
        for i in range(size):
            arr[i] = int(input())

        pElement = int(input("Enter the index of the element to print: "))
        print(f"Element at index {pElement}:{arr[pElement] : .2f}")

    except IndexError:
        print(f"Index {pElement} is invalid.")

main()