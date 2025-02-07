import authenticate_with_msal

# Parametri
PathToEnvironmentJSON = "env.json"
authentication = authenticate_with_msal.getAuthenticatedSession(PathToEnvironmentJSON)
session = authentication[0]
environmentURI = authentication[1]

# Richiesta API per ottenere i ruoli disponibili
request_uri = f"{environmentURI}api/data/v9.2/roles?$select=name,roleid"

response = session.get(request_uri)

if response.status_code == 200:
    roles = response.json()["value"]
    for role in roles:
        print(f"Ruolo: {role['name']}, ID: {role['roleid']}")
else:
    print("Errore:", response.status_code, response.json())
