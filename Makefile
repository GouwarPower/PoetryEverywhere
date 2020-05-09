# Installs the poetry tools package 
all:
	git clone https://github.com/hyperreality/Poetry-Tools.git;
	cd Poetry-Tools && pip install .;
