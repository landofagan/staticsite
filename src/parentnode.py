from htmlnode import HTMLNode
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag=tag, children=children, value=None, props=props)
    def to_html(self):
        if self.tag is None:
            raise ValueError('Parent Node without a tag')
        elif self.children is None or len(self.children) == 0:
            raise ValueError('Parent Node with no children')
        html_string = f'<{self.tag}>'
        for child in self.children:
            childstr = child.to_html()
            html_string += childstr

        html_string += f'</{self.tag}>'
        return html_string
