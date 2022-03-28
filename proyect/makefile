DIRSRCBACKEND := backend/
DIRSRCFRONTEND := frontend/

CFLAGS := -m
LDLIBS := aaa
CCBACKEND := python3
CCFRONTEND := npm

TEST:= test_kodiApi.py

all : runbackend runfrontend

runbackend:
	cd $(DIRSRCBACKEND)proyect/ && flask run

entervenv:
	 cd $(DIRSRCBACKEND) && pipenv shell && cd proyect/ && export FLASK_APP="main.py"

exportflask:
	cd proyect/ && export FLASK_APP="main.py"

runfrontend:
	cd $(DIRSRCFRONTEND) && $(CCFRONTEND) run serve

test:
	./$(DIRSRCBACKEND)proyect/ $(CCBACKEND) -m unittest -v $(TEST)
