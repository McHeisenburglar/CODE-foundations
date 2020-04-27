import http.server
import socketserver

# A simple script to use the python CGI server in python3
# Using CGIHTTPRequestHandler in place of SimpleHTTPRequestHandler
# allows python scripts to be called as an action (POST)

# define the handler to be the CGI server
handler = http.server.CGIHTTPRequestHandler

# point the handler to a directory with scripts
handler.cgi_directories = ["/cgi-scripts"]

# define the server using the handler
# PORT = int(input("Specify port: "))
PORT = 8000
httpd = socketserver.TCPServer(("0.0.0.0", PORT), handler)

# Set variables which the CGIHTTPRequestHandler expects
httpd.server_name = "myServer"
httpd.server_port = PORT

print("staring CGI server...")

class Restaurant:
	def __init__(self, name, neighborhood):
		self.name = name
		self.neighborhood = neighborhood

restaurants = []

f_txt = open("restaurants.txt")
f_lines = f_txt.read().splitlines()
for line in f_lines:
	d = line.split(',')
	restaurants.append(Restaurant(d[0], d[1]))
f_txt.close()


html_list = ""
for restaurant in restaurants:
	html_list += f"""
		<li>
				<h2>{restaurant.name}</h2>
				<h3>{restaurant.neighborhood}</h3>
		</li>
	"""

f_html = open("index.html", "w")
f_html.write(f"""<!DOCTYPE html>
<html>
<head>
	<title>Restaurants</title>
</head>
<body>
	<div id="main">
		<h1>Restaurants in Berlin</h1>
		<ul>
			{html_list}
		</ul>
	</div>
</body>
</html>""")
f_html.close()

# run the server. To kill it, issue Ctrl + C
httpd.serve_forever()
