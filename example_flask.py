from flask import Flask, render_template

application = Flask(__name__)
env = application.jinja_env
env.add_extension('markdown_extension.MarkdownExtension')


@application.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    application.run(debug=True, threaded=True)
