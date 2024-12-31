#!/bin/bash -x
set -e

NGRF_DIRS=(/mnt/c/Users/bigyi/Documents/OpenTTD/newgrf /mnt/c/Users/bigyi/OneDrive/Documents/OpenTTD/newgrf)
USAGE="usage: ./build.sh (default | install | bundle)"
BAD_ARGS=85
GRF_FILENAME=nj-names.grf
GRF_PATH="./out/$GRF_FILENAME"

sprites() {
	python3 generateNameBlock.py | sed '/^\/\/!NAMES!\/\//{
		r /dev/stdin
		d
		}' nj-names.nml > out/nj-names.nml
}

default() {
	mkdir -p out
	sprites
	nmlc --grf=out/$GRF_FILENAME out/nj-names.nml
}

install() {
	default
	if [[ -e $GRF_PATH ]]; then
		for dir in "${NGRF_DIRS[@]}"; do
			cp -v $GRF_PATH $dir
		done
		echo "Successfully installed."
	else
		echo "GRF path '$GRF_PATH' does not exist."
	fi
}

bundle() {
	rm nj-names.tar
	rm -r dist
	mkdir -p dist
	default
	cp out/$GRF_FILENAME dist
	cp README.md dist/readme.txt
	cp LICENSE dist/license.txt
	cp changelog.md dist/changelog.txt
	tar cvf nj-names.tar dist
}

clean() {
    echo "Cleaning installation dir..."
	for dir in "${NGRF_DIRS[@]}"; do
		[ -e "$dir/$GRF_FILENAME" ] && rm -v "$dir/$GRF_FILENAME"
	done
	echo "Cleaning complete."
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
elif [[ "$1" = "clean" ]]; then
	clean
else
	echo $USAGE
	exit $BAD_ARGS
fi