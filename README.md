# Dealarship Portal Project



## Environment creation

First of all we must create a virtual environment to avoid dependency problems.
To create the environment, run the following command

```bash
virtualenv ven
```

Then it is necessary to activate the environment, which can be found in **ven/bin/activate** or **ven/Scripts/activate**

Run the following command

```bash
source ven/bin/activate
# or
source ven/Scripts/activate
```



## Dependency installation

The project has a requirements.txt file in which its dependencies go. To install the dependencies run the following command in terminal.

```bash
pip install -r requeriments.txt 
```

## Run the program

To initialize the service, the following command must be executed.

```bash
python manage.py runserver
```

### Endpoints

#### Admin module.

- http://localhost:8000/admin/

#### Create Vehicle.

- http://localhost:8000/

#### List Vehicles

- http://localhost:8000/v1/portal/vehicles/list

#### List Vehicles JSON

- http://127.0.0.1:8000/v1/portal/vehicles

  

## Admin Module

The administration module is active and modified for use with email. The user created for tests and with whom you can access the module is the following

Email: test@test.com

Password: test

## LDAP

**Install django-auth-ldap**

```bash
pip install django-auth-ldap
```

Add to the settings.py 

```
AUTHENTICATION_BACKENDS = ["django_auth_ldap.backend.LDAPBackend"]
```

Configure the server

```
AUTH_LDAP_SERVER_URI = "ldap://ldap.example.com"
from my_module import find_my_ldap_server

AUTH_LDAP_SERVER_URI = find_my_ldap_server

```

