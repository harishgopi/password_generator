# password generator
## A random strong password generator api

## system limitations
All the limitations are handled as bad request rather than providing a limited output with warning message.
- password minimum length, special character length and numbers length cannot exceed 2000
- sum of special characters and numbers length should not exceed 2000
- number of passwords per API hit cannot exceed 1000

## deployment in kubernetes

default image is harishgopi/password_generator

```sh
cd kubernetes
kubectl apply -f app_deployment.yaml
```

## build and push image to your repo

```sh
cd backend
docker build . -t <repo>:<tag>
```

## run as docker container

```sh
docker run -p 5000:5000 -d harishgopi/password_generator:latest
```