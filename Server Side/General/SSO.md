# Single Sign On

It's form of authentication in which multiple services can make use of a single server, called identity server to authenticate users to their serivices. The service server gets the  users credentials and sends it to the identity server. The identity server then authenticates the user and sends back a token to the service server. The service server then uses this token to authenticate the user.
There will be multiple service servers and a single identity server.

## Advantages

- Single point of authentication.
- Centralized user management.
- Users can use a single username and password to access multiple services.

There are mainly two types of SSO:
    1) OAuth
    2) SAML

### SAML

Security Assertion Markup Language (SAML) is an open standard for exchanging authentication and authorization data between parties, in particular, between an identity provider and a service provider. SAML is an XML-based markup language for security assertions (statements that service providers use to make access-control decisions).Basically the same stuff as the start of this doc.

## How it works

1. User tries to access a service.
2. The service server sends a request to the identity server.
3. The identity server authenticates the user and sends back a SAML assertion in xml form to the service server.
4. The service server then uses this Assertion to authenticate the user.


## Oauth

Oauth provides authorization to third party apps to user accounts without giving the username and password. It is mainly used for authorization and not for authentication. 

## Whats the difference between Oauth and SAML?

- Oauth is mainly used for authorization and not for authentication.
- SAML is mainly used for authentication and not for authorization.
- Oauth is mainly used for third party apps to access user accounts.
- SAML is mainly used for single sign on.
- Oauth is token based(access token).
- SAML is XML based(Saml assertion).


