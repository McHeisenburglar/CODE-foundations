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
PORT = int(input("Specify port: ") or 8000)
httpd = socketserver.TCPServer(("0.0.0.0", PORT), handler)

# Set variables which the CGIHTTPRequestHandler expects
httpd.server_name = "myServer"
httpd.server_port = PORT

print("staring CGI server...")

restaurants = []

csv = open("restaurants.csv")
for line in csv:
	restaurants.append(line.rstrip().split(','))

print(restaurants)

html_list = ""
for restaurant in restaurants:
	html_list += f"""
		<li>
				<h2>{restaurant[0]}</h2>
				<h3>{restaurant[1]}</h3>
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
