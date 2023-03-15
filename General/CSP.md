# Content Security Policy (CSP)

So content security policy is a policy which is implemented mostly to prevent many attacks such as XSS, So  it's a header it defines the sources of scripts,images,media etc ie from where it should be loaded and it will only be loaded from the defined sources in the header if we give any other sources it will throw us an error.

Example 

Content-Security-Policy: default-src 'self'

So default src is the fallback that is used if the sources of some elements are not defined, ie if the script-src is not defined it will fallback to default-src, Here self means the websites own origin.

Another example is as follows 

Content-Security-Policy: default-src 'self'; img-src *; media-src example.org example.net; script-src userscripts.example.com
