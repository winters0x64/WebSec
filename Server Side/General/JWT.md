# JSON WEB TOKEN(JWT)

So the traditional way of authorisation is by creating a session cookie and then assgining a session id to each of the authenticated users and in subsequent request the authenticated users sends the session id with which the server checks if the user is actually logged in or not, Here the info about the authenticated user is stored on the server side but in JWT we actually store these data on the client side, and on every subsequent request we'll send the JWT token with the request and the server actually verifies that the data in the token has not been tampered with 
by verfying the hash of the jwt token with the hash stored in the server. Hence the client can't tamper with the data stored in jwt token.


This is a jwt token:

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

This is its deserialized version:

Header
{
  "alg": "HS256",
  "typ": "JWT"
}

Payload
{

  "sub": "1234567890",

  "name": "John Doe",

  "iat": 1516239022

}

HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  jwt secret key
  
) 

So if the user tampers with the jwt data the hash that the client is sending will change(as hash is calculated from Header and Payload as seen above ) hence
won't match with the hash stored on the server hence the jwt token is declared invalid.