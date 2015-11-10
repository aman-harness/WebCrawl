# WebCrawl
A web - scraper built using scrapy framework in python.
<ul>
<li> Item file conatins the container that will be loaded with scraped data. They are just like a normal python dict.
   Modify it according to the data you need to scrap from a web page.
<li> Spider are the classes used to scrape information from a domain(Or a group of domains).
   They define an initial list of URLs to download, how to follow links, and how to parse the contents of those pages to extract items.<br>
   Note: Remeber to use DOWNLOAD_DELAY >= 2 sec else your IP could be blacklisted.
</ul>   
  
<Strong> How To Run:  </Strong> Go to projects top level directory and type in terminal :- scrapy crawl \<projectname\> <br>
Replace project name wih you the name you gave to your project while creating it.
  
<Strong> Dependencies:  </Strong> Before running this project or any scrapy project you must have <a href="http://doc.scrapy.org/en/0.24/intro/install.html#installing-scrapy">these</a>  packages intalled.

<Strong> To Do: </Strong> Use MongoDB for storing data in the database and use Stack_spider for doing the nested crawling.

Reference: https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/


