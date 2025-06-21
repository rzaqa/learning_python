# cyber_offence

Link for course - https://app.pluralsight.com/paths/skill/python-for-cyber-offense


Website for trainings - GlobalTickets:
https://github.com/RolandGuijt/ps-microservices-getting-started

# Install virtualenv for MacOs:
$ python3 -m venv venv_cyber

# Activate virtualenv for MacOs:
$ source venv_cyber/bin/activate

# Install virtualenv for Windows:
$ python -m venv venv_cyber
# Activate virtualenv for Windows:
$ venv_cyber\Scripts\activate

# Install requirements:
$ pip install -r requirements.txt


#Install docker 
$ brew install docker  (MacOs)
$ sudo apt install -y docker.io (Linux)$ sudo systemctl enable docker --now

# Install docker-compose
$ brew install docker-compose (MacOs)
$ sudo apt install docker-compose (Linux)
# Start docker
$ docker-compose up -d
# Stop docker
$ docker-compose down

# Pull latest python image
$ docker pull python:latest


# Create a new container
$ docker run -it --name python_cyber -v $(pwd):/app python:latest /bin/bash
OR
$ docker run -i -t python /bin/bash