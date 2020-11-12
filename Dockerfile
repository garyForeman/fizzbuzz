FROM python:3.8.3

LABEL maintainer="gary.foreman.42@gmail.com"

# Make port 80 available to the world outside this container
EXPOSE 80

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./*.py ./

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]