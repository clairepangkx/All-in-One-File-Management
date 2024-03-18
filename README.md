# All-in-One File Management System

The All-in-One File Management System is designed to automate the organization of files across your Desktop and Download folders, moving them into a centralized "All-in-One" folder, and maintaining a detailed database for easy file management and retrieval. This project is structured into two main components, housed within the "ManagerProgram" directory: 

- `filesMover`: Contains scripts for scanning specified directories and moving files.
- `databaseManager`: Manages the database operations including file tracking, updates, and data export functionalities.

## Features

- **File Mover Program:** Scans files in the Desktop and Download folders, moving them to the "All-in-One" folder for centralized file management.
- **Database Management Program:** Handles database operations, tracking file movements, updates, and providing an option to export the database contents for review.

## Getting Started

### Prerequisites

- Python 3.6 or later installed on your system.
- SQLite3 for database management (included with Python).

### Installation

1. Clone the GitHub repository to your local machine:
    ```
    git clone https://github.com/clairepangkx/all-in-one-file-management.git
    ```
2. Navigate to the cloned repository directory:
    ```
    cd all-in-one-file-management
    ```
3. Install the required Python libraries:
    ```
    pip install sqlite3
    ```

## Usage

Before running the scripts, ensure the `watch_path` and `destination_root` are configured according to your system's directory structure in both `FileProcessor.py` and `DB_processor.py`.

### File Mover Program

To execute the file mover program:

```bash
python /path/to/ManagerProgram/filesMover/move2AllinOne.py
```

### Database Management Program

To manage the database, including updating and exporting data:

```bash
python /path/to/ManagerProgram/databaseManager/DB_processor.py
python /path/to/ManagerProgram/databaseManager/DB_exporter.py
```

### Automating Execution with Cron Jobs

To run these programs periodically on a MacBook, you can set up cron jobs:

1. Open Terminal and edit the crontab file:
    ```
    export EDITOR='nano'
    crontab -e
    ```
2. Add cron jobs for each script according to your schedule. Example entries:
    ```cron
    # File Mover Program: Run at 11:00 and 21:00 every day
    0 11,21 * * * /path/to/your/python /path/to/ManagerProgram/filesMover/move2AllinOne.py

    # Database Processor and Exporter: Run at 11:30 and 21:30 every day, export on Saturdays at 12:00
    30 11,21 * * * /path/to/your/python /path/to/ManagerProgram/databaseManager/DB_processor.py
    0 12 * * 6 /path/to/your/python /path/to/ManagerProgram/databaseManager/DB_exporter.py
    ```
    Remember to replace /path/to/your/python with the actual path to your Python executable, which you can find by running which python or which python3 in your terminal. Also, adjust 
    the paths to the script files according to where you've placed the cloned repository on your system.


3. Save and close the crontab.

## Contributing

We welcome contributions to the All-in-One File Management System. Feel free to submit pull requests or report issues for any bugs or additional features you think would make this project even better.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
