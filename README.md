# Recipe Manager Application 🍳

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

A full-stack web application for managing recipes, built with Django backend and vanilla JavaScript frontend.
The Recipe Manager website template used was from "open source - Xiaoying Riley at 3rd Wave Media" which was modified to our liking for the project
The project used csv (Comma Separated Values) file as a database for easier transparency

## Features ✨

- **Recipe Management**: Create, read, update, and delete recipes
- **Ingredient Lists**: Manage shopping lists and ingredient inventories
- **Step-by-Step Instructions**: Detailed cooking directions
- **User System**: Basic user management functionality

## Project Structure 📁

```
recipe_manager/
├── .vs/ # Visual Studio configuration (exclude from git)
├── core/ # Django project core settings
├── recipe_manager/ # Main Django app
├── static/ # Frontend assets (JS, CSS, images)
│ ├── css/
│ ├── js/
│ └── images/
├── .gitattributes # Git configuration
├── README.md # This file
├── db.sqlite3 # SQLite database (dev only)
├── lists.csv # Shopping lists data
├── manage.py # Django management script
├── steps.csv # Recipe steps data
├── users.csv # User data
└── web.config # IIS deployment configuration


```


## Setup Instructions ⚙️

### Prerequisites
- Python 3.8+ [![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)]()
- Django 3.2+ [![Django](https://img.shields.io/badge/Django-3.2+-092E20?style=flat&logo=django&logoColor=white)]()

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/recipe-manager.git
cd recipe-manager

# Set up Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django

# Initialize the database
python manage.py migrate

```

### Run 
```
python manage.py runserver






