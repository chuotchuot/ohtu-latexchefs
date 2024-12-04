# ohtu-latexchefs

[![GHA workflow badge](https://github.com/chuotchuot/ohtu-latexchefs/workflows/CI/badge.svg)](https://github.com/chuotchuot/ohtu-latexchefs/actions)

[Backlog](https://helsinkifi-my.sharepoint.com/:x:/g/personal/janteero_ad_helsinki_fi/EZOTEPWAgVVJnm4PhNXM8-YBn665Mru4h2k-IxQ7mwoASQ?e=rFcqFA)

### Definition of done

Requirements are considered done when they've been analyzed, planned, programmed, tested, testing automated, documented and integrated to rest of the software.

### Setting up and running the project locally

Clone the repository to your local
#### SSH
```
git clone git@github.com:chuotchuot/ohtu-latexchefs.git 
```
#### HTTPS
```
git clone https://github.com/chuotchuot/ohtu-latexchefs.git
```
Change directory to the root of the project and install dependencies
```
cd ohtu-latexchefs
poetry install
```
Create .env -file with following specifications to the root of your local project.
```
DATABASE_URL=postgresql://{local database address} 
TEST_ENV=true 
SECRET_KEY={Create personal secret key} 
```
Setup database on your local
```
python3 src/db_helper.py
```
Start virtual environment
```
poetry shell 
```
Run the application
```
invoke start 
```
Run tests while application is running
```
invoke test
```
