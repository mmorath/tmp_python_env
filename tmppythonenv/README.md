# readout
This app reads out the configuraiton of the switch using modbus tcp ip

TODO #  create script for buiding automatically the docker images <br>

## How to install enviroment
In order to have the same enviroment ...a shell script which will install the necessary tools on a debian based enviroment
```bash 
installEnv.sh
```

## How to build the docker image
The folder does include a dockerfile...so in order to build the image, make sure that docker is installed on your machine.
Replace Reg with your general registry if avaliable, Repo with the name of your repository aka. your container. Latest for latest or if you want to stick to a version, add your version there for example (e4tc/cisco:1.0.0)
```bash 
docker build ./ -t reg/repo:latest
```

## How to run the docker build docker container
To run the docker container, make sure to expose the necessary ports and to provide a name for your docker container.
```bash 
docker run -d --expose 1883 --name containerName reg/repo:latest
```

## Testing the individual classes
Each class can be started on its own, this is due to...
```bash 
if __name__ == "__main__":
```
For running the script without docker...ensure to activate the enviroment prior starting the script.
```bash 
source venv/bin/activate
./start.py
```

## Extend the packages....
In order to install additional packages with pip...please make sure that the venv is active and 
install for exampel flask this way....do not forget to save the new model with the pip freeze command...
```bash 
source venv/bin/activate
pip install flask
pip freeze > requirements.txt
```
in order to show what is currently installed use the pip list command..if the new package is not visible there...then check the file permissions and if the venv is active...
```bash 
source venv/bin/activate
pip list
Package       Version
------------- -------
paho-mqtt     1.5.1  
pip           18.1   
pkg-resources 0.0.0  
setuptools    40.8.0 
```
