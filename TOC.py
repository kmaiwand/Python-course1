#!c:/Program Files/Python3/python.exe
#!/usr/bin/python3

with open( "Assets/slides.js") as f:
	data = f.readlines()
	
slides = data[0][12:-3].split( ',')  # cut "var slides= [" and the trailing "];"
#print('slides:', slides, '\n')
slides = [ el.replace("[", "").replace("'", "").replace("]", "") for el in slides]
pairs = []
for i in range( 0, len(slides), 2):
   pairs.append( ( slides[i].strip(), slides[i+1].strip()))
#print( 'pairs:', pairs)

listing = ''
for slide in pairs:
	listing += "\t\t<li><a href='" + slide[0] + "' class='link'>" + slide[1] + '</a></li>' + '\n'
#print( 'listing:', listing)

print( """Content-type: text/html\n
<!DOCTYPE html>
<html lang="en-US">
<head> 
	<title>Contents</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link href="Assets/favicon.ico" rel="icon" />
	<link href="Assets/slides.css" rel="stylesheet" />
	<script>
		function move(e){{
			if( e.keyCode == 37) prev( file_name());
			if( e.keyCode == 39) next( file_name());
		}};
		document.onkeydown = move;
	</script>
	<script src="Assets/slides.js"></script>
</head><body>
	<h1>Contents</h1>
	<ul>
{}
	</ul>
	<footer>
		<a href='#' id='left' title='Left arrow for previous' onclick="prev( file_name())"><img src='Assets/icon_left.png' alt='Previous' /></a>
		<a href='#' id='right' title='Right arrow for next' onclick="next( file_name())"><img src='Assets/icon_right.png' alt='Previous' /></a>
	</footer>
</body>
</html>\
""".format( listing))
