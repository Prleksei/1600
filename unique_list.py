def unique_list(start_list):
    result = []
    for item in start_list:
        if item not in result:
            result.append(item) 
test_list = [1, 2, 3, 4, 5, 1, 2, 3]
print(unique_list(test_list))
