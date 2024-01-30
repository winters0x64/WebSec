# iframe

iframe is an html element which is used to embed content from a website in another website, websites could disable iframe that means you can no longer embed the website within your own website this is done as a security measure 

We can implement additional restrictions on an iframe using the "sandbox" attribute for example 
```
<iframe sandbox="allow-scripts"
srcdoc="<link rel='stylesheet' href='/public/axist.min.css' />{{ space }}" class="space"></iframe>
```
Here we're allowing only script execution and disabling everything else.

