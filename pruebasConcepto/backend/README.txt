pipenv install -r requirements.txt          --> instala las dependencias necesarias
pip freeze > requirements.txt               --> guarda las depdencias actuales

export FLASK_APP="main.py"                  --> declara la variable de entorno para ejecutar en el servidor (export linux/mac)
set FLASK_APP=main.py                       --> declara la variable de entorno para ejecutar en el servidor (set windows CMD)
$env:FLASK_APP = "main.py"                  --> declara la variable de entorno para ejecutar en el servidor ($env: windows PowerShel)

flask run                                   --> ejecuta el servidor flask con la aplicacion definida en el entorno