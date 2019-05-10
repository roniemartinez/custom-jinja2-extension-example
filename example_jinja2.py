#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __license__ = "MIT"
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
from jinja2 import Environment

from markdown_extension import MarkdownExtension


def main():
    template = Environment(extensions=[MarkdownExtension]).from_string("""
    {% markdown "ABOUT.md" %}
    """)
    print(template.render())


if __name__ == '__main__':
    main()
