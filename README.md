# simple-web-crawler
Simple web crawler written in Python with help of BeautifulSoup (and Flask!)

This program uses Flask to be exposed like an API and crawls any website. 
It retrieves the links to the pages but also to JS, CSS and image files.

To run it, you'll need Python 3 installed and also Flask and BeautifulSoup.

## Installing dependencies

To install Python 3, please check the official website: https://www.python.org/

Also, check BeautifulSoup and Flask pages to follow the specific steps to your OS:

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

https://flask.palletsprojects.com/en/1.1.x/installation/#

## Running the program

In your Terminal, go to the project folder and run the "app.py" file:

```python3 app.py```

Usually, Flask runs on port 5000, so when you run the program, you should be able to access it through:

http://localhost:5000/

## Hitting the API

The program have only one endpoint, and it expects a GET request with two parameters: domain link and depth.
Example:

```http://localhost:5000/?domain=http://mywebsite.com/&depth=0```

It returns a list of links with all the JS links, CSS links, Image links and also the depth of the page related to
the link provided. 
