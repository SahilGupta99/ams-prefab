from flask import Blueprint, render_template, redirect, request, url_for, flash, logging
from flask_login import login_user, logout_user, login_required, current_user
from models.models import db, Category, Product, AdminUser

admin_bp = Blueprint("admin", __name__)
# Configure the logging

@admin_bp.route("/admin")
@login_required
def admin_panel():
    categories = Category.query.all()
    products = Product.query.all()
    return render_template("/admin/admin.html", categories=categories, products=products)


# Admin Login
@admin_bp.route('/admin/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Query the AdminUser table to check if the user exists
        admin_user = AdminUser.query.filter_by(username=username).first()
        
        # Check if the user exists and the password matches
        if admin_user and admin_user.password == password:
            login_user(admin_user)  # Login the user
            return redirect(url_for('admin.dashboard'))  # Redirect to the dashboard

        else:
            flash('Invalid credentials', 'error')
            
    return render_template('admin/login.html')

# Admin Dashboard
@admin_bp.route('/admin/dashboard')
@login_required
def dashboard():
    return render_template('admin/dashboard.html')

# Admin Logout
@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))