#!/usr/bin/env bash
openssl req -newkey rsa:2048 -nodes -keyout ./tls.key -x509 -days 365 -out ./tls.crt -subj "/C=UK/ST=/L=/O=/CN=chrisguest.internal"


