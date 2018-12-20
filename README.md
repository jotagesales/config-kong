## running migrations database
docker run --rm --network=kong_kong-network -e KONG_DATABASE=postgres -e KONG_PG_HOST=db -e KONG_CASSANDRA_CONTACT_POINTS=db kong:latest kong migrations up
`````````````````˜˜˜kjkljksdfdskfjksjdfksjflskjflksjdfsdocker run --rm --netwokdjfksldfjsldfkjslfkdsjrk=kong_kong-network -e KONG_DATABASE=postgres -e KONG_PG_HOST=db -e KONG_CASSANDRA_CONTACT_POINTS=db kong:latest kong migrations up
