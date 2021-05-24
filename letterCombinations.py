def letterCombinations(digits):
    digit_dict = {
        '2': ['a', 'b', 'c'], 
        '3': ['d', 'e', 'f'], 
        '4': ['g', 'h', 'i'], 
        '5': ['j', 'k', 'l'], 
        '6': ['m', 'n', 'o'], 
        '7': ['p', 'q', 'r', 's'], 
        '8': ['t', 'u', 'v'], 
        '9': ['w', 'x', 'y', 'z']
        }
    
    current_list = []
    for digit in digits: 
        if not current_list:
            current_list = digit_dict[digit]
        else: 
            new_list = []
            for combo in current_list:
                new_list.extend([''.join([combo, letter]) for letter in digit_dict[digit]])
            current_list = new_list 
    
    return current_list 
                
