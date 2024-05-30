
```markdown
# FastAPI Odoo Project

This project is a FastAPI application that integrates with Odoo via XML-RPC to manage partners and purchase orders.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [Partners Endpoints](#partners-endpoints)
  - [Purchase Orders Endpoints](#purchase-orders-endpoints)
- [Documentation](#documentation)
- [Author](#author)
```
## Installation

1. **Clone the repository:**
   ```sh
   git clone <repo_url>
   cd fastapi_odoo_project
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Project Structure

```
fastapi_odoo_project/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── partners.py
│   │   ├── purchases.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── odoo.py
│   ├── templates/
│   │   └── odoo_data.html
│   └── schemas/
│       ├── __init__.py
│       ├── partner.py
│       ├── purchase.py
│
├── .env
├── requirements.txt
└── README.md
```

## Configuration

The configuration for connecting to the Odoo server is set in `app/config.py`:

```python
import xmlrpc.client
from fastapi import HTTPException

class OdooConfig:
    url = 'http://127.0.0.1:8069'
    db = 'odoo_bmit'
    username = 'sakib@bmitodoo.com'
    password = 'admin'
    
    @classmethod
    def get_odoo_models(cls):
        common = xmlrpc.client.ServerProxy(f'{cls.url}/xmlrpc/2/common')
        uid = common.authenticate(cls.db, cls.username, cls.password, {})
        if not uid:
            raise HTTPException(status_code=500, detail="Unable to authenticate with Odoo")
        models = xmlrpc.client.ServerProxy(f'{cls.url}/xmlrpc/2/object')
        return models, uid

models, uid = OdooConfig.get_odoo_models()
```

Ensure you update these details with your actual Odoo server configuration.

## Running the Application

1. **Navigate to your project directory:**
   ```sh
   cd /media/sakib/ODOO/fastApi_Odoo
   ```

2. **Create and activate a virtual environment (if not already done):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the FastAPI application:**
   ```sh
   uvicorn app.main:app --reload
   ```

5. **Access the API documentation at `http://127.0.0.1:8000/docs`.**

## API Endpoints

### Partners Endpoints

- **GET `/partners/`**
  - Fetch all partners.
  - Response: JSON array of partners.

- **GET `/partners/{partner_id}`**
  - Fetch a partner by ID.
  - Response: JSON object of the partner.

- **POST `/partners/`**
  - Create a new partner.
  - Request body: JSON object containing `name`, `email`, `phone`.
  - Response: JSON object with a message and the new partner ID.

- **PUT `/partners/{partner_id}`**
  - Update an existing partner.
  - Request body: JSON object containing `name`, `email`, `phone`.
  - Response: JSON object with a message.

- **DELETE `/partners/{partner_id}`**
  - Delete a partner by ID.
  - Response: JSON object with a message.

### Purchase Orders Endpoints

- **GET `/purchases/`**
  - Fetch all purchase orders.
  - Response: JSON array of purchase orders.

- **GET `/purchases/{order_id}`**
  - Fetch a purchase order by ID.
  - Response: JSON object of the purchase order.

- **POST `/purchases/`**
  - Create a new purchase order.
  - Request body: JSON object containing `name`, `partner_id`, `amount_total`.
  - Response: JSON object with a message and the new order ID.

- **PUT `/purchases/{order_id}`**
  - Update an existing purchase order.
  - Request body: JSON object containing `name`, `partner_id`, `amount_total`.
  - Response: JSON object with a message.

- **DELETE `/purchases/{order_id}`**
  - Delete a purchase order by ID.
  - Response: JSON object with a message.

## Documentation

The API documentation is automatically generated and can be accessed at:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **OpenAPI JSON:** `http://127.0.0.1:8000/openapi.json`

## Author

- **Name:** Sakib Shahriyar
- **Email:** sakibshahriyar51@gmail.com
```

This `README.md` includes the author's name and email at the end, along with all the necessary information to set up, configure, and run your FastAPI project.
