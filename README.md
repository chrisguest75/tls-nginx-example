# README.md
This repo demonstrates a few TLS features of nginx.  

* HTTP to HTTPS redirection
* TLS protocols and ciphers definitions
* HSTS - Strict Transport Security 
* Reverse proxy definition

# Environment
Create a file called .env

Add the following exports to it.  Feel free to change the information. 
 
```
export DOMAIN=chrisguest.internal
export SUBJECT="/C=UK/ST=Berkshire/L=Reading/O=DevOps/CN=${DOMAIN}"
```

# Generate Self-signed Certs
To run this locally on docker-compose you'll first need to generate a self signed cert

NOTE: This will create a certificate for chrisguest.internal 
The dhparams key can take about 5-10 mins on my MacBook Pro. 

```
./generate.sh
```

# Running
The example uses port http:8080 and https:8443.  Please ensure these are free of other service bindings. 

```
docker-compose up -d --build
```

# Name Resolution through hosts
You can update your local hosts file for name resolution.
To update your hosts file for chrisguest.internal or the domain you chose earlier.

## Ubuntu Hosts
```
cat /etc/hosts
sudo nano /etc/hosts
open https://chrisguest.internal:8443/
```

## MacOS Hosts
```
cat /etc/hosts
sudo nano /etc/hosts
sudo killall -HUP mDNSResponder 
open https://chrisguest.internal:8443/
```

# Trusted Certificates

## Ubuntu Certificate Trust
NOTE: Check that you are not overwriting an existing cert before copying this file over.
```
ls /usr/local/share/ca-certificates 
sudo cp ./certs/tls.crt /usr/local/share/ca-certificates/tls.crt
sudo update-ca-certificates 
```

## MacOS Certificate Trust
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

## Test MySQL writes
Use a mySQL client.  Remember to use the mySQL8 driver as the client auth is different to 5.7.

After invoking the mirror route a few times. 
Check the requests table in the requests_tracking DB.

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
