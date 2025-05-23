from textnode import TextNode, TextType
def main():
    node = TextNode('some anchor shit', TextType.LINK, 'https://fucku.org')
    print(node)
main()
