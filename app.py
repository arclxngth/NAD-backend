from flask import Flask  

app = Flask(__name__)

@app.route("/")
def hello():
    # returning string
    return "<html>\
                <body>\
                    <h3><u>Hello World!</u></h3>\
                </body>\
            </html>"

app.run(debug = True) 