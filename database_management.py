from database_functions import create_db_connection, execute_query


# create_database_query = "CREATE DATABASE SpeakIT"
# create_database(connection,create_database_query)

drop = """ DROP TABLE tokens """
create_token_times = """
CREATE TABLE tokens (
  token_id INT PRIMARY KEY,
  creation_time datetime NOT NULL,
  expiration_time datetime NOT NULL,
  token_content VARCHAR(50) NOT NULL
  );
 """
pw = "punkinbunker1P!"
db = "SpeakIT"
connection = create_db_connection("localhost", "root", pw, db)  # Connect to the Database
execute_query(connection, drop)  # Execute our defined query
execute_query(connection, create_token_times)  # Execute our defined query
