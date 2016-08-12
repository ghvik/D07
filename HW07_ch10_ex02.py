# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
    
def capitalize_nested(nested_list):
    capitalized = []
    for item in nested_list:
        if type(item) == list:
            capitalized.append(capitalize_nested(item))
        else:
            capitalized.append(item.capitalize())
    return capitalized
def main():
    # Test cases below
    # print(capitalize_nested(['apple', ['bear',['dog','animal']], 'cat']))
    # print(capitalize_nested(['dog','cat','box',[]]))
    pass

if __name__ == "__main__":
    main()