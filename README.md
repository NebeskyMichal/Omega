# Projekt Omega
Omega je klientská aplikace vyvinutá jako závěrečný projekt na SPŠE Ječná. Projekt slouží k evidenci, hodnocení a správě videoherních titulů v rámci komunity uživatelů.

## O projektu
Cílem projektu bylo vytvořit komplexní systém využívající architekturu **Model-View-Controller (MVC)**, který umožňuje uživatelům vytvářet profily, hodnotit hry a sdílet názory, zatímco administrátoři mají k dispozici konzolové rozhraní pro správu uživatelů a databázových záznamů.

## Použité technologie a vzory
* **Jazyk:** Python 3.9+
* **Databáze:** MS SQL Server
* **Knihovny:** `pyodbc` (pro komunikaci s DB), `configparser` (konfigurace), `bcrypt` (bezpečné hashování hesel)
* **Návrhové vzory:** * **Singleton:** Pro efektivní správu připojení k databázovému serveru.
    * **Active Record:** Pro objektovou implementaci a snadnou manipulaci s databázovými tabulkami.
    * **Command Pattern:** Pro efektivní volání funkcí a zpracování uživatelských vstupů.

## Databázová struktura
Aplikace pracuje s relační databází obsahující tabulky pro uživatele, hry, vydavatele, hodnocení, bany a nahlášení. Integrován je i databázový trigger `update_game_rating` pro automatický přepočet globálního hodnocení her.

## Instalace

Po stažení projektu je nutné si ná Váš databázový server nahrát databázovou stukturu v souboru export.sql v adresáři ./database.

Vytvořit a použít patričný databázový účet pro správu této DB.

Všechna konfigurační data nastavit v souboru ./db_config.ini 

Je nutné si doinstalovat knihovny pyodbc a  bcrypt pomoci pip, avšak Vás na to program upozorní při spuštění chybovou hláškou.

```text
[Database]
Driver = {ODBC Driver 17 for SQL Server}
Server = Michal\SQLEXPRESS03
Database = GameRatings
UID = admin
PWD = 123
```

## Používání
Program se spouští v příkazové řádce, avšak lze ho spustit i v nějakém vývojovém prostředí pro Python.

Administrátorské konzol se ovládá pomocí vstupů z klavesnice.
Klientská okenní aplikace se ovládá pomocí tlačítek a vstupů z klavesnice

## Příklad používání administrátorské konzole
```text
--------------------------------------------------
Successfully logged in
--------------------------------------------------
--------------------------------------------------
1. Manage games
2. Manage users
3. Change password
4. Check statistics
5. End program
--------------------------------------------------
Choose which action you want to run
1
--------------------------------------------------
1. Add game
2. Edit game title
3. Edit game release date
4. Delete game
5. Add publisher
6. Statistics for certain game
7. Return to main menu
--------------------------------------------------
Choose which action you want to run
7
--------------------------------------------------
Returning to main menu...
--------------------------------------------------


```
