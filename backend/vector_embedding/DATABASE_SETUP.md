# Database setup instructions

#   run the following commands in a new terminal to run the above code (after the app is running):
# pip install tiktoken


#   You should have docker desktop installed and open, then run the following in the terminal still:
# docker pull ankane/pgvector
# docker run --name pgvector -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d ankane/pgvector


#   note that name is the name of the current file, and password is whatever you set it to be,
#   the port is the port setup during the environment setup


#   DataBase Setup:
# You can now install a GUI tool such as pgAdmin 4 to inspect the database that is running in the container,
# or else use psql on the command-line.
# If you're using pgAdmin 4 then simply right click the server on the left and create a new server group named whatever you want.
# Then right click that server and register a server. The name can once again be whatever you want.
# In the connection section, you can specify the host as localhost, and the
# password as whatever you used in the above command - mysecretpassword, in our case and save.


#   Using the right click query tool on your created database (which you need to make next to the premade database and name vector_db),
#   run the following code:
# CREATE DATABASE vector_db; (Not sure about this line actually)
# CREATE EXTENSION pgvector;


#   run the following commands in the terminal:
# pip install psycopg2-binary pgvector


Running the Project:

# in ...\backend\vector_embedding
1) Start PostgreSQL with pgvector using Docker:
docker-compose -f docker/docker-compose.yml up -d

2) Initialize the databasewith the required schema:

# in ...\backend\vector_embedding or \db
cat db/init_db.sql | docker exec -i pgvector psql -U postgres

# in ...\backend\vector_embedding
3) Install Python dependencies:
pip install -r requirements.txt 
# from ...\backend\requirements.txt

4) Run your application:
python ...\backend\vector_embedding\daniel_postgress_vector\pgvector.py