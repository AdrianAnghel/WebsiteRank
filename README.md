

# WebsiteRank

This is a client - server application for a website rank.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python 3.4.3 to run this project. No other external library is needed.



## How to use it.

You need to run both the client (in client\sender.py) and server (in server\controller\main.py

From client in terminal you can send website link.
```
http://www.example.com?SESSIONID=a25asvsd&x=15
```

Or you can send a bulk of websites, separated by ;
```
http://www.example.com?SESSIONID=a25asvsd&x=15 ; http://www.example.com?SESSIONID=b25asvsd&x=15 ; http://www.example1.com?SESSIONID=a25asvsd&x=15 ; http://www.example2.com?SESSIONID=a25asvsd&x=15 ; http://www.example2.com?SESSIONID=b25asvsd&x=15 ; http://www.example.com?SESSIONID=a25asvsd&x=15 ; http://www.example.com?SESSIONID=a25asvsd&x=16 ; http://www.example.com?SESSIONID=c25asvsd&x=16
```
The client sends this information as a POST request.

When you do a GET request, you will get a top of websites, sorted by the most accessed ones from the start and from the last minute.

GET request (for localhost; default port is 8000)
```
http://localhost:8000/
```

GET Response
```
 All time top:
['6:example.com', '4:example2.com', '3:google.com', '2:example1.com']
 Last minute top:
['3:example.com', '2:example2.com', '1:example1.com']
```

The SESSIONID in the parameters is mandatory. Base on this value, the rank is established.

If the same domain and the same SESSIONID is send twice, if it is in the same minute(time interval), it will only be considered once. Otherwise, if you have different time intervals, it will be considered by the number of appearances.

## Author

* **Adrian Anghel** - *Initial work* - (https://github.com/AdrianAnghel)


