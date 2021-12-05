import unittest
import day
import food_item

class TestDay(unittest.TestCase):

    def test_one_item_no_fat(self):
        oneDay = day.Day([food_item.FoodItem("Bread", 4, 0, 10, 30, 7)])
        solution = oneDay.solve();

        self.assertEqual(oneDay.result.success, False);
        self.assertEqual(solution, {'Bread': 0});

    def test_two_items(self):
        oneDay = day.Day([food_item.FoodItem("Avocado", 2, 5, 5, 20, 20),
                          food_item.FoodItem("Bread", 4, 0, 10, 30, 7)])
        solution = oneDay.solve();

        self.assertEqual(oneDay.result.success, True);
        self.assertEqual(solution, {'Avocado': 10, 'Bread': 25});

    def test_two_items_negative_expiry(self):
        oneDay = day.Day([food_item.FoodItem("Avocado", 2, 5, 5, 20, -10),
                          food_item.FoodItem("Bread", 5, 3, 10, 30, -7)])
        solution = oneDay.solve();

        self.assertEqual(oneDay.result.success, True);
        self.assertEqual(solution, {'Avocado': 20, 'Bread': 30});

    def test_zero_items(self):
        oneDay = day.Day([]);

        with self.assertRaises(ValueError):
            solution = oneDay.solve();
        

if __name__ == '__main__':
    unittest.main()
        
        
