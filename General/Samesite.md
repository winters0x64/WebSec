# The samesite attribute for cookies

Samesite is kind of a security measure implemented on cookies mostly to prevent csrf attacks

The samesite attribute for cookies has three values 1)Strict  2)Lax  3)None

1) Strict

So lets say website "a" has a cookie called "auth", when a website "b" makes a request to website "a" the cookie won't be send along with the request, Even if it's top level navigation. cookies can only be send along with the request from the same origin and not from a third party website.

2) Lax

So in lax, when website "b" makes a request to website "a" the cookies will be send along with the request only if it's a top level navigation, or if it's a get request cookies won't be send for POST request or any other methods.(This is the default if samesite attribute is not set)

3) None

The cookies will send to website "a" from "b" no matter what the request type is whether it is get post or anything this was the defaul before lax.


TOP LEVEL navigation changes the URL in your address bar. Resources that are loaded by iframe, img tags, and script tags do not change the URL in the address bar so none of them cause TOP LEVEL navigation.