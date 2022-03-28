DIRSRCBACKEND := backend/

CFLAGS := -m
LDLIBS := aaa
CCBACKEND := python3

TEST:= test_kodiApi.py

all : runbackend runfrontend

runbackend:
	cd proyect/ && flask run

entervenv:
	 cd $(DIRSRCBACKEND) && pipenv shell && cd proyect/ && export FLASK_APP="main.py"

createbackend:
	export FLASK_APP="main.py"

test:
	cd proyect/ && $(CCBACKEND) -m unittest -v $(TEST)
