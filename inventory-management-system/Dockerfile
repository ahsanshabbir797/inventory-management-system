# base image
FROM python:3.12-slim

# setup working directory in container
WORKDIR /inventory_management_system

# copy all files to inventory_management_system directory
COPY . /inventory_management_system/

COPY .venv /inventory_management_system/.venv

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry install --network-timeout 300


# Expose the default Streamlit port
EXPOSE 8501

# Command to run Streamlit on container start
CMD ["poetry", "run", "streamlit", "run", "inventory_management_system/main.py"]
