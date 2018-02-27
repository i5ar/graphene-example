### Run Postgres database in a container

Map a different [container port](https://stackoverflow.com/questions/37694987/) to connect:

    docker run -d -p 5433:5432 -e POSTGRES_PASSWORD=postgres

Eventually stop database in localhost to avoid collision:

    sudo su postgres
    pg_ctl -D /var/lib/pgsql/data stop
    
### Connect to the container

From the current shell:

    psql -h localhost -p 5433 -U postgres
    
From the container shell:

    docker exec -it 74335d8b8a81 /bin/bash
    psql -U postgres
