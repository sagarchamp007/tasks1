import math
import sys


def print_proximity(str_values_ls, index, n):
    '''
    prints the n <user defined> closest strings based on weights.
    Traverses left and right side parallely , takes O(n<user defined>)
    time complexity.
    '''
    r_index = index + 1
    l_index = index - 1
    ls_len = len(str_values_ls)
    cur = str_values_ls[index]
    count = 0
    print("{} -> ".format(cur["string"]), end="")
    while (l_index >= 0 and r_index < ls_len and count < n):
        if (str_values_ls[r_index]["weight"] - cur["weight"] <
                cur["weight"] - str_values_ls[l_index]["weight"]):
            print(str_values_ls[r_index]["string"], end=" ")
            r_index += 1

        else:
            print(str_values_ls[l_index]["string"], end=" ")
            l_index -= 1
        count += 1

    # if no elements on right,print left side elements
    while (count < n and l_index >= 0):
        print(str_values_ls[l_index]["string"], end=" ")
        l_index -= 1
        count += 1

    # if no elements on left side print right side elements
    while (count < n and r_index < ls_len):
        print(str_values_ls[r_index]["string"], end=" ")
        r_index += 1
        count += 1
    print()


def get_ascii_ls(string_ls):
    '''
    return list of weight for input string list.
    weight - sum of ascii value of characters in string.
    '''
    for string in string_ls:
        ascii_sum = sum(map(lambda x: ord(x), list(string)))
        ascii_sum = (ascii_sum)
        yield ascii_sum


def map_values(string_ls):
    ''' return list of dict where dict has string, weight keys.'''
    columns = ["string", "weight"]
    ascii_ls = get_ascii_ls(string_ls)
    string_weights = []
    for values in zip(string_ls, ascii_ls):
        feature_dict = dict(zip(columns, values))
        string_weights.append(feature_dict)
    return list(string_weights)


def make_string_ls(inp_file):
    with open(inp_file, "r") as f:
        str_ls = f.readlines()
        str_ls = map(lambda x: x.strip(), str_ls)

    return list(str_ls)


if __name__ == "__main__":
    try:
        inp_file, n = sys.argv[1], sys.argv[2]
    except IndexError:
        print("Usage : python <prog_name> <inp_file> <N>")
        sys.exit()
    n = int(n)
    str_ls = make_string_ls(inp_file)
    str_values_ls = map_values(str_ls)
    str_values_ls.sort(key=lambda x: x.get("weight"))
    print(str_values_ls)
    ls_len = len(str_values_ls)
    for index in range(ls_len):
        print_proximity(str_values_ls, index, n)
