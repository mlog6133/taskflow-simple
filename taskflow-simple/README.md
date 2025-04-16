# TaskFlow - Simple Team Task Management Web App

TaskFlow is a simple web-based task management application designed to help small teams organize and track their tasks efficiently. The app includes basic features like user authentication, task creation, task assignment, status updates, and a dashboard overview. This project demonstrates core software development concepts, including both frontend and backend technologies.

## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow these steps to install and run the application on your local machine:

1. Clone the repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/taskflow-simple.git
    ```

2. Navigate into the project folder:
    ```bash
    cd taskflow-simple
    ```

3. Set up a virtual environment (if using Python):
    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the application:
    ```bash
    python app.py
    ```

7. Open your browser and navigate to `http://localhost:5000` to access the app.

## Features

- **User Authentication**: Secure login and registration system.
- **Task Creation**: Create tasks with titles, descriptions, and due dates.
- **Task Assignment**: Assign tasks to specific team members.
- **Status Updates**: Tasks can be marked as "To Do", "In Progress", or "Completed".
- **Dashboard Overview**: View all tasks with their statuses in one place.
- **Responsive Design**: Fully functional on both desktop and mobile devices.

## Screenshots

Here are some screenshots of the application:

1. **Login Page**:
   ![Login](screenshots/login.png)

2. **Dashboard**:
   ![Dashboard](screenshots/dashboard.png)

3. **Task Creation**:
   ![Task Creation](screenshots/create_task.png)

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: SQLite
- **Authentication**: Flask-Login
- **Styling**: CSS for a simple and responsive layout

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with improvements or bug fixes. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
