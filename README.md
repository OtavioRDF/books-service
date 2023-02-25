# books-service
Books service is a REST API developed for a microservices study, where the final application will be a library website.

## Run Locally

Clone the project

```bash
  git clone https://github.com/OtavioRDF/books-service.git
```

Go to the project directory

```bash
  cd books-service
```

Install dependencies

```bash
  pip install -r requirements
```

Start the server

```bash
  uvicorn app.main:app
```

## You can also run it with docker

Go to the project directory

```bash
  cd books-service
```

Build the containers

```bash
  docker compose build
```

Run the containers

```bash
  docker compose up
```