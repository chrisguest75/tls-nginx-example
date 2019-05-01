#!/usr/bin/env bash

if [ -f .env ]; then
    echo "Importing .env file"
    source "./.env"
fi

if [ ! -z "${DEBUG_ENVIRONMENT}" ];then 
    env
    export
fi

if [ -z "${DOMAIN}" ];then 
    export DOMAIN="chrisguest.internal"
fi
if [ -z "${SUBJECT}" ];then 
    export SUBJECT="chrisguest.internal"
fi
echo "DOMAIN is set: ${DOMAIN}"
echo "SUBJECT is set: ${SUBJECT}"

pushd ./certs
./generate_certs.sh
./generate_dhparam.sh
popd

cp ./nginx/nginx.conf.template ./nginx/nginx.conf
if [[ $(uname) == 'Linux' ]]; then
    sed -i "s/%DOMAIN%/${DOMAIN}/g" ./nginx/nginx.conf 
elif [[ $(uname) == 'Darwin' ]]; then
    sed "s/%DOMAIN%/${DOMAIN}/g" ./nginx/nginx.conf.template > ./nginx/nginx.conf
fi