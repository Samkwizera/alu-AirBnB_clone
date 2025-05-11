# AirBnB Clone - Command Interpreter

Welcome to the AirBnB Clone project!

This project is a basic clone of the AirBnB backend system. It provides a **command-line interface (CLI)** to manage various types of objects, mimicking how a simple backend might function for an application like AirBnB. It's built using **Python** and stores data in **JSON format**.

---

## 📌 Project Description

This is the first phase of the AirBnB clone. The goal is to build a command interpreter that allows users to:

- Create, show, update, and delete instances of classes
- Persist data to a file using JSON serialization
- Reload data back into memory from storage
- Interact with objects using a custom shell environment

---

## 🧰 Technologies Used

- **Python 3.8+**
- **cmd** module (standard library)
- **Object-Oriented Programming (OOP)**
- **JSON** for storage
- Follows **PEP8** style guidelines

---

## 🗂️ Project Structure & File Content

### `console.py`

```python
#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
# (other imports...)

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    # command methods like do_create, do_show, etc.

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()