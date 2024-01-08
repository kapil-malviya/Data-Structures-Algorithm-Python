'''
This Python program defines a class Permutations that generates all possible permutations 
of a given list. It utilizes a recursive approach to explore and generate permutations, and 
it employs backtracking to backtrack to previous states. The main driver code demonstrates 
the usage of this class by generating permutations for a specific list and length.

'''



class Permutations:
    def __init__(self):
        '''initialize Permutations class with an empty list to store permutations'''
        self.permutations_list = []

    def generate_permutations(self, input_list, r=None):
        '''
        generate permutations of a given list

        parameters:
        - input_list (list): input list for which permutations need to be generated
        - r (int): length of each permutation, if not provided, the default is the 
                   length of the input_list
        '''
        if r is None:
            r = len(input_list)
        self.generate_permutations_recursive(input_list, 0, r)

    def generate_permutations_recursive(self, input_list, start, r):
        '''
        recursively generate permutations of a given list

        parameters:
        - input_list (list): input list for which permutations need to be generated
        - start (int): the current index from which permutations should be generated
        - r (int): the length of each permutation.
        '''
        if start == r:
            self.permutations_list.append(self.copy_list(input_list[:r]))

        # recursive case: swap elements and explore permutations
        for i in range(start, len(input_list)):
            # swap elements at indices start and i
            input_list[start], input_list[i] = input_list[i], input_list[start]

            # recursively call the function with the updated start index
            self.generate_permutations_recursive(input_list, start + 1, r)

            # backtrack: swap elements back to their original positions
            input_list[start], input_list[i] = input_list[i], input_list[start]

    def copy_list(self, input_list):
        '''
        create a copy of the given list

        parameters:
        - input_list (list): the list to be copied

        returns:
        - list: the copied list
        '''
        return [element for element in input_list]

    def get_permutations(self):
        '''
        get the list of generated permutations

        returns:
        - list: list of permutations
        '''
        return self.permutations_list


my_list = [1, 2, 3, 4, 5]
r = 3
perm = Permutations()
perm.generate_permutations(my_list, r)

# display results
print('Permutations : ', perm.get_permutations())
print('Length : ', len(perm.get_permutations()))
