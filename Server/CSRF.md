# CSRF(CROSS SITE REQUEST FROGERY) Token

CSRF token is a unique token generated by the server to identify which domain is sending the request,So an attacker's website cannot make requests with elevated previlages. The server checks if the client sending request has the correct csrf token (It compares the token that is stored on the server with the token that the client is sending).
