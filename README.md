#### PASSWORD MANAGER

![Screenshot (7)](https://github.com/NIGASH333/Password-Manager/assets/113447646/872e1e5a-ed85-427c-a8c1-930cd241f48c)


![Screenshot (8)](https://github.com/NIGASH333/Password-Manager/assets/113447646/bb1c4738-ab1d-4128-8e27-cb6e6fc10a30)


![Screenshot (2)](https://github.com/NIGASH333/Password-Manager/assets/113447646/6c578e8d-6062-4cb1-b5ae-8546159112dd)


![Screenshot (5)](https://github.com/NIGASH333/Password-Manager/assets/113447646/68dffd09-6fea-47eb-97d8-df623400d93a)


![Screenshot (6)](https://github.com/NIGASH333/Password-Manager/assets/113447646/7311a72c-bbc7-4f51-a522-b789631a3f83)


# 🔒 Secure Pass Vault

Secure Pass Vault is a password manager application built using Python and Tkinter. It allows users to securely store and manage their passwords for various accounts.

## Features

- **Login Screen**: Users can log in to their account using their username and password.
- **Create Account**: New users can create an account with a unique username and password.
- **Main Screen**: After logging in, users are presented with a main screen where they can view, add, update, and delete password records.
- **Search and Filter**: Users can search for specific records and filter them based on different criteria.
- **Password Encryption**: Passwords are securely hashed using bcrypt before being stored in the database.
- **Responsive UI**: The user interface is designed using Tkinter, providing a simple and intuitive user experience.

## Requirements

- Python 3.x
- Tkinter
- mysql-connector-python library
- Bcrypt Module 

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/NIGASH333/secure-pass-vault.git
    ```

2. Install the required dependencies. Navigate to the project directory and install the dependencies using pip:

    ```bash
    cd secure-pass-vault
    pip install -r requirements.txt
    ```

3. Set up the MySQL database:
    - Create a MySQL database named `passwords_manager`.
    - Update the database connection details in the code if necessary.

4. Run the application:

    ```bash
    python main.py
    ```

## Usage

- Upon launching the application, users can log in with their existing credentials or create a new account if they're new users.
- After logging in, users can add, view, update, or delete password records.
- The application provides search and filter functionalities to help users manage their passwords efficiently.

## Contributors

- [NIGASH](https://github.com/NIGASH333) 🚀🌟

## License

This project is licensed under the [GPL-3.0 License](LICENSE). 📝

