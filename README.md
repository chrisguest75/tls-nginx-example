# README.md
This repo demonstrates a few TLS features of nginx.  

* HTTP to HTTPS redirection
* TLS protocols and ciphers definitions
* HSTS - Strict Transport Security 
* Reverse proxy definition

# Generate Self-signed Certs
To run this locally on docker-compose you'll first need to generate a self signed cert

NOTE: This will create a certificate for chrisguest.internal 

```
cd certs
./generate_certs.sh
```

# Running
```
docker-compose up -d --build
```

## MacOs Trusted
### MacOS Hosts
You can update your local hosts file for name resolution.
To update your hosts file for chrisguest.internal.

cat /etc/hosts
sudo nano /etc/hosts
sudo killall -HUP mDNSResponder 
open https://chrisguest.internal:8443/

### Certificate Trust
You can add the certificate to the keychain.  This will mean it will be trusted by Safari and Chrome.  

# Testing 

```
|----------------------------------------------|-------------------------------|
| Test                                         | Outcome                       |
|----------------------------------------------|-------------------------------|
| curl https://chrisguest.internal:8443/       | HTML Response                 |
| open https://chrisguest.internal:8443/       | HTML Response                 |
| curl https://chrisguest.internal:8443/mirror | JSON Mirror Response          |
| open https://chrisguest.internal:8443/mirror | JSON Mirror Response          |
|                                              |                               |
|----------------------------------------------|-------------------------------|
```

Test the mirror service.
curl -X POST http://localhost:5000 -d '{"sf":3}'  --header 'content-type: application/json' | jq


# Cleanup
```
docker-compose down
```
