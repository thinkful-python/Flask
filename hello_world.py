#!/usr/bin/python

from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
    
@app.route("/hello/<name>") 
def hi_mentor(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a pug.  Awww...
        </p>
        <img src="http://d21vu35cjx7sd4.cloudfront.net/dims3/MMAH/thumbnail/645x380/quality/90/?url=http%3A%2F%2Fs3.amazonaws.com%2Fassets.prod.vetstreet.com%2F3a%2F54%2F5ae8bfcc41b381c27a792e0dd891%2FAP-KWDHXS-645sm8113.jpg">
    """
    return html.format(name.title())
    
@app.route("/jedi/<firstname>/<lastname>")
def jedi_name(firstname,lastname):
    html = """
         <h1> Welcome!
         <p> Your Jedi name is {}!!! </p>
         </h1> 
         """
    return html.format(lastname[0:3]+firstname[0:2])
        

if __name__ == "__main__":
    app.run(host=environ['IP'],
        port=int(environ['PORT']))
