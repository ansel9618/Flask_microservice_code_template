from user_country_init import manageApp
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'common'))
app = manageApp()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


'''---------------------DOC--------------------------
The code imports the manageApp class from the user_country_init module, which is used to create and configure the Flask application. 
It also imports the os and sys modules to set up the system path.

The code then creates an instance of the manageApp class, which creates a Flask app, registers the Blueprints, 
and performs any other necessary initialization steps.

Finally, the code checks if the module is being run as the main program, and if so, runs the Flask application with the 
run method, specifying the host and port number. The host is set to 0.0.0.0, which means the application will listen for 
requests from any IP address, and the port number is set to 5000, which is a common port number used for Flask applications.
'''