# MicroBit

**MicroBit** is a lightweight and straightforward blogging web application built using Flask, SQLAlchemy, and Bootstrap 5. It provides a minimalistic platform for users to create, edit, and manage blog posts.

## Features

- **User Authentication:** Secure login and registration with password hashing.
- **Post Management:** Create, update, delete, and view blog posts.
- **Responsive Design:** A clean and responsive UI using Bootstrap 5.
- **Database Migrations:** Easy setup and updates with Flask-Migrate.

## Getting Started

### Prerequisites

- Python 3.x
- Flask and other dependencies listed in `requirements.txt`

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AzzyCode/MicroBit.git
   cd MicroBit

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Set up the database:**
    ```bash
    flask db upgrade

5. **Run the application:**
    ```bash
    flask run


## Screenshots

### Home Page
![Home Page](https://github.com/user-attachments/assets/c7fbacb7-ef53-4d5c-b9b4-67d6385f0b84)

## Explory Page
![Explore Page](https://github.com/user-attachments/assets/09cf2edc-8c3d-4438-96b8-b8bd10d8f5af)


## Development

To start development, ensure your environment is set up with the necessary dependencies and the database is initialized. Use a tool like flask shell for interactive work and pytest for testing.

## Acknowledgements
This project was developed as part of a tutorial from Flask Mega-Tutorial. Special thanks to Miguel Grinberg for providing the resources and guidance.