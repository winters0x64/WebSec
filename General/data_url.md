# Data URL

A Data URL is a special type of URL that directly contains data in the form of text, images, audio, or any other binary data. This data can be included in the URL itself, without the need to link to an external resource. This means that the data can be embedded directly into a web page, making it available without any additional network requests.

Think of it as a way to store data within a URL instead of in a separate file. So, instead of linking to an external file (such as an image file), you can embed the data for that image directly in the URL.

The format of a Data URL starts with data: followed by the MIME type, which specifies the type of data being encoded (e.g. image/jpeg for a JPEG image), followed by a comma, and then the actual data encoded as a base64 string.

For example, the following is a Data URL for a simple text message:

eg: 

data:text/plain,Hello%20World