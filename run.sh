#!/bin/bash

docker > /dev/null 2>&1
if [ $? -ne 0 ]
then
    echo Docker is not installed.
fi

docker info > /dev/null 2>&1
if [ $? -ne 0  ]
then
    sudo $0 $@
    exit
fi

mkdir -p ~/.cooktheflag/

echo " - CookTheFlag running as $USER"
echo " - Shared folder: $HOME/.cooktheflag"

if [ $1 ] && [ $1 == "build" ]
then
    docker build -t cooktheflag .
    docker run --volume ~/.cooktheflag:/data -p 8080:8080 cooktheflag
else
    docker run --pull=always --volume ~/.cooktheflag:/data -p 8080:8080 azalo/cooktheflag
fi