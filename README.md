# Virtual Store Project

A Python-based virtual store management system that handles both digital and physical products, with features for managing clients, orders, and reviews.

![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
[![Documentation Status](https://img.shields.io/badge/docs-latest-brightgreen.svg)](docs/build/html/index.html)

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [Development Setup](#development-setup)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Features
- Product Management
  - Support for both digital and physical products
  - Stock management
  - Product categorization
- Client Management
  - Client registration and tracking
  - Client information management
- Order Processing
  - Order creation and management
  - Order total calculation
- Review System
  - Product review management
- User-friendly CLI Interface
  - Clear menu navigation
  - Input validation and error handling

## Installation

1. Clone the repository
   ```bash
   git clone [repository-url]
   cd Virtual_Store
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main application:
```bash
python src/main.py
```

The application provides a menu-driven interface with the following options:
1. Client Management
2. Product Management
3. Order Management
4. Review Management

## Project Structure
```
src/
├── models/
│   ├── C01_Product.py         # Base product class
│   ├── C01A_DigitalProduct.py # Digital product implementation
│   ├── C01B_PhysicalProduct.py# Physical product implementation
│   ├── C02_Client.py          # Client management
│   ├── C03_Order.py           # Order processing
│   └── C04_Review.py          # Review system
├── modules/
│   ├── menu_functions.py      # Menu functionality
│   └── menu_utils.py          # Utility functions
└── main.py                    # Application entry point
```

## Documentation

The project documentation is built using Sphinx and can be found in the `docs` directory. To build the documentation:

```bash
cd docs
make html
```

Then open `docs/build/html/index.html` in your web browser.

## Development Setup

To set up the project for development:

1. Fork the repository
2. Create a new branch for your feature
3. Install development dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Make your changes
5. Update documentation if necessary
6. Submit a pull request

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests and documentation as appropriate.

## Author

Issa El Mokadem

