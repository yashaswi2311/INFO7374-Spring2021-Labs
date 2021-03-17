## Elastic Search

Elasticsearch is an open source search engine highly scalable. It allows you to keep and analyse a great volume of information practically in real time. Elasticsearch works with JSON documents files. Using an internal structure, it can parse your data in almost real time to search for the information you need.

It is very useful when working with big data.

Some technical (but useful) information to know about Elasticsearch are:

- It is a real time distributed and analytics engine.
- It is open source, developed in Java.
- It uses a structure based on documents instead of tables and schema.
- Besides speed and scalability, it has high resiliency relating to failures, and it's really flexible relating to data type.


[1]

### Claat Document Link

https://codelabs-preview.appspot.com/?file_id=17id6QT4nz-ewQ7Py2l0Wu4YZaMiTZLLL2X88DKxPAkE#0

### Getting Started 

##### For Mac Users

If you have MacOS with Homebrew installed, you can install it by simply typing

brew install elasticsearch
brew install kibana

##### For Windows Users

Download the Elasticsearch

- Windows zip file from the Elasticsearch download page.
- Extract the contents of the zip file to a directory on your computer, for example, C:\Program Files.
- Open a command prompt as an Administrator and navigate to the directory that contains the extracted files, and run the batch file using command:

elasticsearch.bat

To test if it is running, open http://127.0.0.1:9200/

If it is successful, it would show something like this :

![Image of Elastic Running](https://imgur.com/hbNpbv6)

Download Kibana

- Windows zip file from the Kibana download page.
- Extract the contents of the zip file to a directory on your computer, for example, C:\Program Files.
- Open a command prompt as an Administrator and navigate to the directory that contains the extracted files

To test if it is running, open http://localhost:5601/

If it is successful, it would show something like this :

![Image of Kibana Running](https://imgur.com/bOb0xZd)



### More demos & useful resources

- [[1 ElasticSearch 101 – a getting started tutorial]](http://joelabrahamsson.com/elasticsearch-101/)
- [[2 Bool Query]](https://www.elastic.co/guide/en/elasticsearch/reference/6.8/query-dsl-bool-query.html)
- [[3 Using Elasticsearch, Kibana, and Python to easily navigate]](https://clubhouse.io/developer-how-to/using-elasticsearch-kibana-and-python-to-easily-navigate/)
- [[4 Elastic Search Tutorial]](https://tsh.io/blog/elasticsearch-tutorial/)
- [[5 Python and Elastic Search]](https://code-maven.com/python-elasticsearch)
