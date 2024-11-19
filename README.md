# ohtu-latexchefs

[![GHA workflow badge](https://github.com/chuotchuot/ohtu-latexchefs/workflows/CI/badge.svg)](https://github.com/chuotchuot/ohtu-latexchefs/actions)

[Backlog](https://helsinkifi-my.sharepoint.com/:x:/g/personal/janteero_ad_helsinki_fi/EZOTEPWAgVVJnm4PhNXM8-YB2JGW8DwOhZs6ALVS5rh3-A?e=fSjnbS)

### Definition of done
Valmiiksi tehty tarkoittaa sitä, että vaatimus on analysoitu, suunniteltu, ohjelmoitu, testattu, testaus automatisoitu, dokumentoitu, integroitu muuhun ohjelmistoon.

### Ohjelman käyttäminen

Kloonaa repositorio laitteellesi
#### SSH
```
git clone git@github.com:chuotchuot/ohtu-latexchefs.git 
```
#### HTTPS
```
git clone https://github.com/chuotchuot/ohtu-latexchefs.git
```
Asenna tarvittavat riippuvuudet suorittamalla alla oleva komento paikallisen repositorion juuressa.
```
poetry install 
```
Luo .env -tiedosto seuraavilla tiedoilla kloonaamasi repositorion juureen paikallisesti
```
DATABASE_URL=postgresql://{Pyydä tietokannan tiedot kehittäjiltä} 
TEST_ENV=true 
SECRET_KEY={Luo henkilökohtainen salausavain} 
```
Käynnistä virtuaaliympäristö seuraavalla komennolla
```
poetry shell 
```
Käynnistä ohjelma suorittamalla alla oleva komento paikallisen repositorion juuressa.
```
python3 src/index 
```
