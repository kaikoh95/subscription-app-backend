# Subscription Feature Backend
Backend for a User Subscription page written in Python Flask 

Frontend repo can be found here - https://github.com/kaikoh95/subscription-feature-frontend

## Usage
Ensure that you have [Docker](https://www.docker.com/) installed in your host machine before trying to run the application.

Please also copy/create your own .env and stores.json files based on the examples provided
(see .env_example and stores_example.json).
The stores.json is used as the persistence here.

```
$ git clone https://github.com/kaikoh95/subscription-feature-backend.git
$ cd subscription-feature-backend
# When running for the first time, use:
$ docker-compose up --build
# When running subsequently, use:
$ docker-compose up
```
Now redirect to http://localhost:5000.

Once you have your local server running,
you can test your server using Postman and
view Swagger docs [here](http://localhost:5000/swagger-ui).


## Backlog

1. Add tests

2. Use actual DB for persistence

3. Explore cache layer