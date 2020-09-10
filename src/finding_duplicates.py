# The task:
# Given list with n + 1 entries and numbers 1 - n, one number is duplicated,
# find it

def find_duplicate_v1(in_list):
    duplicates = []
    for i in range(len(in_list)):
        for j in range(i+1, len(in_list)):
            if in_list[i] == in_list[j]:
                duplicates.append(in_list[i])
    return duplicates


def find_duplicate_v2(in_list):
    duplicates = []
    while len(in_list) > 0:
        num = in_list[0]
        in_list.pop(0)
        if num in in_list:
            duplicates.append(num)
    return duplicates


def find_duplicate_v3(in_list):
    duplicates = []
    for i in range(len(in_list)):
        if in_list[in_list[i] - 1] < 0:
            duplicates.append(in_list[i])
        in_list[in_list[i] - 1] *= -1
    return duplicates


if __name__ == "__main__":
    in_list = [1, 3, 2, 4, 5, 2]
    print(find_duplicate_v3(in_list))
