def two_sum(nums, target):
    number_to_index = {}
    for index, number in enumerate(nums):
        difference = target - number
        if difference in number_to_index:
            return [number_to_index[difference], index]
        number_to_index[number] = index
    return []
