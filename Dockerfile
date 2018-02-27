FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code
ADD . /code/

# Define environment variable
ENV NAME Monty

# Make port 80 available to the world outside this container
# EXPOSE 80

# Execute a shell directly when the container launches
CMD [ "sh", "-c", "echo $NAME" ]
