from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



#using template and passing some data

@app.route('/index')
def test():
    return render_template('index.html' , list_of_names= ['chris', 'Ben'])
 


""" 
#variable passing using url

@app.route('/<string:name>')
def showingName(name):
    return f"hello {name}"
"""

if __name__ == "__main__":
    app.run(debug=True , port = 4000)




# Template
    #  we can add base html file using block content and extends keyword using template to create a boiler plate for 
    # every html page


# request_method 
    # is used for using http method like get and post request using flask
    # redirect and url_for  is used for redirection after something done
    # just check at  28:38



# web form starts at 29:00


