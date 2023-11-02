# Cache Headers

```
If-None-Match: W/"653dc5d2-5887"
If-Modified-Since: Sun, 29 Oct 2023 02:39:14 GMT
```

Basically, if the server sends 304 not modified response the browser checks if the
DOM has been modified after the time specified in 'If-Modified-Since' if it's not modified then it'll load the response from the cache itself if it is modified the server will send back the request content with a "200" code.

