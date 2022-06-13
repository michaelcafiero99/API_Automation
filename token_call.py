import requests
import requests.auth
from datetime import datetime
from database_functions import create_db_connection, read_query, execute_query
# ‘1753-01-01 00:00:00’
# TODO: track if the token is active -- it expires after 1 hour


def get_token():
    now = datetime.now()

    now_string = now.strftime("%Y-%m-%d")

    auth_string = ""
    q1 = """
    SELECT *
    FROM tokens;
    """
    pw = "punkinbunker1P!"
    db = "SpeakIT"
    connection = create_db_connection("localhost", "root", pw, db)
    results = read_query(connection, q1)
    if True:

        print(results)
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
        auth_string = "'Bearer " + token_string + "'"
        q2 = """INSERT IGNORE
        INTO SpeakIT.tokens (token_id, creation_time,expiration_time,token_content)
        VALUES(1,""" + now_string + "," + now_string + "," + auth_string + ")"""
        results = read_query(connection, q2)
        print(q2)
        q3 = "SELECT * FROM SpeakIT.tokens;"
        results2 = read_query(connection, q2)
        print(results2)

    if True:
        one = 1
        # query the token from the database

    return auth_string


get_token()
