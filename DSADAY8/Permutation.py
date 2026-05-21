from itertools import permutations

def generate_permutations(number):
    number_str = str(number)
    perm = permutations(number_str)
    perm_list = [''.join(p) for p in perm]

    return perm_list


print(generate_permutations(234))