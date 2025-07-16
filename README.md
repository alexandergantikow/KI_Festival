# KI Festival Workshop - Setup
## Voraussetzungen

### 1. System aktualisieren
```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Python Installation
```bash
# Python 3.13 und Tools installieren
sudo apt install python3 python3-pip python3-venv python3-dev -y

# Installation überprüfen
python3 --version
pip3 --version
```

### 3. Git Installation
```bash
# Git installieren
sudo apt install git -y

# Installation überprüfen
git --version
```

### 4. Windsurf Installation
```bash
# Windsurf herunterladen und installieren
wget https://windsurf-stable.codeiumdata.com/linux-x64/stable -O windsurf.deb
sudo dpkg -i windsurf.deb
sudo apt-get install -f  # Falls Abhängigkeiten fehlen
```

## Projekt Setup

### 1. Repository klonen

```bash
git clone git@github.com:alexandergantikow/KI_Festival.git
cd KI_Festival
```

### 2. Virtuelle Umgebung erstellen

```bash
# Virtuelle Umgebung erstellen
python3 -m venv venv

# Aktivieren
source venv/bin/activate

# Installation überprüfen
which python
```

### 3. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 4. OpenAI API Key einrichten (für KI-App)

```bash
# In .bashrc oder .zshrc hinzufügen
echo 'export OPENAI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc

# ODER .env Datei im Projektordner erstellen
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

## Apps starten

### Basis-App (Eis-Bewertung)
```bash
streamlit run Base_App/base_app.py
```

### KI-App (Chat mit GPT)
```bash
streamlit run KI_App/ki_app.py
```

## Zusätzliche Einrichtung

## Troubleshooting

### Python nicht gefunden
```bash
# Python-Pfad überprüfen
which python3
ls -la /usr/bin/python*

# Alternative: python3 explizit verwenden
python3 --version
```

### Virtual Environment Probleme
```bash
# Umgebung deaktivieren
deactivate

# Umgebung löschen und neu erstellen
rm -rf venv
python3 -m venv venv
source venv/bin/activate
```

### OpenAI API Key Probleme
```bash
# API Key überprüfen
echo $OPENAI_API_KEY

# Environment neu laden
source ~/.bashrc
```

### Abhängigkeiten-Probleme
```bash
# Pip aktualisieren
pip install --upgrade pip

# Requirements neu installieren
pip install -r requirements.txt --force-reinstall
```

## Für Kursleiter

Siehe `README_INSTRUCTOR.md` für detaillierte Anweisungen zur Durchführung des Workshops.

---

**Ziel erreicht?** Wenn beide Apps erfolgreich starten, bist du bereit für den Workshop!
