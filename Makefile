all: wheel poetry syllables

wheel:
	pip install wheel
# Installs the poetry tools package
poetry:
	git clone https://github.com/hyperreality/Poetry-Tools.git;
	cd Poetry-Tools && pip install .;
	rm -rf Poetry-Tools

# Installs syllables package
syllables:
	pip install syllables;
