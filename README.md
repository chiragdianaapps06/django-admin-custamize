# 🛠️ Django Admin Customization with Jazzmin

This project demonstrates a Django admin interface customized using the **[Jazzmin](https://github.com/farridav/django-jazzmin)** package. It includes:

- A custom user model with roles (`super_admin`, `brand_admin`, etc.)
- Model-level admin permissions
- Dynamic form filtering
- Foreign key filtering based on user role
- Inline model relationships (e.g., `ColorVariant` in `Product`)
- Jazzmin for enhanced UI

---

## 📁 Project Structure

```
adminproject/
├── adminapp/              # Main application with models, views, admin customization
│   ├── admin.py           # Customized Django admin interface
│   ├── models.py          # Models: User, Brand, Category, Product, etc.
│   └── ...
├── adminproject/          # Django project configuration
│   ├── settings.py        # Jazzmin config, apps, static files setup
│   ├── urls.py
│   └── ...
├── templates/
│   └── index.html         # Form or custom HTML pages
├── static/                # Static files (CSS, JS)
├── manage.py
└── README.md
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/chiragdianaapps06/django-admin-custamize.git
cd your-repo-name
```

### 2. Create a Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

Open your browser: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 🧩 Jazzmin Configuration

Jazzmin is added in `INSTALLED_APPS` before `django.contrib.admin`:

```python
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    ...
    'adminapp',
]
```

Optional configuration in `settings.py`:

```python
JAZZMIN_SETTINGS = {
    "site_title": "Admin Panel",
    "site_header": "Custom Admin",
    "site_brand": "MyBrand",
    "welcome_sign": "Welcome to the Admin Dashboard",
    "show_sidebar": True,
    "navigation_expanded": True,
    "user_avatar": None,
}
```

---

## 👤 User Roles and Permissions

- **Super Admin**: Full access to all models.
- **Brand Admin**: Can manage only their brand’s products.
- **Staff User**: Access granted via `is_staff` and method checks in admin classes.

---

## 📦 Models Overview

- **User** (Custom)
- **Brand**
- **Category**
- **Product**
- **ColorVariant**

---

## 🙌 Acknowledgements

- [Jazzmin](https://github.com/farridav/django-jazzmin)
- [Django](https://docs.djangoproject.com/en/5.2/)
