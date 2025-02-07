import authenticate_with_msal

# Percorso del file di configurazione
PathToEnvironmentJSON = "env.json"

# Ottenere il token di autenticazione
authentication = authenticate_with_msal.getAuthenticatedSession(PathToEnvironmentJSON)
session = authentication[0]
environmentURI = authentication[1]

# Nome della tabella da interrogare
table_name = "cra30_contattos"

# Endpoint per ottenere i record della tabella
request_uri = f"{environmentURI}api/data/v9.2/{table_name}?$top=10"

# Effettua la richiesta
r = session.get(request_uri)

# Controlla la risposta
if r.status_code == 200:
    data = r.json()
    print(f"Record della tabella {table_name}:")

    for record in data["value"]:
        print(record)  # Stampa tutti i campi del record

else:
    print(f"Errore: {r.status_code}, {r.text}")
