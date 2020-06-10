install:
	git clone https://github.com/digling/word-formation-paper.git
	cd word-formation-paper; python setup.py develop
	echo "installed worforpy"
help:
	worforpy help
split:
	worforpy split-from-list TestData/German.tsv TestData/German-morphemes.tsv
length:
	worforpy check-length AnnotatedDatasets/Burmish.tsv


