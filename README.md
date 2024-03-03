# User Profile Application

This Django application allows users to create user profiles with basic information such as first name, surname, email address, and phone number.

## Prerequisites

- Python 3.11
- pip 24.0 (Python package installer)
- Django-5.0.2

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv myworld
    source myworld/bin/activate  # For Unix/Mac
    .\myworld\Scripts\activate   # For Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run database migrations:

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

2. Start the development server:

    ```bash
    python3 manage.py runserver
    ```

3. Navigate to `http://127.0.0.1:8000/profiles/create/` in your web browser to create a user profile.

4. After submitting the form, you'll be redirected to a page confirming that the profile was created.

## License

This project is licensed under the [MIT License](LICENSE).
