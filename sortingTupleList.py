def sort_by_last_element(tuples_list):
    for i in range(len(tuples_list)):
        for j in range(len(tuples_list) - i - 1):
            if tuples_list[j][-1] > tuples_list[j + 1][-1]:
                tuples_list[j], tuples_list[j + 1] = tuples_list[j + 1], tuples_list[j]
    return tuples_list

sample_list = [(2, 7), (3, 1), (4, 6), (2, 3), (2, 1)]
sorted_list = sort_by_last_element(sample_list)
print("Expected Result :", sorted_list)