# 🛒 Smart Commerce – Python + SQL E-Commerce Project  

E-commerce management system built with **Python** and **MySQL** – includes user authentication, admin panel, product inventory, order processing, and review system.  

---

## ✨ Features
- 👥 **User Management** – registration, login, password reset  
- 🛍️ **Product Management** – add, update, delete, view products  
- 🛒 **Shopping Cart** – add/remove items, generate bill  
- 📦 **Order Management** – checkout, update, view orders  
- ⭐ **Reviews System** – add, update, delete, view reviews  
- 📝 **Grievances Handling** – submit, update, delete, reply to complaints  
- 🔑 **Admin Panel** – manage users, products, orders, and grievances  

---

## 🛠️ Tech Stack
- **Python 3.9**  
- **MySQL 8.0**  
- **mysql-connector-python** (for database connectivity)  

---

## 🚀 Setup & Installation
1. Install Python (>=3.8) and MySQL on your system.  
2. Clone this repository:  
   ```bash
   git clone https://github.com/umikasood27/Smart-Commerce.git
   cd Smart-Commerce
## Install dependencies:

pip install mysql-connector-python

## Create the database in MySQL:

CREATE DATABASE ECOMMERCE;
USE ECOMMERCE;

## Update database credentials in ecommerce.py:
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="yourpassword"   # 🔒 replace with your MySQL password

## Run the program:
python ecommerce.py


## 📂 Project Structure
```
Smart-Commerce/
│
├── ecommerce.py          # main Python code
├── README.md             # project documentation
└── E-Commerce_UmikaSood.pdf   # detailed project report
```

## 📖 Documentation
For full details, flow diagrams, and output screenshots, see the full report:
📄 E-Commerce_UmikaSood.pdf

## 🙌 Credits
This project was originally developed as part of my Class XII Computer Science Investigatory Project (2024–25) at Delhi Public School, R.K. Puram.
👩‍💻 Developed by: Umika Sood

## 🚧 Future Improvements
🌐 Web-based front-end with Flask/Django
🔒 Enhanced security with hashed passwords
💳 Integration with payment gateway APIs
🤖 Recommendation system for products
