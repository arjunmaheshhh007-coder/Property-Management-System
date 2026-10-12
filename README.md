# Commercial Property Management System

## About the Project

The Commercial Property Management System is a desktop application developed using Python and Tkinter. It provides a graphical interface for managing commercial property information and allows users to browse and search available properties.

This project was developed as part of my first-year Computer Science studies at Cardiff Metropolitan University.

## Technologies Used

- **Python** — application logic
- **Tkinter** — graphical user interface (GUI)
- **CSV** — file-based data storage

## Features

### Administrator
- Admin login interface
- Add new commercial property records
- View stored properties
- Search properties by type
- Add administrator accounts
- Store property information in CSV files

### General User
- View property information
- Search properties by type
- Access a simplified, read-only interface

## Property Information

The application manages details such as:

- Property type
- Number of floors
- Property size
- Parking information
- Availability for lease or purchase
- Cost

## Project Structure

```text
Property-Management-System/
├── property_management_system.py
├── properties.csv
├── admins.csv
└── README.md
```

The CSV files should contain safe sample data only. Do not commit real credentials or private information.

## How to Run

1. Install Python 3 from https://www.python.org/.
2. Download or clone this repository.
3. Open the project folder in VS Code or PyCharm.
4. Ensure the Python installation includes Tkinter.
5. Run the following command from the project directory:

```bash
python property_management_system.py
```

The application should open in a desktop window.

## What I Learned

Through this project, I practised:

- Python functions and application logic
- Creating GUI screens with Tkinter
- Handling user input
- Reading and writing CSV files
- Implementing basic login functionality
- Organising a multi-screen desktop application

## Future Improvements

- Improve input validation and error handling
- Implement secure password storage
- Add property editing and deletion
- Introduce a database instead of CSV storage
- Improve the user interface and accessibility

## Academic Context

**Course:** BSc (Hons) Computer Science  
**University:** Cardiff Metropolitan University  
**Project:** First-year academic project

This repository showcases my learning and development in Python programming and desktop application development.
