from flask import Blueprint, request, jsonify, render_template, json, current_app as app
from models.models import db, Category, Product
import os
import time
from werkzeug.utils import secure_filename
category_bp = Blueprint("category", __name__)

#DEV: Route for showing all categories on main product page
@category_bp.route("/products")
def index():
    categories = Category.query.all()
    return render_template("product.html", categories=categories)


#DEV: Route for displaying category page with all its products
@category_bp.route("/category/<int:category_id>")
def category_page(category_id):
    category = Category.query.get_or_404(category_id)
    products = Product.query.filter_by(category_id=category_id).all()

    products_data = []
    for product in products:
        app.logger.info(f"Product ID: {product.id}, Specs: {product.specs}, Image URLs: {product.image_urls}")

        # Fix `specs` (Ensure it's valid JSON)
        if isinstance(product.specs, str):
            try:
                specs = json.loads(product.specs)
            except json.JSONDecodeError:
                app.logger.error(f"Error decoding specs for product {product.id}")
                specs = {}
        else:
            specs = product.specs or {}

        # Fix `image_urls` (Ensure it's a valid list)
        if isinstance(product.image_urls, str):
            try:
                images = json.loads(product.image_urls) if "[" in product.image_urls else product.image_urls.split(",")
            except json.JSONDecodeError:
                app.logger.error(f"Error decoding image_urls for product {product.id}")
                images = []
        else:
            images = product.image_urls or []

        products_data.append({
            "id": product.id,
            "name": product.name,
            "description": product.description or "",
            "price": float(product.price) if product.price else 0.0,
            "specs": specs,
            "images": images,
            "video_url": product.video_url or ""
        })

    return render_template(
        "category.html", 
        category=category,  # Pass the entire category object
        products=products_data
    )