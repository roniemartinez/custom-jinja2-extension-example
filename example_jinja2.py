from jinja2 import Environment

from markdown_extension import MarkdownExtension


def main():
    template = Environment(extensions=[MarkdownExtension]).from_string("""
    {% markdown "ABOUT.md" %}
    """)
    print(template.render())


if __name__ == '__main__':
    main()
