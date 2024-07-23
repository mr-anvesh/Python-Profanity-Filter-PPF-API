

# Profanity Filter API

A Python-based API that filters and replaces profanity words in text input using a MySQL database. The API replaces profane words with asterisks (`*`) of the same length.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Filters and replaces profane words from a text input.
- Case-insensitive matching.
- Uses MySQL database to store profanity words.
- RESTful API built with Flask.
- Easily deployable to cloud platforms like Heroku.

## Requirements

- Python 3.6+
- MySQL

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/profanity-filter-api.git
   cd profanity-filter-api
   ```

2. **Install Required Libraries**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up MySQL Database**

   Ensure MySQL is installed and running. Create a database and table for storing profanity words.

   ```sql
   CREATE DATABASE pwords;

   USE pwords;

   CREATE TABLE profanitywords (
       id INT AUTO_INCREMENT PRIMARY KEY,
       word VARCHAR(255) NOT NULL
   );

   INSERT INTO profanitywords (word) VALUES ('badword1'), ('badword2'), ('badword3');
   ```

## Configuration

Update the `DATABASE_URI` in `app.py` to match your MySQL credentials:

```python
DATABASE_URI = 'mysql+mysqlconnector://username:password@localhost/pwords'
```

## Usage

1. **Run the Flask Application**

   ```bash
   python app.py
   ```

2. **Test the API**

   Use Postman or curl to test the API. Example using curl:

   ```bash
   curl -X POST http://127.0.0.1:5000/filter -H "Content-Type: application/json" -d '{"text": "This is a badword1 and another badword2"}'
   ```

   Expected response:

   ```json
   {
       "filtered_text": "This is a ******* and another *******"
   }
   ```
## Contributing

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```


