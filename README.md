## up database
``docker-compose up -d db``
## runnging migrations konga admin
``docker run --rm --network=kong_kong-network pantsel/konga -c prepare -a postgres -u postgresql://kong@db:5432/konga_db``
## running project
``docker-compose up``
