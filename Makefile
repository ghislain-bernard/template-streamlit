############################################## ghislain.bernard@gmail.com ##############################################

all: clean

SHELL = /usr/bin/env bash

########################################################################################################################

clean:
	@echo ''
	@echo -e '/!\ cleaning...'

	rm --force --recursive --verbose module/__pycache__

	@echo ...done

############################################## ghislain.bernard@gmail.com ##############################################
