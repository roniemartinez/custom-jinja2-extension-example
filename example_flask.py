#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __license__ = "MIT"
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
from flask import Flask, render_template

application = Flask(__name__)
env = application.jinja_env
env.add_extension('markdown_extension.MarkdownExtension')


@application.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    application.run(debug=True, threaded=True)
