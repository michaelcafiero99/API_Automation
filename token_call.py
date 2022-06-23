import requests
import requests.auth
import sqlparse
import datetime
from datetime import timedelta
from database_functions import create_db_connection, read_query, execute_query


# ‘1753-01-01 00:00:00’
# TODO: track if the token is active -- it expires after 1 hour

def new_token(connection):

    url = "https://api.preview.platform.athenahealth.com/oauth2/v1/token"
    payload = 'grant_type=client_credentials&scope=athena%2Fservice%2FAthenanet.MDP.*%0A'
    headers = {
        'data': 'grant_type=client_credentials',
        'Cache-Control': 'no-cache',
        'Authorization': 'Basic MG9hZGIxM3ZqODBtaHhhQXgyOTc6TXF4U3F5VlktemlwdXR0cDJYNVRILW9zUzI1cWNQVjJXa0tEZ3RKQg==',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'dtCookie=5AF86EC06F3D5BB6E6D09A1BBF3C7710|RUM+Default+Application|1'
    }

    token_response = requests.request("POST", url, headers=headers, data=payload)
    content = token_response.content
    #  print(content)
    decoded_string = content.decode()
    token_string = decoded_string[59:87]
    auth_string = "Bearer " + token_string + ""
    now = datetime.datetime.now()
    now_string = now.strftime("%Y-%m-%d %H:%M:%S")
    expiration = now + timedelta(hours=1)
    expiration_string = expiration.strftime("%Y-%m-%d %H:%M:%S")
    q1 = """DELETE FROM SpeakIT.tokens;"""
    results = execute_query(connection, q1)
    print(results)
    q2 = """INSERT
           INTO SpeakIT.tokens (token_id, creation_time,expiration_time,token_content)
           VALUES(5,""" + "'" + now_string + "'" + "," + "'" + expiration_string + "'" + "," + "'" + auth_string + "'" + ")"""
    results = execute_query(connection, q2)
    #print(results)
    q3 = "SELECT * FROM SpeakIT.tokens;"
    results2 = read_query(connection, q3)
    #print(results2)



def check_token(connection):

    q3 = "SELECT * FROM SpeakIT.tokens;"
    results2 = read_query(connection, q3)
    print(results2)
    parsed = ((results2[0])[2])
    now = datetime.datetime.now()

    if now > parsed:
        new_token(connection)


def get_token():

    pw = "punkinbunker1P!"
    db = "SpeakIT"
    connection = create_db_connection("localhost", "root", pw, db)
    check_token(connection)

    q3 = "SELECT * FROM SpeakIT.tokens;"
    results2 = read_query(connection, q3)
    print(results2)
    auth_string = ((results2[0])[3])
    print(auth_string)
    return auth_string
get_token()



