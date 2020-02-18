#!/usr/bin/env python3

import cgitb
import cgi
cgitb.enable()

print("Content-Type: text/html")    # HTML is following
print()

form = cgi.FieldStorage()
names = None
generation_1 = None

# if form:
# 	if 'name' in form or 'generation' not in form
# 	split_names = form['name'].value.split('.')
# 	i = 0
# 	while i < len(split_names):
# 		split_names[i] = split_names[i].capitalize()
# 		i += 1
# 	names = ' '.join(split_names)
# 	generation_1 = form['generation'].value
# else:
# 	names = 'stranger'
# 	generation_1 = 'CODE'

if 'name' in form:
	split_names = form['name'].value.split('.')
	i = 0
	while i < len(split_names):
		split_names[i] = split_names[i].capitalize()
		i += 1
	names = ' '.join(split_names)
else:
	names = 'stranger'

if 'generation' in form:
	generation_1 = f"#{form['generation'].value}"
else:
	generation_1 = 'CODE'


# first_name = names[0].capitalize()
# last_name = names[1].capitalize()
print(f'''
<!DOCTYPE html>
<html>
<head>
	<title>Forms Basics</title>
	<link rel="stylesheet" type="text/css" href="/style-animate.css"/>
	<link href="https://fonts.googleapis.com/css?family=Roboto+Slab:300,400,500,600,700,800&display=swap" rel="stylesheet">
</head>
<body style="background-color: #1C2838; color: white;">
	<div id="container">
		<img class="icon" src="https://cdn.glitch.com/6fe427ae-d3ba-45f3-8041-3a10617d2a8d%2Fguy-fawkes.svg?v=1581947192302">
		<h1 style="margin-top: 80px;" class="animate-fade-up">Welcome, {names}.</h1>
		<h2 class="animate-fade-up">Glad you've joined your <strong>{generation_1}</strong> brethren.</h2>
		<form action="/">
			<button class="animate-fade-in" type="submit">Go back</button>
		</form>
		<script> </script>
	</div>
</body>
</html>''')