# server-app-pep

1. Created env  using command :  python3 -m venv venv 
2. Activate env  : source venv/bin/activate 
3. install : pip install fastapi
4. install : pip install "uvicorn[standard]"
5. add main.py
6. setup git remote and add git required files
7. add dockerfile
8.  

## Steps to run application from docker 

Open Docker applictaion :

###  Run the following commands in terminal : 

### `docker pull pavanpogula/server-app-pep:latest`

docker container run -d -p 3000:3000 --platform linux/amd64 pavanpogula/server-app-pep:b2977611c0c867133a0913badb6adf75fa42e6a7