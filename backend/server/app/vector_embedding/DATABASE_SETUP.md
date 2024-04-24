# Database setup instructions

# install and run docker desktop
# install a GUI tool such as pgAdmin 4 to inspect the database that is running in the container
# Using pgAdmin 4, simply right click the server on the left and create a new server group named whatever you want.
# Then right click that server and register a server. The name can once again be whatever you want.
# In the connection section, you can specify the host as localhost, and the
# password as - mysecretpassword, in our case and save.


#   Using the right click query tool on your created database (which you need to make next to the premade database and name vector_db),


Running the Project:

# after starting the server and client, run the following:

# in the terminal in ...\backend\server\app\vector_embedding
1) Start PostgreSQL with pgvector using Docker:
docker-compose -f docker/docker-compose.yml up -d

2) Initialize the databasewith the required schema:

# in ...\backend\server\app\vector_embedding
cat db/init_db.sql | docker exec -i pgvector psql -U postgres
# if the above command fails. try:

 docker exec -i docker-pgvector-1 psql -U postgres -c "CREATE DATABASE vector_db"
 # NOTICE: The extension currently is failing to be set up.

3) Run your application:
# in python ...\backend\server\app\vector_embedding\postgress_vector\pgvector.py
py pgvector.py