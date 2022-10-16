FROM node:16.18.0 AS builder

COPY /ui /app

# switch working directory
WORKDIR /app

RUN npm install ci && npm run build


# start by pulling the python image
FROM python:3.8 AS server

# copy the requirements file into the image
COPY --from=builder /app/dist /app/static
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["server.py" ]