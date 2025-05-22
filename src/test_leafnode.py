import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_to_html_without_props(self):
        node = LeafNode('b', 'WOAH')
        self.assertEqual(node.to_html(), '<b>WOAH</b>')

    def test_to_html_with_props(self):
        node = LeafNode('a', 'Click me!', {'href':'https://www.google.com'})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_value_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode(None,None)
            node.to_html()

if __name__ == "__main__":
    unittest.main()
