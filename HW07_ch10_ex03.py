# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def cumulative_sum(lst):
    if len(lst) <= 1:
        return lst
    else:
        # Recursive step.
        sum_so_far = cumulative_sum(lst[:-1])
        # Append the next sum to the list of sums.
        return sum_so_far + [sum_so_far[-1] + lst[-1]]
        
def main():
    # Commented test cases below:
    # print(cumulative_sum([1, 2, 3]))
    # print(cumulative_sum([3,5,-6]))
    # print(cumulative_sum([]))
    pass
    
if __name__ == "__main__":
    main()
    