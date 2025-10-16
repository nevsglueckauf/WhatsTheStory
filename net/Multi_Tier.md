# Multi Tier Architektur 



```mermaid
---
config:
  look: handDrawn
  theme: neutral
---
sequenceDiagram
autonumber
    box lightgray Clients
      participant UserAgent@{ "type" : "boundary"}
      participant Browser@{ "type" : "boundary"}
      participant HttpClientBot@{ "type" : "boundary"}
    end
    box yellow Backend
      participant Webserver@{ "type" : "control" }
      participant ApplicationServer@{ "type" : "queue" }
      participant RDBMS@{ "type" : "database" }
    end
    UserAgent->>Webserver: http://Loki/Api/Entry/items/new 
    Webserver->>ApplicationServer: Hole Daten zu Produkt ABC
    ApplicationServer->>RDBMS:SQL
    RDBMS->>ApplicationServer:Liefere Daten
    ApplicationServer->>Webserver: Liefert Daten (z.B: Produktdaten aus DB + weitere Berechnungen)
    Webserver->>UserAgent: HTTP Response (JSON Payload oder HTML Payload etc.)
    
```
