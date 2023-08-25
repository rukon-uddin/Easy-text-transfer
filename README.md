# Simple Text Sharing using Python, Flask, and Redis

![Project Image](https://raw.githubusercontent.com/rukon-uddin/Easy-text-transfer/python_code/assets/ezgif.com-optimize.gif) <!-- If you have a project image, add it here -->

A simple web application that allows users to share text using a unique ID. Users can assign a unique ID to their text and share it with others. Others can then retrieve the text using that unique ID.

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Demo

https://www.linkedin.com/posts/rukonuddin_python-flask-redis-activity-7100770400803983360-_mqB?utm_source=share&utm_medium=member_desktop
## Features

- Share text using a unique ID.
- Retrieve text using the unique ID.
- Lightweight and easy-to-use web interface.
- Utilizes Flask for web application framework.
- Uses Redis for storing and retrieving shared text.

## Getting Started

### Prerequisites

- Python 3.7
- Flask
- Redis

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rukon-uddin/Easy-text-transfer
   git checkout python_code
   ```
2. Navigate to the project directory:
    ```bash
    cd Easy-text-transfer
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Usage:
    ```bash
    gunicorn app:app or python app.py
    ```
### License

This project is licensed under the [MIT License](LICENSE).

### Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Redis](https://redis.io/)
- [Gunicorn](https://gunicorn.org/)
