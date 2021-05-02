def get_max_profit(stock_prices):

    # Calculate the max profit

    # Keep two counters: 
    # One counter to keep track of buy index
    # One counter to keep track of sell index
    # Once a new low price is found 

    buy_price = stock_prices[0]
    sell_price = stock_prices[1]
    best_diff = sell_price - buy_price
    
    i = 2
    n = len(stock_prices)
    
    while i < n:
        
        price = stock_prices[i]
        
        # price as new sell price, same buy_price
        new_diff_old_buy = price - buy_price
        
        # price as new sell price, old sell_price = buy_price
        new_diff_new_buy = price - sell_price
        
        
        if best_diff < new_diff_old_buy and new_diff_old_buy >= new_diff_new_buy:
            # current price is a better sell price
            sell_price = price
            best_diff = sell_price - buy_price
            i += 1
        
        elif best_diff < new_diff_new_buy and new_diff_new_buy > new_diff_old_buy: 
            # sell price is a better buy price if
            # current price is the new sell price 
            buy_price = sell_price
            sell_price = price
            best_diff = sell_price - buy_price
            i += 1
        
        elif price < buy_price and i < n-1: 
            # current price is lower than buy price, 
            # and is not a better sell price 
            # begin a new search 
            buy_price = price 
            sell_price = stock_prices[i+1]
            
            new_diff = sell_price - buy_price
            if best_diff < new_diff: 
                best_diff = new_diff
            i += 2
        
        else: 
            i +=1
    
    return best_diff 
        
        
            


















# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_big_increase_then_small_increase(self):
        actual = get_max_profit([2, 10, 1, 4])
        expected = 8
        self.assertEqual(actual, expected)                

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)