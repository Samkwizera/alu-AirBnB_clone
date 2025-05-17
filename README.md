# AirBnB Clone

## Project Description
This project is a clone of the AirBnB website, implementing a simplified version of the platform's core features. The project demonstrates the implementation of a full-stack web application, from the backend API to the frontend interface.

## Features
- Command interpreter to manage AirBnB objects
- Web static to learn HTML/CSS
- MySQL storage with SQLAlchemy ORM
- RESTful API with Flask
- Web dynamic with Flask
- Frontend with HTML/CSS

## Project Structure
```
alu-AirBnB_clone/
├── AUTHORS
├── README.md
├── console.py
├── models/
│   ├── __init__.py
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine/
│   │   ├── __init__.py
│   │   └── file_storage.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
├── tests/
│   ├── __init__.py
│   └── test_models/
│       ├── __init__.py
│       ├── test_amenity.py
│       ├── test_base_model.py
│       ├── test_city.py
│       ├── test_place.py
│       ├── test_review.py
│       ├── test_state.py
│       └── test_user.py
└── web_static/
    ├── images/
    │   ├── icon.png
    │   ├── icon_bath.png
    │   ├── icon_bed.png
    │   └── icon_group.png
    ├── styles/
    │   ├── 3-common.css
    │   ├── 3-footer.css
    │   ├── 3-header.css
    │   ├── 4-common.css
    │   ├── 4-filters.css
    │   ├── 5-filters.css
    │   ├── 6-filters.css
    │   ├── 7-places.css
    │   └── 8-places.css
    ├── 0-index.html
    ├── 1-index.html
    ├── 2-index.html
    ├── 3-index.html
    ├── 4-index.html
    ├── 5-index.html
    ├── 6-index.html
    ├── 7-index.html
    └── 8-index.html
```

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/alu-AirBnB_clone.git
```

2. Navigate to the project directory:
```bash
cd alu-AirBnB_clone
```

## Usage
### Console
The console is a command interpreter to manage AirBnB objects:
```bash
./console.py
```

Available commands:
- `create`: Creates a new instance of a class
- `show`: Shows the string representation of an instance
- `destroy`: Deletes an instance
- `all`: Shows all instances of a class
- `update`: Updates an instance's attributes

Example:
```bash
(hbnb) create User
(hbnb) show User 1234-1234-1234
(hbnb) all User
```

### Web Interface
The web interface is accessible through a web browser. Open any of the HTML files in the `web_static` directory to view different versions of the interface:

- `0-index.html`: Basic structure
- `1-index.html`: Added header
- `2-index.html`: Added footer
- `3-index.html`: Added filters
- `4-index.html`: Added search button
- `5-index.html`: Added locations and amenities filters
- `6-index.html`: Added dropdown functionality
- `7-index.html`: Added places section
- `8-index.html`: Enhanced places with detailed information

## Testing
Run the test suite:
```bash
python3 -m unittest discover tests
```

## Authors
- Samuel Kwizera Ihimbazwe (s.Ihimbazwe@alustudent.com)

## License
This project is part of the Holberton School curriculum and is open source.
