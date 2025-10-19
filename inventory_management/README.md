Inventory Management API

This is a Django + Django REST Framework (DRF) project that implements a backend API for managing inventory items. It supports user authentication, inventory CRUD operations, change tracking, and filtering/sorting of inventory items.

---

## Features

### Authentication & Permissions

- JWT authentication via `djangorestframework-simplejwt`.
- Users must be logged in to create, update, or delete inventory items.
- `IsOwnerOrReadOnly` permission ensures that only the owner of an item can modify it; read-only access is public.

### Inventory Management

- Create, Read, Update, Delete (CRUD) inventory items.
- Each inventory item includes:
  - `name`
  - `description`
  - `quantity`
  - `price`
  - `category`
  - `date_added`
  - `last_updated`
- Inventory changes are logged with:
  - Old and new quantity
  - User who made the change
  - Reason for change

### Filtering & Sorting

- Filter items by category, price range, or low stock threshold.
- Sort items by name, quantity, price, or date added.
- Pagination for large datasets.

---

## Getting Started

### Requirements

- Python 3.9+
- Django 4.2+
- Django REST Framework
- djangorestframework-simplejwt
- django-filter

### Installation

1. Clone the repository:

```bash
git clone <repo_url>
cd inventory_management
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
API Endpoints
User Authentication
Register a new user

swift
Copy code
POST /api/auth/register/
Body (JSON):

json
Copy code
{
  "username": "myuser",
  "email": "myuser@example.com",
  "password": "mypassword"
}
Obtain JWT token

swift
Copy code
POST /api/auth/token/
Body (JSON):

json
Copy code
{
  "username": "myuser",
  "password": "mypassword"
}
Returns access and refresh tokens.

Refresh JWT token

swift
Copy code
POST /api/auth/token/refresh/
Body (JSON):

json
Copy code
{
  "refresh": "<refresh_token>"
}
Inventory Items
List inventory items

bash
Copy code
GET /api/items/
Optional filters & ordering:

ruby
Copy code
?category=widgets&min_price=5&max_price=20&ordering=-quantity
Create an inventory item

bash
Copy code
POST /api/items/
Headers:

makefile
Copy code
Authorization: Bearer <access_token>
Body (JSON):

json
Copy code
{
  "name": "Blue Widget",
  "description": "Small widget",
  "quantity": 12,
  "price": 9.99,
  "category": "widgets"
}
Update an inventory item

bash
Copy code
PUT /api/items/{id}/
Delete an inventory item

bash
Copy code
DELETE /api/items/{id}/
Inventory Change History
View changes for an item

bash
Copy code
GET /api/changes/?item=<item_id>
Testing the API
You can test the API using Postman or curl:

Register a user or create via admin.

Obtain JWT token via /api/auth/token/.

Include Authorization: Bearer <access_token> in requests to protected endpoints.

Test CRUD operations on /api/items/.

Check inventory change history via /api/changes/.
```
