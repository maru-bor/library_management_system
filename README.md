# Systém pro správu knihovny (konzolová aplikace)
Konzolová aplikace pro správu knihovny je implementovaná v jazyce **Python** s využitím relační databáze **Microsoft SQL Server**.
Aplikace je navržena v three-tier architektuře a využívá návrhové vzory **DAO** a **Singleton**.

# Software požadavky
Aplikace využívá následující software: 
  1. Python 3.10+ (+ ```pyodbc``` balíček)
  2. Microsoft SQL Server
  3. ODBC Driver 17 for SQL Server

# Instalace a spuštění aplikace
Tento návod na instalaci a spuštění aplikace je především určen pro školní počítače na SPŠE Ječná. Tudíž návod tedy také počítá s tím, že výše uvedený software je už na zařízení nainstalovaný (kromě specifických Python knihoven a balíčků) a že uživatel používá Windows 10 OS. 

## 1. Vytvoření a nastavení databáze
  1. Připojíte se pomocí programu Microsoft SQL Server Management Studio pomocí následujících přístupových údajů, kde PCXXX nahradíte skutečným jménem databázového serveru:
      - SERVER TYPE: ```Database engine```
      - SERVER NAME: ```PCXXX```
      - AUTHENTICATION: ```SQL Server authentication```
      - LOGIN: ```sa```
      - PASSWORD: ```student```
  2. Vytvořte novou databázi s názvem ```db_library```:
     ```
     create database db_library
     ```
  3. Vytvořte aplikační uživatelský účet, který vytvoříte ve složce "Security" a podsložce "Logins" klinutím na pravé tlačítko a zvolením "New login". Nového uživatele vytvořte s těmito parametry:
      - LOGIN NAME: lib_admin
      - AUTHENTICATION: SQL Server authentication
      - PASSWORD: admin
      - USER MUST CHANGE PASSWORD: no
      - DEFAULT DATAVASE: db_library

      V záložce "User mapping" pak nastavte mapování mezi databází ```db_library``` a oprávněním ```db_owner```.
  4. Spojení otestujte tak, že kliknete v záložce "Object explorer" znovu na tlačítko "Connect" a vytvoříte druhé připojení pomocí tohoto uživatele.
  5. Stáhněte si SQL DDL [skript](script.sql) a spustě ho v databázi ```db_library```
  6. Zkontrolujte, zda-li se úspěšně vytvořili všechny tabulky, jejich vazby a také pohledy.
## 2. Nastavení konfiguračního souboru
  1. Naklonujte si repozitář projektu
  ```
  git clone https://github.com/maru-bor/library_management_system.git
  ```
  2. Přejděte do adresáře ```db```
  **Windows CMD a PowerShell**:
  ```
  cd library_management_system\db
  ```
   **Git Bash**:
  ```
  cd library_management_system/db
  ```   
  3. Upravte konfigurační soubor ```db_config.json``` tak, aby měl následující parametry, PCXXX nahradíte skutečným jménem databázového serveru:
  ```
  {
    "server": "PCXXX",
    "database": "db_library",
    "username": "lib_admin",
    "password": "admin",
    "driver": "ODBC Driver 17 for SQL Server"
  }
  ```
## 3. Vytvoření virtuálního prostředí a instalace Python balíčků
  1. Přejděte do kořenového adresáře projektu
  ```
  cd library_management_system
  ```
  2. Vytvořte virtuální prostředí 
  ```
  python -m venv venv
  ```
  Poté prostředí aktivujte:
  - **Windows**
   ```
   venv\Scripts\activate
   ```
  3. Po aktivaci venv prostředí, instalujte balíček ```pyodbc```
  ```
  pip install pyodbc
  ```
  4. Spusťte aplikaci
  ```
  python main.py
  ```
  Mělo by se zobrazit hlavní konzolové menu aplikace
