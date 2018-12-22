## running migrations database
```docker run --rm --network=kong_kong-network -e KONG_DATABASE=postgres -e KONG_PG_HOST=db -e KONG_CASSANDRA_CONTACT_POINTS=db kong:latest kong migrations up```
## runngin migrations
docker run --rm --network=kong_kong-network -e KONG_DATABASE=postgres -e KONG_PG_HOST=db -e KONG_CASSANDRA_CONTACT_POINTS=db kong:latest kong migrations up
docker run --rm --network=kong_kong-network pantsel/konga -c prepare -a postgres -u postgresql://kong@db:5432/konga_db
