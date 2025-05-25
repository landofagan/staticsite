import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestNodeSplitter(unittest.TestCase):
    def test_it_returns_a_list_of_nodes(self):
        nodes = [
        ]
        split_list = split_nodes_delimiter(nodes, '**', TextType.BOLD)
        self.assertIsInstance(split_list, list)
        for node in nodes:
            self.assertIsInstance(node, TextNode)

    def test_supported_delimeters(self):
        with self.assertRaises(ValueError):
            split_nodes_delimiter(['test'], '', TextType.BOLD)

    def test_bold(self): # Going to assume it works for italic and code.
        node = [TextNode('Some **BOLD** text.', TextType.TEXT)]
        split_nodes = split_nodes_delimiter(node,'**',TextType.BOLD)

        self.assertEqual(split_nodes[0].text, 'Some ')
        self.assertEqual(split_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(split_nodes[1].text, 'BOLD')
        self.assertEqual(split_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(split_nodes[2].text, ' text.')
        self.assertEqual(split_nodes[2].text_type, TextType.TEXT)

    def test_unmatched_delimiter(self):
        with self.assertRaises(ValueError):
            node = [TextNode('testing an **unclosed delimiter', TextType.TEXT)]
            split_nodes_delimiter(node, '**', TextType.BOLD)

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
if __name__ == "__main__":
    unittest.main()
