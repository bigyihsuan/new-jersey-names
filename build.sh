#!/bin/bash -x

NGRF_DIR=/mnt/c/Users/bigyi/OneDrive/Documents/OpenTTD/newgrf/
USAGE="usage: ./build.sh (default | install | bundle)"
BAD_ARGS=85

sprites() {
	python3 generateNameBlock.py | sed '/^\/\/!NAMES!\/\//{
		r /dev/stdin
		d
		}' nj-names.nml > out/nj-names.nml
}

default() {
	mkdir -p out
	sprites
	# nmlc --nfo=out/nj-names.nfo --grf=out/nj-names.grf --palette=DOS out/nj-names.nml
	nmlc --grf=out/nj-names.grf out/nj-names.nml
}

install() {
	default
	if [[ -e "./out/nj-names.grf" ]]; then
		cp ./out/nj-names.grf $NGRF_DIR
	fi
}

bundle() {
	rm nj-names.tar
	rm -r dist
	mkdir -p dist
	default
	cp out/nj-names.grf dist
	cp README.md dist/readme.txt
	cp LICENSE dist/license.txt
	cp changelog.md dist/changelog.txt
	tar cvf nj-names.tar dist
}

if [[ "$#" -eq 0 ]]; then
	default
	exit 0
fi

if [[ "$1" = "sprites" ]]; then
	sprites
elif [[ "$1" = "default" ]]; then
	default
elif [[ "$1" = "install" ]]; then
	install
elif [[ "$1" = "bundle" ]]; then
	bundle
else
	echo $USAGE
	exit $BAD_ARGS
fi