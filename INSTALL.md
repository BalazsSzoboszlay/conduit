# Elérési hely
A GitHub-repository elérési címe:<br/>
https://github.com/BalazsSzoboszlay/conduit

# Telepítés

Letöltés után a 
```
docker-compose up -d
```

parancs futtatása parancssorból.
# Futtatás
Böngészőben a [http://localhost:1667](http://localhost:1667) megnyitása.

# Tesztek futtatása automatizált módon

A Github Actions segítségével minden **push** eseménynél 
automatizáltan lefutnak a tesztek a **/.github/workflows/tests.yml** fájlban leírtak szerint.
Ennek eredményét a https://github.com/BalazsSzoboszlay/conduit/actions oldalon vagy a 
https://balazsszoboszlay.github.io/conduit reporting oldalon lehet megtekinteni. 

# Összes teszt futtatása egyszerre

A program gyökérkönyvtárából `pytest` parancs kiadása. 
Feltelepített python, pytest és a `requirements.txt`-ben
megadott függőségeket igényli előzetesen.

# Tesztek futtatása egyesével

A program `src/tests/automation` 
mappájában kiadott `pytest <kívánt teszt neve>` parancs kiadása parancssorban.
Az előző fejezetben megadott a függőségeket igényli.

