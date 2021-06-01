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
