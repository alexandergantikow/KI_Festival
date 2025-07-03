# Anleitung für Kursleiter - Python Level 1 Workshop

## Windsurf Terminal verwenden

### Terminal öffnen
**Shortcut:** `Strg+ J`

### Zwischen Projektordnern navigieren

#### Aktueller Ordner anzeigen
```bash
pwd
```

#### Ordnerinhalt anzeigen
```bash
ls
```

#### In Unterordner wechseln
```bash
# Zur Eis-App
cd Base_App

# Zur KI-App
cd KI_App
```

#### Zurück zum Hauptordner
```bash
cd ..
```

#### Direkt zwischen Ordnern wechseln
```bash
# Vom Hauptordner zu Base_App
cd Base_App

# Von Base_App zu KI_App
cd ../KI_App

# Von KI_App zurück zum Hauptordner
cd ..
```

## Streamlit Apps starten

#### Eis-Bewertungs-App
```bash
# Im Hauptordner
streamlit run Base_App/base_app.py

# Oder im Base_App Ordner
cd Base_App
streamlit run base_app.py
```

#### KI-App
```bash
# Im Hauptordner
streamlit run KI_App/ki_app.py

# Oder im KI_App Ordner
cd KI_App
streamlit run ki_app.py
```

#### Demo-App (vollständige Referenz)
```bash
poetry run streamlit run helper_app.py
```

### Alternative ohne Poetry
```bash
# Eis-App
streamlit run Base_App/base_app.py

# KI-App
streamlit run KI_App/ki_app.py

# Demo-App
streamlit run helper_app.py
```

## Apps beenden

### Im Terminal
- **Shortcut:** `Ctrl+C` 
- Die App wird beendet und das Terminal ist wieder verfügbar

## Tipps für den Workshop

1. **Immer vom Hauptordner starten** - so funktionieren alle Pfade
2. **`Ctrl+C` zum Beenden** - nicht nur Browser-Tab schließen
3. **Terminal im Blick behalten** - für Fehlermeldungen
