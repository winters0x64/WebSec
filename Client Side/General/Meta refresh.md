# Meta refresh

<meta http-equiv="refresh" content="0;url=http://site/webhook">

meta tags define the metadata for a website, the http-equiv attribute specifies the values which could be used as headers often CSP is delievered through the meta tags.

This tag is quite useful, if we have an html injection but if the CSP is strict and won't allow any script exections we could use this tag to cause a redirection.
