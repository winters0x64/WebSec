# Same origin policy

SOP is a browser-side concept or a rule that restricts resource sharing to the same origin.

Same origin policy is a  policy that defines that a particular information on a website can be accessed only if its from the same origin, that is it should be from the same domain(no subdomains) having the same port number, having same protocol.

Many people assume that the web browser same origin policy prevents all communication between separate domains on the web unless relaxed via CORS. This is not true. If the same origin policy was a file permission, it would be -WX (write & execute). You can write (POST) content to other domains, for example via form submission or AJAX. You just cannot read the results. Similarly you can execute, i.e. load javascript or CSS from other domains. The only thing it prevents is javascript from reading cross-domain content. You can even display cross-domain content, for example in <img> tags, as long as javascript does not have access to it