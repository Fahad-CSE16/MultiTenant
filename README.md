# BasicProjectOnly

1. **Teams**
   - *FrontEnd (React.js)*
     - [Md Fahad Hossain](https://www.facebook.com/fahad.cse16)
   - *Backend (Python Django and REST framework)*
     - [Md Fahad Hossain](https://www.facebook.com/fahad.cse16)
2. **Description**
   - *Subprojects*
     - Only Setup
## Run Manually

##### Step 1 : Run these command after cloning (Django)
```
virtualenv venv
source venv/bin/activate 

```
for windows OS: 
```
python -m venv venv
venv/Scripts/activate 

```
```
pip install -r requirements.txt
```
If any error occurs then run 
```
pip install -r requirements_raw.txt
```
##### Step 2 : Start Django Server 
```
python manage.py runserver
```
##### Everytime after pulling any error shows up then after activating virtualenv
```
pip install -r requirements.txt
python manage.py runserver
```

## Run Using Docker 
##### Step 1 : First Install docker & docker-compose (if already installed then skip this step)
```
sudo apt update
sudo apt upgrade
sudo apt install docker.io
```
<b> Install Docker compose </b>
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

##### Step 2 : To run the app using docker aslo  Everytime after pulling any error shows up

```
docker-compose build
docker-compose up
sudo chown -R $USER:$USER .
```

##### Run Redis: Start Docker and enter the following command to enable it after every time the system reboots.
```
sudo systemctl enable --now docker
```
###### To disable it again, simply type in the following command.
```
sudo systemctl disable --now docker
```
```
sudo usermod -aG docker YourUsername
sudo chmod 666 /var/run/docker.sock
docker run -p 6379:6379 -d redis:5
```
###### if any error shows up then run this command
```
sudo apt-get install net-tools
sudo netstat -pna | grep 6379 
docker run -p 6379:6379 -d redis:5
```

##### To perform any operation/command on docker container 
```
docker ps
```
copy your required image Name
```
docker exec imagename1 your-command
docker exec front npm run build
docker exec back python manage.py migrate
docker exec back python manage.py collectstatic
```
