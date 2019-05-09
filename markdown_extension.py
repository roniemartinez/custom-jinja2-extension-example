#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __license__ = "MIT"
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
import codecs

from jinja2 import nodes
from jinja2.ext import Extension
from markdown2 import Markdown


class MarkdownExtension(Extension):
    tags = {'markdown'}

    def __init__(self, environment):
        super(MarkdownExtension, self).__init__(environment)
        environment.extend(
            markdown_dir='markdowns'
        )

    def parse(self, parser):
        line_number = next(parser.stream).lineno
        md_file = [parser.parse_expression()]
        return nodes.CallBlock(self.call_method('_to_html', md_file), [], [], []).set_lineno(line_number)

    def _to_html(self, md_file, caller):
        with codecs.open('{}/{}'.format(self.environment.markdown_dir, md_file), 'r', encoding='utf-8') as f:
            return Markdown().convert(f.read())
