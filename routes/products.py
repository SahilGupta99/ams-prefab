import json  # Import JSON to handle specs properly
import os
from flask import Blueprint, request, jsonify, current_app as app, render_template
from werkzeug.utils import secure_filename
from models.models import db, Product, Category

product_bp = Blueprint("product", __name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "mp4"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@product_bp.route("/product/<int:product_id>")
def product_page(product_id):
    product = Product.query.get_or_404(product_id)
    
    # Process product data same as category route
    if isinstance(product.specs, str):
        try:
            specs = json.loads(product.specs)
        except json.JSONDecodeError:
            app.logger.error(f"Error decoding specs for product {product.id}")
            specs = {}
    else:
        specs = product.specs or {}

    if isinstance(product.image_urls, str):
        try:
            images = json.loads(product.image_urls) if "[" in product.image_urls else product.image_urls.split(",")
        except json.JSONDecodeError:
            app.logger.error(f"Error decoding image_urls for product {product.id}")
            images = []
    else:
        images = product.image_urls or []

    # Get related products
    related_products = Product.query.filter(
        Product.category_id == product.category_id,
        Product.id != product.id
    ).limit(4).all()

    # Process related products same as main products
    related_products_data = []
    for related in related_products:
        related_products_data.append({
            "id": related.id,
            "name": related.name,
            "price": float(related.price) if related.price else 0.0,
            "images": related.image_urls.split(",") if isinstance(related.image_urls, str) else related.image_urls or []
        })

    return render_template(
        "product-detail.html",
        product={
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": float(product.price) if product.price else 0.0,
            "specs": specs,
            "images": images,
            "video_url": product.video_url,
            "category_id": product.category_id
        },
        related_products=related_products_data,
        category=product.category
    )

