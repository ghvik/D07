# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(lst):
    index = 0
    while index < len(lst) - 1:
        if lst[index] > lst[index + 1]:
            return False
        index += 1
    return True

def main():
    # Commented test cases below
    # print(is_sorted([1, 2, 3]))
    # print(is_sorted([[1, 2, 3], [4, 5], [6]]))
    # print(is_sorted(["apple", "banana", "carrot"]))
    pass

    
if __name__ == "__main__":
    main()