# Make file to compress and join all JS files
all: compress_js compress_css

compress_js:
	java -jar ~/bin/yuicompressor.jar js/htmltidypanel.js > js/htmltidypanel.min.js

compress_css:
	java -jar ~/bin/yuicompressor.jar --type css css/htmltidypanel.css > css/htmltidypanel.min.css
