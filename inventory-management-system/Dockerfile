# base image
FROM python:3.12-slim

# setup working directory in container
WORKDIR /inventory_management_system

# copy all files to apinventory_management_systemp directory
COPY . /inventory_management_system/

RUN poetry install

# command to run on container start
CMD ["poetry", "run", "python", "inventory_management_system/main.py"]