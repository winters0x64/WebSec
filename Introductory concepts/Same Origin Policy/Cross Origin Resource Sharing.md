# CORS

Same Origin Policy prevents reading data from two different domains. So,https://blog.az3z3l.io/  can't read data from https://blogposts.az3z3l.io/  even though they might be owned by the same person. CORS( Cross-Origin Resource Sharing) comes into play here.

Cross-Origin Resource Sharing (CORS) is an HTTP mechanism that uses HTTP headers to define origin permissions. Using CORS headers, you can inform the browser that resources from another origin have the rights to access resources on your page.

CORS allows us to bypass SOP(Same origin policy) and read data from a different site.

For example, a GET request to a site may be sent with an Origin request header that declares the exact origin

GET / HTTP/1.1
Host: www.example.com
(...)
Origin: http://example2.com

In response, the resource that supports CORS will send an Access-Control-Allow-Origin response header:

HTTP/1.1 200 OK
(...)
Access-Control-Allow-Origin: http://example2.com
(...)

The response header Access-Control-Allow-Origin can take in two types of values: a domain or a * . The * denotes that any domain can read data and adding the domain name allows access only to that domain name.

So, Access-Control-Allow-Origin allows us to only read data, it doesn't send the user's cookies along with the request. To do that, we use another header called Access-Control-Allow-Credentials with True as value. This allows sending the cookie along with the request.