############################################ crear el entorno virtual de python con (venv, virtualenv, pipenv, etc) ##########################################
################################################################## ejemplo creado para pipenv ################################################################

pip install pipenv                          --> instala el paquete de entornos virtuales pipenv

pipenv install                              --> instala todas las dependencias necesarias (en caso de usar otro gestor de entorno virtual se incluye un requirements)

pipenv run server                           --> ejecuta el servidor

####################################################################### UTILIDADES ###########################################################################

pipenv shell                                --> crea un entorno virtual con el nombre de la carpeta actual y entra a el abriendo una consola
pipenv exit                                 --> sale del entorno virtual

######################################################## instalar dependencias en caso de no usar pipenv ######################################################
pip install -r requirements.txt             --> instala las dependencias necesarias
pip freeze > requirements.txt               --> guarda las depdencias actuales

################# exporta la variable de entorno para tu sistema operativo y consola de comandos usada ################
export FLASK_APP="main.py"                  --> LINUX/MAC;           declara la variable de entorno para ejecutar el servidor (export linux/mac)
set FLASK_APP=main.py                       --> WINDOWS/CMD;         declara la variable de entorno para ejecutar el servidor (set windows CMD)
$env:FLASK_APP = "main.py"                  --> WINDOWS/POWERSHELL;  declara la variable de entorno para ejecutar el servidor ($env: windows PowerShel)

############################################## cambio de entorno flask ################################################
export FLASK_ENV=development                --> LINUX/MAC; cambia a entorno de desarrollo en lugar de production

#######################################################################################################################

flask run                                   --> ejecuta el servidor flask con la aplicacion definida en el entorno

####################################################### ejecucion de test #############################################
python -m unittest -v test_kodiApi.py       --> ejecuta la prueba unitest


##################################################### DESPLIEGUE DOCKER ###############################################

docker build -f Dockerfile -t koicebackend:latest .         --> construye la imagen del backend

docker run -p 5000:5000 -i --network host koicebackend      --> crea el contenedor y lo ejecuta ('-i' esta opcion mantiene la entrada de teclado abierta)

docker-compose up                                           --> crea y ejecuta el contenedor con el archivo docker-compose incluido