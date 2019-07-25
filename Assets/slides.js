var slides= [ ['about.html', 'About the Course'], [ 'TOC.py', 'Table of Contents'], [ 'program.html', 'Why program?'], [ 'install.html', 'Installing Python'], [ 'using-idle.html', 'Using IDLE'], [ 'vars.html', 'Variables'], [ 'nums.html', 'Numbers'], [ 'strings.html', 'Strings'], [ 'flow.html', 'Flow Control'], [ 'condition.html', 'Conditions'], [ 'lists.html', 'Lists'], [ 'functions.html', 'Functions'], [ 'modules.html', 'Modules'], [ 'files.html', 'Working with Files'], [ 'resources.html', 'Resources'], [ 'next_steps.html', 'Next Steps'] ];

function find_it( url){
	var i;
	for (i = 0; i < slides.length; i++) { 
		if( slides[i][0] === url)
			return i;
	};
};

function prev(curr){
	var curr_ind = find_it( curr);
	if( curr_ind > 0) 
		window.location.href = slides[curr_ind-1][0];
};

function next(curr){
	var curr_ind = find_it( curr);
	if( curr_ind != slides.length-1 && curr_ind != -1)
		window.location.href = slides[curr_ind+1][0];
};

function show_hide( id) {
	var code = document.getElementById( id);
	if( code.style.display === "none") {
		code.style.display = "block";
	} else {
		code.style.display = "none";
	};	
};

function file_name() {
	var url = window.location.pathname; 
	var filename = url.substring(url.lastIndexOf('/')+1); 
	return filename;
};
