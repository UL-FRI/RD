docker build --rm -t rd-update .
docker run --rm -i -p 8889:8888 -v "$PWD/..":/home/jovyan/work -w /home/jovyan/work rd-update
