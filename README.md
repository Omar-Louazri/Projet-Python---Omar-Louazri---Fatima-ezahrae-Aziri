# Student Management System

## Overview
This Python project manages student records, ranks them based on their final grades, and assigns them to their preferred academic fields based on availability. The system includes functionalities for both administrators and students.

## Features
### Administrator
- Add, edit, and delete student records.
- Manage available academic fields.
- Assign students to fields based on their grades and preferences.
- View student rankings.
- Manage field capacity.

### Student
- View personal ranking.
- View and edit field preferences.
- Check assigned field.

## Requirements
- Python 3.x
- `eleves.json` (stores student data)
- `filieres.json` (stores field data)
- `affectation.json` (stores assignment data)

## Usage
Run the script:
```sh
python script.py
```

Follow on-screen instructions to navigate through menus for both administrators and students.

## Data Structure
### `eleves.json`
Stores student records:
```json
[
  {
    "id": 1,
    "NomComplet": "John Doe",
    "note_final": 85.5,
    "liste_filliere_voulu": ["INDIA", "GBM", "IAA"]
  }
]
```

### `filieres.json`
Stores available academic fields:
```json
[
  {
    "filieres": [
      { "nomFiliere": "INDIA", "NbPlace": 10 },
      { "nomFiliere": "GBM", "NbPlace": 8 }
    ]
  }
]
```

### `affectation.json`
Stores assigned students:
```json
[
  { "id": 1, "NomComplet": "John Doe", "filiere": "INDIA" }
]
```

## Authors
Omar Louazri
Fatima-ezahrae Aziri


