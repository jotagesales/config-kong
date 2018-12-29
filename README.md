## up database
``docker-compose up -d db``
## running migrations kong
``docker run --rm --network=kong_kong-network -e KONG_DATABASE=postgres -e KONG_PG_HOST=db -e KONG_CASSANDRA_CONTACT_POINTS=db kong:latest kong migrations up``
## runnging migrations konga admin
``docker run --rm --network=kong_kong-network pantsel/konga -c prepare -a postgres -u postgresql://kong@db:5432/konga_db``
## up kong
``docker-compose up kong``
## up kong-admin
``docker-compose up kong-admin``
## up prometheus
``docker-compose up prometheus``
## up grafana
``docker-compose up grafana``
## granafa dashboard
``6486``
