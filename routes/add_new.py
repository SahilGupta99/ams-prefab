from flask import Blueprint, request, jsonify, current_app as app
from models.models import db, Category, Product
from werkzeug.utils import secure_filename
import os
import time, json
from flask_login import login_required

add_new_bp = Blueprint("add_new", __name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "mp4"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for adding a new category
@add_new_bp.route("/add_category", methods=["POST"])
@login_required
def add_category():
    try:
        if 'image' not in request.files:
            return jsonify({"message": "No image file provided"}), 400
            
        image_file = request.files['image']
        
        if image_file.filename == '':
            return jsonify({"message": "No selected image file"}), 400

        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
        if not allowed_file(image_file.filename):
            return jsonify({"message": "Invalid image file type"}), 400

        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()

        if not name:
            return jsonify({"message": "Category name is required!"}), 400

        if Category.query.filter_by(name=name).first():
            return jsonify({"message": "Category already exists!"}), 400

        # Save image in uploads/category-images
        filename = secure_filename(f"category_{int(time.time())}_{image_file.filename}")
        upload_folder = os.path.join(app.root_path, 'static', 'uploads', 'category-images')
        os.makedirs(upload_folder, exist_ok=True)
        filepath = os.path.join(upload_folder, filename)
        image_file.save(filepath)

        image_url = f"/static/uploads/category-images/{filename}"

        new_category = Category(
            name=name,
            description=description,
            image_url=image_url
        )
        db.session.add(new_category)
        db.session.commit()

        return jsonify({
            "message": "Category added successfully!",
            "category": {
                "id": new_category.id,
                "name": new_category.name
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Error adding category: {str(e)}")
        return jsonify({"message": "An error occurred while adding the category"}), 500

# Route for adding a new product
@add_new_bp.route("/add_product", methods=["POST"])
@login_required
def add_product():
    try:
        category_id = request.form.get("category_id")
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")
        specs = request.form.get("specs")

        if not category_id or not name or not description or not price or not specs:
            return jsonify({"message": "All fields are required! Missing data."}), 400

        category = Category.query.get(category_id)
        if not category:
            return jsonify({"message": "Invalid category selected!"}), 400

        try:
            specs = json.loads(specs) if specs else {}
        except json.JSONDecodeError:
            return jsonify({"message": "Invalid JSON format for specs!"}), 400

        try:
            price = float(price)
            if price <= 0:
                return jsonify({"message": "Price must be greater than 0!"}), 400
        except ValueError:
            return jsonify({"message": "Invalid price value!"}), 400

        # Handle Image Uploads (uploads/products)
        image_urls = []
        if "images" in request.files:
            images = request.files.getlist("images")
            upload_folder = os.path.join(app.root_path, 'static', 'uploads', 'products')
            os.makedirs(upload_folder, exist_ok=True)

            for image in images:
                if image and allowed_file(image.filename):
                    filename = secure_filename(f"product_{int(time.time())}_{image.filename}")
                    filepath = os.path.join(upload_folder, filename)
                    image.save(filepath)
                    image_urls.append(f"/static/uploads/products/{filename}")

        # Handle Video Upload (uploads/videos)
        video_url = ""
        if "video" in request.files:
            video = request.files["video"]
            if video and allowed_file(video.filename):
                upload_folder = os.path.join(app.root_path, 'static', 'uploads', 'videos')
                os.makedirs(upload_folder, exist_ok=True)

                filename = secure_filename(f"video_{int(time.time())}_{video.filename}")
                filepath = os.path.join(upload_folder, filename)
                video.save(filepath)
                video_url = f"/static/uploads/videos/{filename}"

        image_urls_str = ",".join(image_urls) if image_urls else ""

        new_product = Product(
            category_id=category_id,
            name=name,
            description=description,
            price=price,
            specs=specs,
            image_urls=image_urls_str,
            video_url=video_url
        )

        db.session.add(new_product)
        db.session.commit()

        return jsonify({
            "message": "Product added successfully!",
            "product": {
                "id": new_product.id,
                "category_id": new_product.category_id,
                "name": new_product.name,
                "description": new_product.description,
                "price": new_product.price,
                "specs": new_product.specs,
                "image_urls": new_product.image_urls.split(",") if new_product.image_urls else [],
                "video_url": new_product.video_url
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
