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


class TransformError(Exception):

    def __init__(self, message, source):
        Exception.__init__(self, message)
        self.source = source

    def __str__(self):
        return self.message + '\n' + self.source


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

    PREFIX = '/** @jsx React.DOM */'

    def __call__(self, app, doctree, docname):
        script = []

        for block in doctree.traverse(jsx_block):
            source = block.rawsource

            if not block.attributes['hidesource']:
                replacement = literal_block(source, source)
                block.replace_self(replacement)
            else:
                block.parent.remove(block)

            if not block.attributes['showsourceonly']:
                try:
                    js = jsx_transformer.transform_string(
                        self.PREFIX + source)[len(self.PREFIX):]
                    script.append(js)
                except jsx.TransformError as e:
                    raise TransformError(e.message, source)

        if script:
            script = self.SCRIPT_TEMPLATE % '\n'.join(script)
            node = raw('', script, format='html')
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
        node = jsx_block(text, text,
            hidesource='hidesource' in self.options,
            showsourceonly='showsourceonly' in self.options,
        )
        return [node]


def setup(app):
    app.connect('doctree-resolved', JSXInjector())
    app.add_directive('jsx', JSXDirective)

