# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

html = '''
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>测试Html</title>
    <style>
        h1 {
        color: #333333;
        font-size:48px;
        text-shadow:3px 3px 3ps #666666;
        }
    </style>
    <script>
        function change() {
            document.getElementsByTagName('h1')[0].style.color = '#ff0000';
        }
    </script>
</head>
<body>
    <h1 onclick="change()">Hello,world!</h1>
</body>
</html>

'''

def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	# return [b'<h1>hello wsgi server </h1>']
	return [html.encode('utf-8')] # html内容