# Single Sign On

It's form of authentication in which multiple services can make use of a single server, called identity server to authenticate users to their serivices. The service server gets the  users credentials and sends it to the identity server. The identity server then authenticates the user and sends back a token to the service server. The service server then uses this token to authenticate the user.
There will be multiple service servers and a single identity server.

## Advantages

- Single point of authentication.
- Centralized user management.
- Users can use a single username and password to access multiple services.

There are two types of SSO:
    1) OAuth
    2) SAML

### OAuth

I've already wrote about Oauth.

### SAML

Security Assertion Markup Language (SAML) is an open standard for exchanging authentication and authorization data between parties, in particular, between an identity provider and a service provider. SAML is an XML-based markup language for security assertions (statements that service providers use to make access-control decisions).Basically the same stuff as the start of this doc.