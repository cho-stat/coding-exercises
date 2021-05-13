import unittest


def change_possibilities(amount, denominations):
    
    if amount == 0: 
        # can always make zero change 
        return 1

    # Calculate the number of ways to make change
    if len(denominations) == 0: 
        return 0
    
    min_denom = min(denominations)
    if min_denom > amount: 
        # no way to make change
        return 0 
    
    times = amount // min_denom 
    # since amount >= min_denom, times > 0 
    
    ways_to_make_change = 0
    
    for i in range(times+1): 
        new_amt = amount - i*min_denom 
        new_denoms = [ x for x in denominations if x != min_denom ]
        ways_to_make_change += change_possibilities(new_amt, new_denoms)
    
    return ways_to_make_change















# Tests

class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = change_possibilities(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = change_possibilities(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = change_possibilities(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = change_possibilities(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = change_possibilities(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = change_possibilities(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)