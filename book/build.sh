#!/bin/sh
docker run --rm -it -v "$(pwd)"/src:/book/src -v "$(pwd)"/book:/book/book peaceiris/mdbook:v0.4.18 build
