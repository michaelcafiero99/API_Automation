import requests
import requests.auth


# TODO: track if the token is active -- it expires after 1 hour
def get_token():
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
    decoded_string = content.decode()
    token_string = decoded_string[59:87]
    auth_string = 'Bearer ' + token_string
    return auth_string
