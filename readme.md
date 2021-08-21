# Description

This is a simple budgeting GUI script built from tkinter

# Usage

Execute the main.py file in the commandline to constuct GUI. All customization of GUI menu labels, function mappings and media are handled in the __init__.
The media files are contained in this repo.

# Python Environment

This script runs on Python 3.9.4.

# Dependencies

The only dependency is for Pillow 3.8.0, used to handle jpg files.

# Design Choices

The entire GUI is contained in a single class in budget_gui.py. The approach was used to code reusability, but a procedural script may have been just as effective.
A command line script of the same application is in budget.py.