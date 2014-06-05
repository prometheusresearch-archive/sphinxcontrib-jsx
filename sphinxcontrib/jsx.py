"""

    jsx_directive
    =============

"""

from react import jsx

from docutils.parsers.rst import directives, Directive
from docutils.nodes import literal_block, raw


jsx_transformer = jsx.JSXTransformer()


class jsx_block(literal_block):
    """
    Represent a literal block, that contains JSX code
    """
    pass


class JSXInjector(object):
    """
    JSXInjector traverses the doctree and replaces all jsx_block node with
    literal_block nodes, collecting all js code and injecting raw html block
    node at the end.
    """

    SCRIPT_TEMPLATE = """
    <script>
    window.addEventListener("DOMContentLoaded", function() {
    %s
    });
    </script>
    """

    def __call__(self, app, doctree, docname):
        js = []

        for block in doctree.traverse(jsx_block):
            jsx = block.rawsource

            if not block.attributes['hidesource']:
                replacement = literal_block(jsx, jsx)
                replacement['language'] = 'javascript'
                block.replace_self(replacement)

            if not block.attributes['showsourceonly']:
                js.append(jsx)

        if js:
            js = '\n'.join(js)
            js = jsx_transformer.transform_string('/** @jsx React.DOM */' + js)
            js = self.SCRIPT_TEMPLATE % js
            node = raw('', js, format='html')
            doctree.children.append(node)


class JSXDirective(Directive):
    """
    JSXDirective represents a directive for constructing jsx_block
    """

    has_content = True
    option_spec = {
        'hidesource': directives.flag,
        'showsourceonly': directives.flag,
    }

    def run(self):
        text = '\n'.join(self.content)
        return [jsx_block(text, text,
            hidesource='hidesource' in self.options,
            showsourceonly='showsourceonly' in self.options)]


def setup(app):
    app.connect('doctree-resolved', JSXInjector())
    app.add_directive('jsx', JSXDirective)

