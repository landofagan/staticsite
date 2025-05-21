
class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError()
    def props_to_html(self):
        value = ''
        if self.props is None:
            return value
        for prop in self.props:
            value += ' ' + prop + '="' + self.props[prop] + '"'
        return value
    def __repr__(self):
        return f'HTMLNode: Tag "{self.tag}", Value "{self.value}, Children "{self.children}", Props <{self.props_to_html()}> '
