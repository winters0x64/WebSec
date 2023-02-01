# Sessions

Once a client connects first time to a server, the server generates a new session id, which later will be sent to the client as a cookie value.

From then on, this session-id will identify that client connection

Now for each session-id, the server keeps some data structure, which enables the server to store data specific to a user

Cookies Vs Sessions

The main difference between a session and a cookie is that a cookie has data that is directly stored on the user's browser but a session is saved in the backend server and the reference to that data is stored on the user's end. A session will end when a browser gets closed.