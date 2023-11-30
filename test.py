list_of_dicts_1 = [
    {'a': 1},
    {'d': 4},
    {'f': 6}
]

list_of_dicts_2 = [
    {'a': 1},
    {'d': 4},
    {'f': 6},
    {'a': 1},
    {'f': 6},
    {'g': 7}
]

# Extract key-value pairs from the dictionaries in list_of_dicts_1
pairs_list_1 = [list(d.items())[0] for d in list_of_dicts_1]

# Extract key-value pairs from the dictionaries in list_of_dicts_2
pairs_list_2 = [list(d.items())[0] for d in list_of_dicts_2]

# Count the total number of items from list_of_dicts_1 that match any item in list_of_dicts_2
total_matches = sum(pair in pairs_list_2 for pair in pairs_list_1)

print("Total number of items from list_of_dicts_1 that match list_of_dicts_2:", total_matches)
