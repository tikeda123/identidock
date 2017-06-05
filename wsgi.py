from flask import Flask,Response
import requests

application = Flask(__name__)
default_name = 'Joe Bloggs'

@application.route('/')
def get_identicon():
    name    = default_name
    header  = '<html><head><title>Identidock</title></head><body>'
    body    = '''<form method="POST">
                Hello <input type="text" name="name" value="{}">
                <input type="submit" value="submit">
                </form>
                <p>You look like a:
                <img src="/monster/monster.png"
                '''.format(name)
    footer  = '</body></html>'

    return header + body + footer


if __name__ == '__main__':
    application.run()
