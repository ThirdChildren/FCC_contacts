import os
from dotenv import load_dotenv
import authenticate_with_msal

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Ottieni il user_id dalla variabile d'ambiente
user_id = os.getenv("USER_ID")

if not user_id:
    print("USER_ID non trovato nel file .env")
    exit()

# Parametri
PathToEnvironmentJSON = "env.json"
authentication = authenticate_with_msal.getAuthenticatedSession(PathToEnvironmentJSON)
session = authentication[0]
environmentURI = authentication[1]

# Prima richiesta: ottieni i ruoli assegnati all'utente (solo ID)
request_uri = f"{environmentURI}api/data/v9.2/systemuserrolescollection?$filter=systemuserid eq {user_id}"

response = session.get(request_uri)

if response.status_code == 200:
    roles = response.json()["value"]

    for role in roles:
        role_id = role["roleid"]  # Solo ID del ruolo

        # Seconda richiesta: ottieni i dettagli del ruolo (nome)
        role_details_uri = f"{environmentURI}api/data/v9.2/roles({role_id})"
        role_details_response = session.get(role_details_uri)

        if role_details_response.status_code == 200:
            role_name = role_details_response.json()["name"]  # Nome del ruolo
            print(f"ID Ruolo: {role_id}, Nome Ruolo: {role_name}")
        else:
            print(
                f"Errore nel recupero del nome del ruolo per ID {role_id}: {role_details_response.status_code}"
            )
else:
    print("Errore:", response.status_code, response.json())
