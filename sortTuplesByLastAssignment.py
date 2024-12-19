def sort_by_last_element(tuples_list):
    def last_element(t):
        return t[-1]
    return sorted(tuples_list, key=last_element)

def remove_duplicates_preserve_order(input_list):
    seen = set()
    return [x for x in input_list if not (x in seen or seen.add(x))]

# Sample List for Sorting Tuples
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Get the sorted list
sorted_list = sort_by_last_element(sample_list)
print("Expected Result for Sorted Tuples:", sorted_list)

# Sample List for Removing Duplicates
input_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
unique_list = remove_duplicates_preserve_order(input_list)
print("Expected Result for Unique List:", unique_list)
