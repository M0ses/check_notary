test:
	perl -c ./check_notary
	perltidy -b -g ./check_notary
	perlcritic --verbose 8 --brutal ./check_notary
