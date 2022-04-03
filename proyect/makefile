DIRSRCBACKEND := backend/
DIRSRCFRONTEND := frontend/

CFLAGS := -m
LDLIBS := null
CCBACKEND := python3
CCFRONTEND := npm

TEST:= test_kodiApi.py

all : runbackend runfrontend

runfrontend:
	cd $(DIRSRCFRONTEND) && $(CCFRONTEND) run serve

runbackend:
	cd $(DIRSRCBACKEND) && pipenv run $(CCBACKEND) ./proyect/main.py

entervenv:
	 cd $(DIRSRCBACKEND) && pipenv shell

installdeps: installdepsfrontend installdepsbackend

installdepsfrontend:
	cd $(DIRSRCFRONTEND) && npm install

installdepsbackend:
	cd $(DIRSRCBACKEND) && pipenv install

test:
	./$(DIRSRCBACKEND)proyect/ $(CCBACKEND) -m unittest -v $(TEST)
