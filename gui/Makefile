.PHONY: clean

fich= $(shell ls *.ui) #Récupère tous les .ui
fichPy= $(patsubst %.ui, %.py, $(fich))

all:$(fichPy)

#Pour chaque .ui on crée un .py
%.py : %.ui
	pyuic5 $< -o $@

clean :
	rm *.py
