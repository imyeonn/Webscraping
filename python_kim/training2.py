html="""
<html>
     <head>
          <title> test web </title>
     </head>
     <body>
          <p align="center"> text contents </p>
          <img src="c:\Python34\Koala.jpg" width="500" height="300">
     </body>
</html> """

from bs4 import BeautifulSoup
bs=BeautifulSoup(html)
print(bs.prettify() )

bs.find('title')
