This is my learning of setting up Docker with MariaDB running within and notes for reference docs.
# Links to instructions
[Japanese translation: 使い方](#使い方)
# Reference documents
# How to set up Docker with MariaDB
[How to set up Docker with MariaDB](https://hub.docker.com/_/mariadb)
## expose vs ports in Docker 
[expose](https://docs.docker.com/compose/compose-file/compose-file-v3/#expose)

[ports](https://docs.docker.com/compose/compose-file/compose-file-v3/#ports)

expose: Expose ports w/out publishing them to the host machine. i.e. host machine can't access it.
ports: Defined as `HOST:CONTAINER`, expose ports both host machine and container. 

# Docker compose vs Dockerfile
Docker compose is a tool for defining and running multiple docker container application. 
Dockerfile contains the commands that user can run on the command line to assemble an image. 
[Dockerfile reference](https://docs.docker.com/engine/reference/builder/)

# Writing application 
[Writing application using Docker](https://docs.docker.com/language/python/develop/)
[Containerized docker dev 2](https://www.docker.com/blog/containerized-python-development-part-2/)
# Dump the database running in the Docker container. 
```commandline  
sudo docker exec <container name> sh -c 'mysqldump <db name> <table name> -u <user> -p"<password>" ' > ./all-database.sql
```

# Redis
[Redis site](https://redis.io/)

> Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker
# SQLAlchemy
[SQLAlchemy](https://www.sqlalchemy.org/)

# 使い方
## インストールするもの
### Docker 
インフラとアプリを同時に管理するプラットフォーム。同時に管理することによって開発環境そのままをプロダクションに移行できるので、インフラ環境の違いの
すり合わせをなくすことができ、早くリリースできるようになる。

[Dockerをダウンロードしてインストールする方法](https://docs.docker.jp/desktop/index.html#desktop-download-and-install)

### Docker Compose
Docker Compose とは、複数のコンテナを定義し実行する Docker アプリケーションのためのツール
[Docker Compose のインストール](https://docs.docker.jp/compose/install.html)

