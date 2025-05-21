import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        prop_data = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=prop_data)
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')
    def test_child_node(self):
        child = HTMLNode('a', 'Click Here', None, {'href': 'https://www.google.com'})
        parent = HTMLNode(children = [child])
        props_string = parent.children[0].props_to_html()
        self.assertEqual(props_string, ' href="https://www.google.com"')
    def test_printing(self):
        node = HTMLNode(tag = 'a', value='Click Here', children = None, props = None)
        print(node)
if __name__ == "__main__":
    unittest.main()
