
# Day 15: OpenID Connect (OIDC) Investigation

## 1. Objective

Investigate Google's publicly available OpenID Connect configuration and JSON Web Key Set (JWKS). Understand how OIDC supports authentication and how public keys are used to verify ID token signatures.

## 2. Environment

- Operating System: Ubuntu on WSL2
- Working directory: ~/cybersecurity/day15
- Tools: Linux terminal, curl, Python 3, JSON module
- Target: Google's public OIDC discovery and JWKS endpoints

## 3. OAuth 2.0 vs OpenID Connect

OAuth 2.0 provides delegated authorization, allowing applications to access permitted resources.

OpenID Connect builds an identity layer on OAuth 2.0, allowing applications to authenticate users and receive identity claims.

## 4. Important Token Concepts

### Access Token
Used to access protected resources through an API.

### ID Token
Communicates authentication and identity information to the OIDC client.

### Important JWT Claims

- iss: Identity provider that issued the token.
- sub: Identifier of the authenticated subject.
- aud: Intended recipient of the token.
- exp: Token expiration time.
- iat: Token issuance time.
- nonce: Connects an authentication request to the returned ID token.

## 5. Discovery Investigation

Retrieved Google's public discovery document from:

https://accounts.google.com/.well-known/openid-configuration

Findings:

- Issuer: https://accounts.google.com
- Authorization endpoint: https://accounts.google.com/o/oauth2/v2/auth
- Token endpoint: https://oauth2.googleapis.com/token
- UserInfo endpoint: https://openidconnect.googleapis.com/v1/userinfo
- JWKS URI: https://www.googleapis.com/oauth2/v3/certs
- Supported signing algorithm: RS256
- Supported scopes included openid, email and profile.
- PKCE challenge methods included plain and S256.

## 6. JWKS Investigation

Retrieved the public key document from:

https://www.googleapis.com/oauth2/v3/certs

The document contained two RSA public keys when inspected.

Important fields:

- kid: Identifies a particular public key.
- kty: Specifies the key type.
- alg: Specifies the signing algorithm.
- use: Indicates the key's intended use.
- n: RSA public modulus.
- e: RSA public exponent.

The published public keys can be used by applications to verify token signatures.

## 7. Python Automation

Created inspect_jwks.py to:

- Load the JWKS JSON document.
- Count the available public keys.
- Display key identifiers.
- Display key types and algorithms.
- Display public key usage and exponent information.

## 8. Security Risks

Potential OIDC implementation vulnerabilities include:

1. Missing ID token signature validation.
2. Incorrect issuer validation.
3. Incorrect audience validation.
4. Missing nonce validation.
5. Weak redirect URI validation.
6. Trusting unverified email addresses.
7. Exposure of authentication tokens.

## 9. Security Recommendations

- Verify ID token signatures using trusted public keys.
- Validate issuer, audience and expiration claims.
- Validate nonce values against the original authentication request.
- Use secure redirect URI validation.
- Prefer Authorization Code Flow with PKCE using S256.
- Protect tokens from exposure in URLs, logs and insecure storage.
- Never trust identity information simply because it appears in a decoded JWT.

## 10. Conclusion

This investigation demonstrated how an OIDC provider publishes authentication configuration and public signing keys.

The practical work improved my understanding of identity verification, JWT claims, public-key cryptography, Linux command-line tools and basic Python automation.

The investigation was limited to publicly available configuration documents. No private accounts or authentication tokens were accessed.

## 11. Practical Verification Results

Executed the Python inspection script successfully.

Results:
- Number of public keys detected: 2
- Key type: RSA
- Signing algorithm: RS256
- Key usage: sig
- Public exponent: AQAB

The script inspected public key metadata. It did not perform cryptographic signature verification.

The number of published keys may change when the identity provider rotates its signing keys.
