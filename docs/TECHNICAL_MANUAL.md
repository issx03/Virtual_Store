# Virtual Store Technical Manual

## Table of Contents
1. [System Architecture](#system-architecture)
2. [Class Hierarchy](#class-hierarchy)
3. [Module Documentation](#module-documentation)
4. [Data Structures](#data-structures)
5. [Development Guidelines](#development-guidelines)
6. [Maintenance](#maintenance)

## System Architecture

The Virtual Store system follows a modular architecture with clear separation of concerns:

```
Virtual Store
├── models/           # Data models and business logic
├── modules/          # Utility functions and menu handling
└── main.py           # Application entry point
```

### Core Components
1. **Models Layer** - Business logic and data structures
2. **Modules Layer** - Utility functions and user interface
3. **Main Application** - Program flow and user interaction

## Class Hierarchy

### Product Hierarchy
```
Product (Base Class)
├── DigitalProduct
└── PhysicalProduct
```

#### Product (Base Class)
- **Attributes**:
  - `__id`: str - Unique identifier
  - `__name`: str - Product name
  - `__price`: float - Product price
  - `__stock`: int - Available quantity

- **Methods**:
  - Properties for all attributes (getters/setters)
  - `act_stock(quantity)`: Update stock quantity
  - `_strip_lower(string)`: Utility for string normalization

#### DigitalProduct
- **Additional Attributes**:
  - `__format`: str - File format
  - `__file_size`: float - Size in MB

#### PhysicalProduct
- **Additional Attributes**:
  - `__weight`: float - Weight in kg
  - `__dimensions`: str - Physical dimensions

### Supporting Classes
- **Client**
  - Manages customer information
- **Order**
  - Handles order processing
- **Review**
  - Manages product reviews

## Module Documentation

### main.py
Main application module implementing the menu-driven interface.

**Key Functions**:
- `menu()`: Main program loop and user interaction

### modules/menu_functions.py
Utility functions for menu operations.

**Functions**:
- `generate_input()`: Handle user input
- `generate_id()`: Create unique identifiers

### modules/menu_utils.py
Menu display and formatting utilities.

**Functions**:
- `clear()`: Clear screen
- `pause()`: Wait for user input
- `print_error()`: Format error messages
- `menu_options()`: Display menu options
- `menu_titles()`: Format menu titles

## Data Structures

### Memory Storage
The application uses in-memory data structures:
- `avaible_products`: List of Product objects
- `registred_clients`: Dictionary of Client objects (key: client_id)
- `orders_placed`: Dictionary of Order objects (key: order_id)

### ID Formats
- Products: 
  - Regular: "P" + number
  - Digital: "PD" + number
  - Physical: "PF" + number
- Clients: "C" + number
- Orders: "PED" + number

## Development Guidelines

### Coding Standards
- Follow PEP 8 style guide
- Use type hints for function parameters
- Document classes and methods using docstrings
- Implement proper encapsulation using private attributes

### Adding New Features
1. **New Product Types**:
   - Extend the Product base class
   - Implement required attributes and methods
   - Update menu system in main.py

2. **New Functionality**:
   - Add appropriate models in models/
   - Implement UI handling in modules/
   - Update main menu structure

### Error Handling
- Use try-except blocks for input validation
- Implement proper error messages
- Maintain type safety with explicit conversions

## Maintenance

### Common Tasks
1. **Adding Product Types**:
   - Create new class in models/
   - Inherit from Product base class
   - Update menu options in main.py

2. **Modifying Data Structures**:
   - Update relevant model classes
   - Adjust menu handling in main.py
   - Update documentation

3. **UI Modifications**:
   - Modify menu_utils.py for display changes
   - Update menu_functions.py for input handling

### Testing
- Test new features in isolation
- Verify inheritance hierarchy
- Validate input handling
- Check error scenarios

### Documentation
- Update docstrings for new code
- Maintain this technical manual
- Update user manual for UI changes
- Keep README.md current

