def splitted_input_ints():
    """
    This function should get an input as a list
    and transform everything in another list of
    integers ["1", "20", "3"] -> [1, 20, 3]
    """
    return [int(i) for i in input().split()]
def main():
    T = splitted_input_ints()
    elem_sum = 0
    for i in T:
        elem_sum = elem_sum + i
    print(elem_sum - 3)
if __name__ == "__main__":
    main()