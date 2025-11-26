# Bridge Designer – Desktop UI

A modern desktop application for basic bridge structural calculations with interactive visualization. Built with Python and PySide6 for the FOSSEE Osdag Winter Internship 2025 screening task.

## Features

- 🎨 Clean, modern user interface with animated feedback
- 📊 Calculate deck weight, moments, and shear forces
- 🌉 Interactive structural schematic visualization
- 💾 Save/load analysis data as JSON
- ⌨️ Direct input via typing or arrow controls

## Installation

### Requirements
- Python 3.8+
- PySide6

### Setup
```bash
pip install PySide6
python bridge_ui_enhanced.py
```

## Usage

1. **Enter Parameters**: Span, width, girders, and live load
2. **Calculate**: Click ⚡ Calculate button for results
3. **View Results**: See values in result cards and schematic
4. **Save/Load**: Export or import configurations as JSON

### Input Methods
- Click and type directly in fields
- Use up/down arrow buttons
- Keyboard arrows when focused
- Mouse scroll wheel

## Calculations

The app uses simplified formulas:

- **Deck Weight**: `ρ × thickness × area` (ρ = 25 kN/m³, t = 0.2 m)
- **Uniform Load**: `(Weight / Span) + Live Load`
- **Moment**: `w × L² / 8`
- **Shear**: `w × L / 2`
- **Per-Girder**: `Total / Number of Girders`

> ⚠️ **Note**: Simplified calculations for demonstration only. Not for actual engineering design.

## File Structure

```
├── bridge_ui_enhanced.py    # Main application
├── README.md                # Documentation
└── requirements.txt         # Dependencies
```

## JSON Format

```json
{
  "inputs": {"span": 30.0, "width": 10.0, "girders": 4, "live": 5.0},
  "results": {
    "deck_self_weight_kN": 1500.0,
    "uniform_load_kN_per_m": 55.0,
    "total_moment_kN_m": 6187.5,
    "total_shear_kN": 825.0,
    "per_girder_moment_kN_m": 1546.875,
    "per_girder_shear_kN": 206.25
  },
  "timestamp": 1704067200
}
```

## Technology

- **Framework**: PySide6 (Qt for Python)
- **Language**: Python 3.8+
- **Graphics**: QPainter for custom schematic rendering
- **Styling**: Qt Style Sheets

## Troubleshooting

**PySide6 not found**
```bash
pip install --upgrade PySide6
```

**Import errors**
```bash
python -m pip install PySide6
```

## Purpose

This project demonstrates:
- Modern desktop UI design skills
- Understanding of basic structural calculations
- Software development capabilities relevant to Osdag

## Author

Developed by Aditya Wagh for FOSSEE Osdag Winter Internship 2025 screening task.

---

