def main():
    """
    Ideally, this code is meant to isolate and identify skipped numbers, to collect them and sum them,
    then subtract them from the total of the original list. If the answer is the sum of all selected numbers,
    then removing the sum all skipped numbers from the sum of the original list leaves us with nothing but the solution.
    """

    given_list = [0, 24, 17, 15, 61, 49, 61, 8, 65, 43, 26, 99, 7, 57, 97, 50, 93, 6, 82, 52]
    skipped_numbers = []
    list_sum = sum(given_list)
    average = list_sum / len(given_list)
    skipped_number_total = sum(skipped_numbers)

    print(skipped_numbers)
    print(average)
    print(skipped_number_total)
    print(list_sum)
    print(skipped_number_total - list_sum)
    print(given_list[0])
    print(given_list[1])
    if given_list[0] > given_list[1]:
        skipped_numbers.append(given_list[0])
    for x in range(len(given_list)):
        while x < (len(given_list) - 1):
            if given_list[x] < average and given_list[x + 2] < average and given_list[x + 1] > average:
                skipped_numbers.append(given_list[x + 1])
            elif given_list[x] < average and given_list[x + 2] < average and given_list[x + 1] < average:
                if given_list[x] < given_list[x + 1] and given_list[x + 2] < given_list[x + 1]:
                    skipped_numbers.append(given_list[x + 1])
                else:
                    continue
            elif given_list[x] > average and given_list[x + 2] > average and given_list[x + 1] > average:
                if given_list[x] < given_list[x + 1] and given_list[x + 2] < given_list[x + 1]:
                    skipped_numbers.append(given_list[x + 1])
                else:
                    continue
            else:
                continue
    print(skipped_numbers)
    print(average)
    print(skipped_number_total)
    print(list_sum)
    print(skipped_number_total - list_sum)
    return (skipped_number_total - list_sum)

if __name__ == '__main__':
    main()

'''
abandon all hope ye who enter here: the first item in the list is always 1 and the last number must be landed on, it is a simple greater than comparison combined with a running total sum.
'''