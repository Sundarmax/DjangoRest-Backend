import zcrmsdk
import requests

config = {
        "apiBaseUrl":"https://www.zohoapis.com",
        "apiVersion":"v2",
        "currentUserEmail":"",
        "sandbox":"False",
        "applicationLogFilePath":"",
        "client_id":"",
        "client_secret":"",
        "redirect_uri":"https://www.abc.com",
        "accounts_url":"https://accounts.zoho.com",
        "token_persistence_path":"",
        "access_type":"online",
        # Use the below keys for MySQL DB persistence
        "mysql_username":"",
        "mysql_password":"",
        "mysql_port":"3306",
        # Use the below keys for custom DB persistence
        "persistence_handler_class" : "Custom",
        "persistence_handler_path": "/Users/Zoho/Desktop/PythonSDK/CustomPersistance.py"
}

# url = "https://accounts.zoho.com/oauth/v2/token?code= "+ code + "&redirect_uri=" + redirect_uri +"&client_id=" + client_id +  "&client_secret=" + client_secret + "&grant_type=authorization_code"

# try:
#     zcrmsdk.ZCRMRestClient.initialize(config)
#     oauthInstance = zcrmsdk.ZohoOAuth.get_client_instance()
#     tokenInstance = oauthInstance.generate_access_token(code)
#     print(tokenInstance.accessToken)
# except Exception as e:
#     print(str(e))


#url  = "https://accounts.zoho.com/oauth/v2/token?grant_type=authorization_code&client_id=1000.1G9AJWH0BJBM22YC6D9LNRRET00A5H&client_secret=49f96a115dd8ef1e126c18b071940716ac3733e63f&redirect_uri=aeiser.com&code=" + code
response = requests.post(url)
print(response.content,response.status_code)

#print(url)
#zcrmsdk.ZCRMRestClient.initialize(config)
#oauth_client = zcrmsdk.ZohoOAuth.get_client_instance()
#print(oauth_client)
#grant_token  = "1000.87f94152f1854817c59d6ba1f26a63ca.36d1041f04b03450989c34bc362cd4f3" 
#oauth_tokens = oauth_client.generate_access_token(grant_token)