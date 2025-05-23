import unittest

from parentnode import ParentNode
from leafnode import LeafNode
class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_tag_validation(self):
        with self.assertRaises(ValueError):
            child_node = LeafNode("span", "child")
            node = ParentNode(None, [child_node])
            node.to_html()

    def test_child_validation(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, None)
            node.to_html()

        with self.assertRaises(ValueError):
            node = ParentNode(None, [])
            node.to_html()
