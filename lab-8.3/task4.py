import unittest
# Class under test
class ShoppingCart:
    def __init__(self):
        self.items = []  # list of (name, price)
    def add_item(self, name, price):
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be numeric")
        self.items.append((name, price))
    def remove_item(self, name):
        for i, (item_name, price) in enumerate(self.items):
            if item_name == name:
                self.items.pop(i)
                return
        # If not found, ignore (graceful handling)
    def total_cost(self):
        return sum(price for _, price in self.items)
class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
    def test_empty_cart_total(self):
        self.assertEqual(self.cart.total_cost(), 0)
    def test_add_single_item(self):
        self.cart.add_item("Apple", 1.5)
        self.assertEqual(self.cart.total_cost(), 1.5)
    def test_add_multiple_items(self):
        self.cart.add_item("Apple", 1.5)
        self.cart.add_item("Banana", 2.0)
        self.cart.add_item("Orange", 3.0)
        self.assertEqual(self.cart.total_cost(), 6.5)
    def test_remove_existing_item(self):
        self.cart.add_item("Apple", 1.5)
        self.cart.add_item("Banana", 2.0)
        self.cart.remove_item("Apple")
        self.assertEqual(self.cart.total_cost(), 2.0)
    def test_remove_nonexistent_item(self):
        self.cart.add_item("Apple", 1.5)
        self.cart.remove_item("Water")  # should not raise error
        self.assertEqual(self.cart.total_cost(), 1.5)
    def test_add_duplicate_items(self):
        self.cart.add_item("Apple", 1.5)
        self.cart.add_item("Apple", 1.5)
        self.assertEqual(self.cart.total_cost(), 3.0)
    def test_remove_one_of_duplicates(self):
        self.cart.add_item("Apple", 1.5)
        self.cart.add_item("Apple", 1.5)
        self.cart.remove_item("Apple")
        self.assertEqual(self.cart.total_cost(), 1.5)
    def test_add_zero_price_item(self):
        self.cart.add_item("Coupon", 0)
        self.assertEqual(self.cart.total_cost(), 0)
    def test_add_negative_price_item(self):
        self.cart.add_item("Discount", -5)
        self.assertEqual(self.cart.total_cost(), -5)
    def test_empty_cart_after_removals(self):
        self.cart.add_item("Apple", 1.5)
        self.cart.remove_item("Apple")
        self.assertEqual(self.cart.total_cost(), 0)
if __name__ == "__main__":
    # Define the missing ShoppingCart class so tests can run
    class ShoppingCart:
        def __init__(self):
            self.items = []
        def add_item(self, name, price):
            self.items.append((name, price))
        def remove_item(self, name):
            for i, (item_name, price) in enumerate(self.items):
                if item_name == name:
                    self.items.pop(i)
                    return
        def total_cost(self):
            return sum(price for _, price in self.items)

    unittest.main()