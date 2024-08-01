#!/bin/bash

YELLOW="\033[0;33m"
GREEN="\033[0;32m"
NC="\033[0m"

success() {
	echo -e "${GREEN}[*] $1${NC}"
}

warning() {
	echo -e "${YELLOW}[!] WARNING: $1${NC}"
}

rm -rf yoowallet/__pycache__
rm -rf yoowallet/*/__pycache__
success "Python cache has been cleaned!"

if [[ $1 = "all" ]]; then
	rm -rf dist/ build/ yoowallet.egg-info
	success "Build cache has been cleaned!"
fi
