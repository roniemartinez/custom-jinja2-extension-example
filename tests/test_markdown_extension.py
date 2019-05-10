#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
from jinja2 import Environment

from markdown_extension import MarkdownExtension


def test_markdown_file():
    template = Environment(extensions=[MarkdownExtension]).from_string("""{% markdown "HEADER.md" %}""")
    assert template.render().strip() == "<h1>Header Title</h1>"


def test_markdown_string():
    template = Environment(extensions=[MarkdownExtension]).from_string(
        """{% markdown %}# Header Title{% endmarkdown %}"""
    )
    assert template.render().strip() == "<h1>Header Title</h1>"


def test_markdown_empty_string():
    template = Environment(extensions=[MarkdownExtension]).from_string(
        """{% markdown %}{% endmarkdown %}"""
    )
    assert template.render().strip() == "<p></p>"
