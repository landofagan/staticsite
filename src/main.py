from textnode import TextNode, TextType
from enum import Enum
def main():
    node = TextNode('some anchor shit', TextType.LINK, 'https://fucku.org')
    print(node)
main()
