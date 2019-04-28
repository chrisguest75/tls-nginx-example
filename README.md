# README.md
This repo demonstrates a few TLS features of nginx.  

* HTTP to HTTPS redirection
* TLS protocols and ciphers definitions
* HSTS - Strict Transport Security 
* Reverse proxy definition

# Generate Self-signed Certs
To run this locally on docker-compose you'll first need to generate a self signed cert

NOTE: This will create a certificate for chrisguest.internal 
The dhparams key takes about 15-20 mins on my MacBook Pro. 

```
cd certs
./generate.sh
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

## Simple tests
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

## Test the mirror service route.
```
curl -X POST https://chrisguest.internal:8443/mirror -d '{"sf":3}'  --header 'content-type: application/json' | jq
```
NOTE: You can view the DB and check the responses.

## Test DHParam
```
openssl s_client -connect chrisguest.internal:8443 -cipher "EDH" | grep "Server Temp Key"
```

## Test supported protocols and ciphers
```
nmap --script ssl-enum-ciphers -p 8443 chrisguest.internal
```


# Cleanup
```
docker-compose down
```
