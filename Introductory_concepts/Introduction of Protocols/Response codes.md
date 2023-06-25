# Response codes

When a page is requested to a web server, a three digit HTTP Response Status Code is returned as the first characters. This code denotes the status or what is going to be the next move.

The status codes can be interpreted as:

10x - I(Server) am still processing your request, its current status is...
20x - Everything went smooth, here is your page
30x - The page is currently not here. The new page is located at...
40x - Oops! You(Client) made some mistake
50x - Oops! I(Server) made some mistake