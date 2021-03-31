# It is possible to build a URL dynamically, by adding variable parts to the rule parameter.
# This variable part is marked as <variable-name>. It is passed as a keyword argument to the 
# function with which the rule is associated.

# In the following example, the rule parameter of route() decorator contains <name> variable part attached to URL ‘/hello’. 
# Hence, if the http://localhost:5000/hello/Tutorial is entered as a URL in the browser, ‘Tutorial’ will be supplied 
# to hello() function as argument.

from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run(debug = True)


# Save the above script as hello.py and run it from Python shell. Next, open the browser and enter URL http://localhost:5000/hello/Tutorial
# The following output will be displayed in the browser.

# OUTPUT : Hello Tutorial!