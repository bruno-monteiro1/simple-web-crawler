# simple-web-crawler
Simple web crawler written in Python with help of BeautifulSoup (and Flask!)

This program uses Flask to be exposed like an API and crawls any website. 
It retrieves the links to the pages but also to JS, CSS and image files.

You can check it out here: 

https://simple-web-crawler.herokuapp.com/

## Hitting the API

The program have only one endpoint, and it expects a GET request with two parameters: domain link and depth.
Example:

```https://simple-web-crawler.herokuapp.com/crawl?domain=http://nubank.com.br/&depth=0```

You can call it with your browser, but something like Postman may be a better choice, since the visualization of the result will be better. 

The endpoint returns a list of links with all the JS links, CSS links, Image links and also the depth of the page related to the link provided. 

## Running locally

To run it locally, you'll need Python 3 installed and also Flask and BeautifulSoup.

### Installing dependencies

To install Python 3, please check the official website: https://www.python.org/

Also, check BeautifulSoup and Flask pages to follow the specific steps to your OS:

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

https://flask.palletsprojects.com/en/1.1.x/installation/#

### Running the program

In your Terminal, go to the project folder and run the "app.py" file:

```python3 app.py```

Usually, Flask runs on port 5000, so when you run the program, you should be able to access it through:

http://localhost:5000/