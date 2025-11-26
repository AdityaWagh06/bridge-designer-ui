Bridge Designer – Desktop UI

A simple desktop application built with Python Tkinter to calculate basic bridge parameters and display a structural schematic. Created for the FOSSEE Osdag Winter Internship 2025 (Bridge Module UI – Desktop).

Features

Clean and modern Tkinter interface

Input fields for span, width, girders, and live load

Calculates deck self-weight, uniform load, moment, shear, and per-girder values

Displays a simple bridge schematic

Saves input data to JSON

Input validation with clear error messages

Installation

Install Python 3.8+

Tkinter is included by default (check using python -m tkinter)

Run the application:

python bridge_ui.py

How It Works

The app uses simplified formulas for demonstration:

Self-weight = density × thickness × area

Uniform load = (self-weight / span) + live load

Moment = wL² / 8

Shear = wL / 2

Per-girder values = moment/shear ÷ number of girders

Files
bridge_ui.py     # Application source code
README.md        # Project documentation

Purpose

This project demonstrates a clean UI, basic structural calculations, and desktop interface development skills relevant to the Osdag project.