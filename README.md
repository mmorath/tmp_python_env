# What is it about  #
A simple example how to use pydantic https://pydantic-docs.helpmanual.io/
...some intresting links 
 * https://github.com/squidfunk/mkdocs-material
 * https://www.youtube.com/watch?v=X-LbOBAd-xg
 * https://www.youtube.com/watch?v=0pYN6Z-t1-s 
 * https://www.youtube.com/watch?v=b4iFyrLQQh4  Spinx 
 * https://www.youtube.com/watch?v=0YUdYk5E-w4  #6: Python Docstrings | Python Best Practices

# What do you need to play around #

1. Computer any type
2. OS--> Windows, MacOS, Linux
3. I use VisualCode...but is not a must  https://code.visualstudio.com/
4. Docker to be installed  --> https://docs.docker.com/desktop/windows/install/
5. Git...for cloning and contritbuting to this repository http://git-scm.com/book/de/v2/Erste-Schritte-Git-installieren

# How to clone this repository #
1. Open git bash 
    ```bash
    cd ~
    mkdir workspace
    cd workspace 
    mkdir github
    cd github
    git clone https://github.com/mmorath/cisco.git
    cd cisco
    code .
    ```
# Install some nice plugins for visual code #
2. Install nice plugins in vcode 
  * docker
  * Github
  * Python
  * Pylance
  * YAML

# First steps in docker-compose 
    ```bash
    #check if ocntainer is running
    docker ps
    #build ansible docker container using docker-compose
    docker-compose -f docker-compose-ansible.yml build
    #start the container
    docker-compose -f docker-compose-ansible.yml up -d
    #log into ansible
    docker exec -it ansible bash
    ```
# Inisde of the container 
    ```bash
    #activating the virtual enviroment
    root@ansible:/usr/src/app# source venv/bin/activate
    (venv) root@ansible:/usr/src/app# 
    #deactivatin the virtual enviromen
    (venv) root@ansible:/usr/src/app#deactivate
    ```
