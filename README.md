Create a .env file in the project root directory and set your environment variables. You can copy the example .env.example file and customize it as needed.

shell

cp .env.example .env

Build and start the Docker containers using Docker Compose:

shell

docker-compose build
docker-compose up -d

Apply migrations and create a superuser:

shell

docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

Access the API at http://localhost:8000/. The admin interface is available at http://localhost:8000/admin/.

Usage

    Register a user: POST request to /api/register/ with username, email, and password.
    Obtain a token: POST request to /api/token/ with username and password.
    Use the obtained token in the Authorization header for protected endpoints.

Endpoints

    /api/register/: User registration
    /api/token/: Token authentication
    /api/books/: List of books and book creation (requires authentication)
    /api/books/{id}/: Retrieve, update, or delete a book by ID (requires authentication)

Testing

To run tests, use the following command:

shell

docker-compose exec web python manage.py test

Database Initialization

If you need to initialize the database or apply new migrations, use the following commands:

shell

docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
