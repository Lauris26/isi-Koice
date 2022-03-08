############################################ alternativa a venv y virtualenv ##########################################
pip install pipenv                          --> instala el paquete de entornos virtuales pipenv
pipenv shell                                --> crea un entorno virtual con el nombre de la carpeta actual y entra a el (en caso de estar creado unicamente entra a el)
pipenv exit                                 --> sale del entorno virtual


pipenv install -r requirements.txt          --> instala las dependencias necesarias
pip freeze > requirements.txt               --> guarda las depdencias actuales

################# exporta la variable de entorno para tu sistema operativo y consola de comandos usada ################
export FLASK_APP="main.py"                  --> LINUX/MAC;           declara la variable de entorno para ejecutar el servidor (export linux/mac)
set FLASK_APP=main.py                       --> WINDOWS/CMD;         declara la variable de entorno para ejecutar el servidor (set windows CMD)
$env:FLASK_APP = "main.py"                  --> WINDOWS/POWERSHELL;  declara la variable de entorno para ejecutar el servidor ($env: windows PowerShel)
#######################################################################################################################

flask run                                   --> ejecuta el servidor flask con la aplicacion definida en el entorno