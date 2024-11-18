# main.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from inventory_management_system.auth.login import AuthSystem
from inventory_management_system.auth.roles import is_admin
from inventory_management_system.product.product import Product
from inventory_management_system.product.product_operations import ProductOperations
from inventory_management_system.inventory.inventory_manager import InventoryManager

# Initialize systems
auth_system = AuthSystem()
product_ops = ProductOperations()
inventory_manager = InventoryManager(product_ops)

# Login
st.title("Inventory Management System")
st.sidebar.header("Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Login"):
    try:
        user = auth_system.login(username, password)
        st.sidebar.success(f"Logged in as {user.role}")
    except ValueError as e:
        st.sidebar.error(str(e))

# Admin functionalities
if 'user' in locals() and is_admin(user):
    st.header("Admin Panel")
    st.subheader("Add Product")
    with st.form("add_product"):
        product_id = st.text_input("Product ID")
        name = st.text_input("Name")
        category = st.text_input("Category")
        price = st.number_input("Price", min_value=0.0)
        stock_quantity = st.number_input("Stock Quantity", min_value=0)
        submit = st.form_submit_button("Add Product")

        if submit:
            product = Product(product_id, name, category, price, stock_quantity)
            try:
                product_ops.add_product(product)
                st.success("Product added successfully")
            except ValueError as e:
                st.error(str(e))

    st.subheader("View Products")
    products = product_ops.view_products()
    for product in products:
        st.write(f"ID: {product.product_id}, Name: {product.name}, Stock: {product.stock_quantity}")

# User functionalities
if 'user' in locals() and not is_admin(user):
    st.header("User Panel")
    st.subheader("View Products")
    products = product_ops.view_products()
    for product in products:
        st.write(f"ID: {product.product_id}, Name: {product.name}, Stock: {product.stock_quantity}")
