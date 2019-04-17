# Setting up Laravel Instance using Docker in Local Machine

----
## Use [Docker Compose](https://docs.docker.com/compose/install/) to build docker image and create docker container
```bash
docker-compose build --force-rm
docker-compose up -d
```

## Update storage and cache folders permissions
```bash
cd ../
sudo chmod 0777 storage bootstrap/cache -R
```

## Add .env file
```bash
APP_NAME=SOP-WebClient
APP_ENV=local
APP_KEY=base64:P4wQnUvYU+urr58kG9HeDgkZri70Gm4nJR77Je3iK5A=
APP_DEBUG=true
APP_URL=https://localhost:447

LOG_CHANNEL=stack

BROADCAST_DRIVER=log
CACHE_DRIVER=file
QUEUE_CONNECTION=sync
SESSION_DRIVER=file
SESSION_LIFETIME=120

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379

PUSHER_APP_ID=
PUSHER_APP_KEY=
PUSHER_APP_SECRET=
PUSHER_APP_CLUSTER=mt1

MIX_PUSHER_APP_KEY="${PUSHER_APP_KEY}"
MIX_PUSHER_APP_CLUSTER="${PUSHER_APP_CLUSTER}"

```

Wait for 1-2 mins then check https://localhost:447

## install composer dependencies and npm packages
``` bash
cd ../
composer install
npm install

```