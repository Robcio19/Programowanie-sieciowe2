from flask import Flask
from flask import render_template
app = Flask(__name__)
import socket

@app.route("/")
def hello():
    #return "Hello World!"
    #my_ip=get_ip()
    return render_template('index.html', my_ip=get_ip(), moja_suma=12 , moja_roznica=odejmowanie() )
	
	
@app.route("/test")
def test():
    return "Test adresu!"
	
def odejmowanie():
    a = 100
    b =40
    return str(a-b)
	
def get_ip():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname (host_name)
    return ip_address
	

@app.route("/suma")
def suma():
    a = 11
    b = 22
    return str(a + b)
	
@app.route("/iloczyn")
def iloczyn():
    a = 5
    b = 6
    return str(a * b)
	
if __name__ == '__main__':
    app.run()
	

	