import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):

    # Shuffle the input in place
    i = 0 
    n = len(the_list)
    
    while i < n: 
        # which element will take i-th place
        new_idx = get_random(i, n-1)
        the_list[i], the_list[new_idx] = the_list[new_idx], the_list[i]
        i+=1         
    
    pass



sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)