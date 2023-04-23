# Nonce

While using CSP we might not wanna allow inline scripts to be executed therefore we might give a CSP header as "default-src" as "None"
but we might wanna allow specific inline scripts to be executed these might be the scripts that we might have written. So there we use something called as a Nonce which would be cryptographic hash and this is generated in the backend and given to certian scripts as an attribute like ```<script nonce="8IBTHwOdqNKAWeKl7plt8g=="></script>``` the nonce attribute is hidden for obvious security reasons.
