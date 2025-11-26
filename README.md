Bridge Designer – Desktop UI

A simple desktop application built using Python Tkinter to calculate basic bridge parameters and display a structural schematic. Developed as part of the FOSSEE Osdag Winter Internship 2025 screening task under the Bridge Module UI – Desktop category.

Features

Modern and clean Tkinter-based user interface

Input fields for span, width, number of girders, and live load

Automatic calculation of:

Deck self-weight

Uniform load

Bending moment

Shear force

Per-girder moment and shear

Simple structural schematic visualization

Save input parameters as JSON

Input validation with clear error messages

Installation
Requirements

Python 3.8 or higher

Tkinter (included with Python by default)

To verify Tkinter installation:

python -m tkinter

Run the application
python bridge_ui.py

How It Works

The application performs simplified structural calculations using the following formulas:

Deck self-weight:
density × thickness × area

Uniform load:
(self-weight / span) + live load

Bending moment:
wL² / 8

Shear force:
wL / 2

Per-girder values:
total moment or shear ÷ number of girders

These formulas are for demonstration purposes only and are not intended for real engineering design.

File Structure
bridge_ui.py     # Main application code
README.md        # Documentation file

Purpose

This project showcases:

Ability to design a clean and user-friendly desktop UI

Understanding of basic bridge engineering calculations

Skills relevant to UI and software development tasks within the Osdag project
