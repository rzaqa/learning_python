def find_smallest(data_list:list)-> int:
    smallest = data_list[0]
    smallest_index = 0
    for i in range(1, len(data_list)):
        if data_list[i] < smallest:
            smallest = data_list[i]
            smallest_index = i
    return smallest_index

print(find_smallest([2,3,4,1,5,6,7,8,9]))

def selection_sort(data_list:list) -> list:
    new_data = []
    for _ in range(len(data_list)):
        smallest = find_smallest(data_list)
        new_data.append(data_list.pop(smallest))
    return new_data

print(selection_sort([11,6,9,0,8,1,14,15,2,3,4,7,12,13,5,10]))


# =======================================================================

def improved_selecting_sorting(data:list) -> list:
    new_data = []

    def find_smallest(data: list)-> int:
        smallest_index = 0
        smallest_number = data[0]

        for i in range(1, len(data)):
            if data[i] < smallest_number:
                smallest_index = i
                smallest_number = data[i]

        return smallest_index

    for _ in range(len(data)):
        smallest = find_smallest(data)
        new_data.append(data.pop(smallest))
    return new_data

assert improved_selecting_sorting([3, 7, 1, 9, 11, 13, 17,5, 19, 23]) == [1, 3, 5, 7, 9, 11, 13, 17, 19, 23]