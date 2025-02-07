import authenticate_with_msal

# Parametri
PathToEnvironmentJSON = "env.json"
authentication = authenticate_with_msal.getAuthenticatedSession(PathToEnvironmentJSON)
session = authentication[0]
environmentURI = authentication[1]

# Richiesta API per ottenere gli utenti
request_uri = f"{environmentURI}api/data/v9.2/systemusers?$select=fullname,systemuserid"

response = session.get(request_uri)

if response.status_code == 200:
    users = response.json()["value"]
    for user in users:
        print(f"Utente: {user['fullname']}, ID: {user['systemuserid']}")
else:
    print("Errore:", response.status_code, response.json())
