#!/bin/sh
docker run --rm -v "$(pwd)"/src:/book/src -v "$(pwd)"/book:/book/book -p 3000:3000 peaceiris/mdbook:v0.4.18 serve -n 0.0.0.0
