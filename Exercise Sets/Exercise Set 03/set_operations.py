#Set Operations
set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

first_diffset = set1.difference(set2)
second_diffset = set2.difference(set1)
print('Set Difference\n',first_diffset)
print(second_diffset, '\n')

union_ = set1.union(set2)
print('Union Set\n',union_, '\n')

first_symdeff = set2.symmetric_difference(set1)
second_symdeff = set1.symmetric_difference(set2)
print('Syemmetric Difference\n',first_symdeff)
print(second_symdeff, '\n')

first_set_inter = set1.intersection(set2)
second_set_inter = set2.intersection(set1)
print('Set Intersectin\n',first_set_inter)
print(second_set_inter)