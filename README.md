# README.md
This repo demonstrates a few TLS features of nginx.  

# Generate Self-signed Certs
To run this locally on docker-compose you'll first need to generate a self signed cert

NOTE: This will create a certificate for chrisguest.internal 

```
cd certs
./generate_certs.sh
```

# Running
```
docker-compose up
```


## MacOS Hosts
You can update your local hosts file for name resolution.
To update your hosts file for chrisguest.internal.

cat /etc/hosts
sudo nano /etc/hosts
sudo killall -HUP mDNSResponder 
open https://chrisguest.internal:8443/

# Testing 
curl https://chrisguest.internal:8443/
curl -k http://localhost:8080
curl -k https://localhost:8443


# Cleanup
```
docker-compose down
```
