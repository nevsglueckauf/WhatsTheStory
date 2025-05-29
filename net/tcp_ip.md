# TCP/IP

PLACEHOLDER File - wird sukzessiv ergänzt

## Überstunden? Schichtsache
```mermaid
flowchart TD
    
    id4(Application) <--> id3(Host-To-Host)
    id3(Host-To-Host) <--> id2(Internet)
    id2(Internet) <--> id1(Network Access)
    
    style id1 fill:#a1f1a8
    style id2 fill:#6062e2
    style id3 fill:#f10103
    style id4 fill:#aa0102

```







## <a name="socket">Socket</a>

- <em>Eindeutiger Endpunkt</em> einer Kommunikation -  Verbindung von <var>IP-Adresse</var> und <var>Port</var>, sowie Protokoll (<var>UDP</var>, <var>TCP</var>):
    - <kbd>192.168.23.42</kbd> : <kbd>443</kbd> <var>TCP</var> (HTTPS via TCP auf diese IP-Adresse )