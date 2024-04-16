# Top 10 Web Bugs of 2023

A deeper of the most interesting bugs on the web that were presented in 2023.

## 1) SOP bypass in chrome

CVE 2022-4908

Same Origin VS Same Site

https://example.com and https://www.example.com are not same origin since the subdomains are different, hence they are cross origin.(Subdomain also matters). Same origin would mean that the domain name would be same, same protocol and same port as well.

But inorder for something to be samesite on the other side means the protocol and the tld or the etld(extended top level domain) should be same. So https://example.com:1234 and https://example.com:1111 are diffrent origins but is the samesite.

etlds case is a bit different when it comes to samesite essentially, example1.com and example2.com are different cross sites and cross origin similarily site1.gitlab.io and site2.gitlab.io here etld is gitlab.io

Navigation API replaces the old History api, can be used to intercept client navigations and can view past navigation entries, provided that these navigations are same origin, these can also leak sensitive info such as auth tokens in URL's(ctf idea).

### Exploit

When an iframe is framed inside a target window, they should be cross-origin samesite in this case. then if inside the iframe the user makes any navigations it'll be stored under navigation.entries(), Now if the target location of the iframe is changed into 'about:blank'
then all the navigation.entries() gets stored under the root windows navigation.entries() array. Hence whatever navigations that the user had made in the framed window is exposed outside the frame, bypasing  SOP. This also works If we open another window with a reference in the current window(window.opener()) then change its location to 'about:blank' and then we'll have access to the navigation.entries() for the opened window SOP is bypassed. 

### What i learned from this?

More about navigation api,site,origin. 
Every single website can be hacked with this, that is super cool.




## Can i speak to your manager?

Registers & Registrars

Registrars communicate with the corresponding Registers to update the domains that they own, they make use of a protocol named EPP protocol( Extensible Provisioning Protocol (EPP)), which uses XML to communicate, in this case the registry server was running an EPP client from CoCCA Registry Software(Java) which was vulnerable to XXE and they also found a lfi in the system, which led to pwning multiple domains.

### What i learned from this?

Java still strong, practical side of XXE.


## 2) Cookies In Crumbles(Later)


## 3) 