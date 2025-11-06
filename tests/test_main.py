import unittest
from statuscodechecker.__main__ import parse_cli_args

class TestParseCliArgs(unittest.TestCase):
    def test_no_values(self):
        ints, invalid = parse_cli_args(['main.py'])
        self.assertEqual(ints, [])
        self.assertEqual(invalid, [])

    def test_all_valid_integers(self):
        ints, invalid = parse_cli_args(['main.py', '200', '404', '500'])
        self.assertEqual(ints, [200, 404, 500])
        self.assertEqual(invalid, [])

    def test_some_invalid_values(self):
        ints, invalid = parse_cli_args(['main.py', '200', 'abc', '404', 'xyz'])
        self.assertEqual(ints, [200, 404])
        self.assertEqual(invalid, ['abc', 'xyz'])

    def test_all_invalid_values(self):
        ints, invalid = parse_cli_args(['main.py', 'foo', 'bar'])
        self.assertEqual(ints, [])
        self.assertEqual(invalid, ['foo', 'bar'])

    def test_mixed_types(self):
        ints, invalid = parse_cli_args(['main.py', '123', '', '456', '7.89'])
        self.assertEqual(ints, [123, 456])
        self.assertEqual(invalid, ['', '7.89'])

if __name__ == '__main__':
    unittest.main()
