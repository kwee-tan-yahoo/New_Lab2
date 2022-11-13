def display_main_menu():
    print("Sub: display_main_menu()")
    print("Enter some numbers separated by commas (eg: 5,67,32)")


def get_user_input():
    print("Sub: get_user_input()")
    # datalist = [int(x) for x in input().split(',')]
    inputstr = input()
    print("Input string =", inputstr)
    strlist = inputstr.split(',')
    print("After split:", strlist)
    datalist=[] # Create an empty list
    for x in range(0, len(strlist)):
        datalist.append(int(strlist[x])) # append element to the list
    print("Data List:", datalist)
    return datalist


def calc_average(inputlist):
    print("Sub: calc_average()")
    print(inputlist)
    print("List length=", len(inputlist))
    total = sum(inputlist)
    average = total / len(inputlist)
    print("Average is", average)
    return average


def find_min_max(inputlist):
    print("Sub: find_min_max()")
    print("Before sorting", inputlist)
    inputlist.sort()
    print("After sorting", inputlist)
    MinMaxList =[] # Create an empty list
    min = inputlist[0]
    max = inputlist[len(inputlist)-1]
    MinMaxList.append(min)  # append min element to the list
    MinMaxList.append(max)  # append max element to the list
    print("Min & Max :", MinMaxList)
    return MinMaxList


def sort_temperature(inputlist):
    print("Sub: sort_temperature()")
    print("Before sorting", inputlist)
    inputlist.sort()
    print("After sorting", inputlist)
    return inputlist


def calc_median_temperature(inputlist):
    print("Sub: calc_median_temperature()")
    inputlist.sort()
    listlen = len(inputlist)
    if (listlen % 2 == 0):
        median_index = int(listlen / 2)
    else:
        median_index = int((listlen - 1) / 2)

    print("Median index is", median_index)
    median = inputlist[median_index]
    print("Median is", median)
    return median


def main():
    # print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    print('===========')
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    find_min_max(num_list)
    sort_temperature(num_list)
    calc_median_temperature(num_list)


if __name__ == "__main__":
    main()

