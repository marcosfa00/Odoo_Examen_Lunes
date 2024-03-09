# PRACTICA EXAMEN ODOO

Lo primero será levantar un servicio de Docker:

```YML
version: '3.1'
services:
  # Aquí indicamos la imagen web que va a tener odoo
  web:
    image: odoo:16.0
    depends_on:
      - mydb
    volumes:
      - ./addons:/mnt/extra-addons
    ports:
      - "8069:8069" # indicamos que lo vamos a levantar en el puerto 8069
    environment:
      - HOST=mydb # indicamos el nombre del host al que nos vamos a conectar, es decir la base de datos es el database Name que debemos indicar al iniciar odoo
      - USER=odoo # creamos el usuario de esta base d edatos
      - PASSWORD=myodoo # indicamos la contraseña de este usuario
  mydb: # a continuación indicamos que cliente de base de datos vamos a usar
    image: postgres:15 # en este caso usaremos postgres
    environment:
      - POSTGRES_DB=postgres # indicamos que a la base de datos que nos vamos a conectar dentro del cliente postgres será postgres
      - POSTGRES_PASSWORD=myodoo # la contraseña de postgres será myodoo
      - POSTGRES_USER=odoo # el usuario que emplearemos será odoo
    ports:
      - "5433:5432" # aquí indicamos que docker va a usar el puerto por defecto 5432, peor nosotros accederemos a la base d edatos a través del puerto 5433
```

levantamos el servicio con ```docker compose up -d```

Bien una vez iniciado **ODOO** para activar los ajustes de administrador debemos primero instalar una app cualquiera
En mi caso he elegido **CRM**  

### CRM
Este es un chat tipo **TEAMS** o **MEET** que permite a los usuarios creados en odoo chatear entre ellos.

Tras instalar este modulo de **CRM** como caualquier otro, ya nos aparecen otro tipo de ajustes en odoo mucho más avanzados.

Aquñi debemos activar : ```developer mode (with assets)```

esto nos permitirá instalar comodamente OPENACADEMY

# OPENACADEMY

para instalar openacademy creamos una carpeta llamada extra-addons, bueno si la indicamos en volumenes ya al crea sola
En mi caso mis volum,es en docker compose son los siguientes:

            volumes:
      - ./addons:/mnt/extra-addons
por lo que es evidente que mi carpeta se llame solo addons, pero es algo de lo que no debemos preocuparnos.

#### Instalación:

Para isntalar open academuy debemos ejecutar el siguiente comando

        docker exec -it nombre-contenedor-web-1 odoo scaffold openacademy /mnt/extra-addons

El comando como tal es ```odoo scaffold openacademy /mnt/extra-addons``` Pero recordemso que odoo está instalado en 
docker, por lo que no contamso el comando odoo para ejecutar ya que no esta en local, para ello, podemos acceder
dentro de nuestro contenedor como terminal con la primera parte del comando:

    docker exec -it nombre-contenedor-web-1

indico evidentemente el contenedor web, ya que el otro es la parte d ela base de datos.


### CONFIGURACIÓN DEL OPEN ACADEMY

AQUÍ podemos encontrar varios archivos que cambiaremos a continuación para poder crear tablas y añadir datos en nuestro openacademy

```path
 tree 
.
├── Readme.md
├── addons
│   └── openacademy
│       ├── __init__.py
│       ├── __manifest__.py
│       ├── controllers
│       │   ├── __init__.py
│       │   └── controllers.py
│       ├── demo
│       │   └── demo.xml
│       ├── models
│       │   ├── __init__.py
│       │   └── models.py
│       ├── security
│       │   └── ir.model.access.csv
│       └── views
│           ├── templates.xml
│           └── views.xml
└── docker-compose.yml

```

Bien, ahora que tenemos unamejor visual, vamso a comenzar paso a paso.

##### Manifest:
Aquí podremos indicar una descripción, una vesrión de nuestro openacademy y más cosas, como indicar donde pondremso nuestros cambios, vista etc...

Por ejemplo ahora tras cambiar el nombre, y ano aparece en odoo como openAcademy aparece con el nombre que le hemso indicado.

#### DATA
Bien, ahora vamos a crear una tabla en nuestro openAcademy, asiq  lo que deberemos hacer será crear la carpeta data e inicarla en nuestro manifest
Dentro de esta carpeta data, crearemos el archivo datos.xml
Aquí será donde inidcaremso como apareceran los campo s de nuestra tabla
la cual vamos ac rear en la base de datos

#### tabla en la base de datos

Esta tabla la creremos en nuestro models.py, si no existe ninguno crearemso nosotros el archivo o lo podemos renombrar.

```Python
from odoo import fields, models
# el nombre de nuestra clase será como el nbombre d ela tabla
class users(models.Model):
    _name= "users"
    _description="Tabla de usuarios"
```
EN este caso nos llorará el codigo del  import, ya que como hemos mencioando anteriormente odoo no está instalado en lcoal
Pero, una vez se relance el contenedor si que funcionará

Bien, tras hacer esto, debemos ir al archivo datos, que creamos dentro de data, aquí indicaremso como se mostrará la base d edatos en nuestro odoo

tendría una estructura como esta:

```xml
<odoo>
    <data>
        <record model="users" id="openacademy.nombres">
            <!-->Aquñi indicaremso que campos tiene la talba, o haremso referencia a ellso mejro dicho<-->
            <field name="name">MARCOS F. AVNEDAÑO</field>
            <field name="description">ATHLETA DEL DEPORTE BIKETRIAL</field>
            
        </record>
        
    </data>
    
</odoo>
```

#### Security

El siguiente paso será indicarle a nuestro odoo de nuestra tabla pro así decirlo

pro lo que cambiamos el por defecto de nuestro security pro indicarle nuestra tabla:

        access_openacademy_openacademy,openacademy.openacademy,model_users,base.group_user,1,1,1,1


## Down/Up
Tras hacer esto para que se cree nuestra tabla en postgres, debemos lanzar el servicio de nuevo, 
```Path
docker compose down

docker compose up -d

```
Tras hacer esto y configurar rapidamente odoo se creará nuestra tabla

# Visualizar nuestro openAcademy

Bien, ahora queremos que nuestro openAcademy aparezca en el menu de aplicaciones, al igual que si instalamos cualquier otro paquete.
Para ello debemos editar la Vista

para que estos cambios surgan efecto debemos comentar en nuestro archivo **Manifest** los siguiente, en el campo data:

  # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/datos.xml'
    ],

