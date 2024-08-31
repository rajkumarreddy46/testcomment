import unittest

def greet(name):
    return f"Hello, {name}!"

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")

if __name__ == '__main__':
    unittest.main()

