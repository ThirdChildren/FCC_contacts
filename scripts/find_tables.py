import authenticate_with_msal

# Percorso del file di configurazione
PathToEnvironmentJSON = "env.json"

# Ottenere il token di autenticazione
authentication = authenticate_with_msal.getAuthenticatedSession(PathToEnvironmentJSON)
session = authentication[0]
environmentURI = authentication[1]

# Endpoint per ottenere l'elenco delle tabelle
request_uri = (
    f"{environmentURI}api/data/v9.2/EntityDefinitions?$select=LogicalName,DisplayName"
)

# Effettua la richiesta
r = session.get(request_uri)

# Controlla la risposta
if r.status_code == 200:
    data = r.json()
    print("Tabelle disponibili in Dataverse:")
    for entity in data["value"]:
        logical_name = entity.get("LogicalName", "N/A")
        display_name = logical_name  # Imposta di default il LogicalName

        # Controlla se DisplayName esiste e ha un valore
        if entity.get("DisplayName") and entity["DisplayName"].get(
            "UserLocalizedLabel"
        ):
            display_name = entity["DisplayName"]["UserLocalizedLabel"].get(
                "Label", logical_name
            )

        print(f"- {logical_name} ({display_name})")
else:
    print(f"Errore: {r.status_code}, {r.text}")
