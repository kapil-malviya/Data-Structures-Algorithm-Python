class Permutations:
    def __init__(self):
        self.permutations_list = []

    def generate_permutations(self, input_list, r=None):
        if r is None:
            r = len(input_list)
        self.generate_permutations_recursive(input_list, 0, r)

    def generate_permutations_recursive(self, input_list, start, r):


        print('\ninput_list before if condition : ', input_list)
        print('start before if condition : ', start)
        print('r before if condition : ', r)
        print('permutation list at first : ', self.permutations_list)

        if start == r:
            self.permutations_list.append(self.copy_list(input_list[:r]))


        print('\ninput_list after if condition : ', input_list)
        print('start after if condition :', start)
        print('r after if condition : ', r)
        print('permutation list after if condition : ', self.permutations_list)


        # recursive case: Swap elements and explore permutations
        for i in range(start, len(input_list)):
            print('\nvalue of start inside for loop : ', input_list[start])
            print('value of i inside for loop : ', input_list[i])



            # swap elements at indices start and i
            input_list[start], input_list[i] = input_list[i], input_list[start]

            print('\nvalue of start inside for loop after swap : ', input_list[start])
            print('value of i inside for loop after swap : ', input_list[i])
            print('permutation list after first swap : ', self.permutations_list)

            # recursively call the function with the updated start index
            self.generate_permutations_recursive(input_list, start + 1, r)

            # backtrack: Swap elements back to their original positions
            input_list[start], input_list[i] = input_list[i], input_list[start]

            print('\nstart after last swap : ', input_list[start])
            print('i after last swap : ', input_list[i])
            print('permutation list after last swap : ', self.permutations_list)

    def copy_list(self, input_list):
        return [element for element in input_list]

    def get_permutations(self):
        return self.permutations_list

my_list = ['a', 'b', 'c']
r = 2
perm = Permutations()
perm.generate_permutations(my_list, r)

print('\n\t---------------\t\n')
print('Permutations : ', perm.get_permutations())
print('Length : ', len(perm.get_permutations()))