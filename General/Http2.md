# HTTP2 (rfc - 7540)

## What's up with tcp and http2?

http 2 tries to maintain as much as backwards compatibility to http 1.1 as possible. Most of the application layer features are the same but underhood where tcp lives have some changes.

### Pipelining (http 1.1) vs Multiplexing(http 2)

http 0.9 had only support for the GET method which was changed with http 1 which had the support for POST method, http 1.1 solved the connection timeout issue with http 1 with the introduction of persistent connections ```Connection : keep-alive```. Pipeline is a feature when a persistent http connection is made we can make use of the same connection(TCP connection) to multiple request and get the responses in the same order as we sent the request. For example this would be possible

```
GET /test.php HTTP 1.1
Host: lol.lol

GET /ok.php HTTP 1.1
Host: lol.lol
```

and we will get the responses in the same order in a single http connection.

Persistent connections solved the problem of opening multiple tcp connections and if you're using https you'll have to start an additional tls layer which would be constly.

To address this http2 introduces multiplexing in which it makes frames out of request/response and organize these frames into streams (corresponding to the request-response pair) We can send another request, and it is not necessary to wait for the previous answer.

**ADVANTAGES**

So in practice the advantage of http2 is that it can make use of a single TCP connection to make requests for lets say 10 resources(ie 10 independent requests) and get the response in any order and it doesn't have to wait for any particular reponse to come before going on to the next response, however in http1.1 with pipelining the order of responses needed to match the order of requests so if one response lagged for some reason then it'll affect the overall loading time. 

Mentioned above, http2 achives multiplexing by splitting the request and responses into frames which are later organized into streams identified by a stream number, and the server will send the responses as frames in any arbitary order and the browser will reconstruct the request according to the stream number.

This is the main advantage of http2.


### Header Compression

HTTP2 uses HPACK to compress header fields, it uses huffman encoding to reduce individual transfer sizes. On top of  that HPACK also uses a static and dynamic table to reduce the size of headers. ie Binary framing layers also in multiplexing.


### Server Push

Normally when a request is made to the server it'll respond back with an html file and the client's browser parses this html to DOM and then makes subsequent request to fetch additional resources which are mentioned in the DOM, this will also increase load times, so instead of this the http2 uses server push when a client makes a request for index.html the server will send all the related css,js files along with the request so the load times would be less the request doesn't have to wait for the DOM to parse and then send the request. This is done via utilizing the Link http header.

```
Link: "https://example.com/css/styles.css; rel=preload; as=style"
```


# Encryption 

HTTP2 does support tls, but it's possible to work with it without the use of tls, which reduces the cost of creating a tls session hence making the latency even less.