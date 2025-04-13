# Virtual Store User Manual

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Basic Operations](#basic-operations)
4. [Advanced Features](#advanced-features)
5. [Troubleshooting](#troubleshooting)
6. [FAQs](#faqs)

## Introduction
Welcome to the Virtual Store Management System! This application helps you manage a digital marketplace that handles both digital and physical products. Whether you're selling e-books or physical merchandise, this system provides all the tools you need to manage your inventory, customers, and orders.

## Getting Started

### System Requirements
- Python 3.12 or higher
- Terminal or Command Prompt
- Required Python packages (installed via requirements.txt)

### Installation
1. Install Python 3.12 or higher
2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### First Launch
Run the application using:
```bash
python src/main.py
```

## Basic Operations

### 1. Client Management
- **Adding a New Client**
  1. Select "Gestionar clientes" (1)
  2. Choose "Añadir un Cliente" (1)
  3. Enter required information:
     - Client name
     - Email
     - Shipping address

- **Viewing Client List**
  1. Select "Gestionar clientes" (1)
  2. Choose "Mostrar todos los clientes" (2)

### 2. Product Management
- **Adding Products**
  1. Select "Gestionar productos" (2)
  2. Choose product type:
     - Regular Product (1)
     - Digital Product (2)
     - Physical Product (3)
  3. Enter product details:
     - Name
     - Price
     - Stock quantity
     - Additional details based on product type:
       * Digital: Format and file size
       * Physical: Weight and dimensions

- **Updating Stock**
  1. Select "Gestionar productos" (2)
  2. Choose "Actualizar stock" (4)
  3. Enter product ID
  4. Enter new stock quantity

### 3. Order Management
- **Creating Orders**
  1. Select "Gestionar pedidos" (3)
  2. Choose "Añadir un Pedido" (1)
  3. Enter:
     - Client ID
     - Order date
     - Product IDs (comma-separated)

- **Calculating Order Total**
  1. Select "Gestionar pedidos" (3)
  2. Choose "Calcular total de un pedido" (2)
  3. Enter order ID

## Advanced Features

### Product Types and Specifications
1. **Regular Products**
   - Basic product information
   - Stock management

2. **Digital Products**
   - Format specification (e.g., PDF, MP3)
   - File size tracking

3. **Physical Products**
   - Weight tracking
   - Dimension specifications

### Review System
- Add product reviews
- View all reviews

## Troubleshooting

### Common Issues and Solutions

1. **Invalid ID Format**
   - Ensure IDs follow the correct format:
     * Products: P (regular), PD (digital), PF (physical)
     * Clients: C
     * Orders: PED

2. **Product Not Found**
   - Verify the product ID is correct
   - Check if the product exists in inventory

3. **Order Creation Fails**
   - Verify client ID exists
   - Ensure all product IDs are valid
   - Check product stock availability

## FAQs

**Q: How do I find a client's ID?**
A: Use the "Mostrar todos los clientes" option in the client management menu.

**Q: Can I modify a product's price?**
A: Yes, update the product information through the product management menu.

**Q: How do I check available stock?**
A: Use the "Mostrar todos los productos" option in the product management menu.

**Q: Can I cancel an order?**
A: Contact system administrator for order cancellation.

**Q: How are digital products delivered?**
A: Digital products are managed through the system and delivery methods can be customized based on requirements.

