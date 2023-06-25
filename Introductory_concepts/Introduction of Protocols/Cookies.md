# Cookie

A piece of data that a server sends to a user's web browser.

The browser may store the cookie and send it back to the same server with later requests.

Cookies are used for session management, authentication, tracking, etc.

Set-Cookie response header from the server is used to set a cookie on the browser
Cookie header is used to send cookies to the server.

Why do we use cookies

HTTP is stateless connection protocol, i.e , the server cannot differentiate between different connections of different users.

SameSite Cookies

SameSite attribute prevents the browser from sending this cookie along with cross-site requests. The main goal is to mitigate the risk of cross-origin information leakage. Possible values for the attribute are:
lax -> allows the cookie to be sent with these top-level navigations. (default)
strict -> Cookies will only be sent in a first-party context and not be sent along with requests initiated by third party websites
None -> Cookies will be sent in all contexts. If SameSite=None is set, the cookie Secure attribute must also be set