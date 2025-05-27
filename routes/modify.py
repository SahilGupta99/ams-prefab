from flask import Blueprint, request, jsonify, current_app, render_template
from models.models import db, Category, Product
import os, logging, time, json
from werkzeug.utils import secure_filename
from flask_login import login_required

modify_data_bp = Blueprint("modify", __name__)

def allowed_video_file(filename):
    ALLOWED_VIDEO_EXTENSIONS = {'mp4', 'mov', 'avi', 'mkv', 'webm'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_VIDEO_EXTENSIONS

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@modify_data_bp.route('/modify-data')
@login_required
def modify_data_page():
    categories = Category.query.all()
    products = Product.query.all()
    return render_template('/admin/modify-data.html', categories=categories, products=products)

# ----------------- Category Routes -----------------

@modify_data_bp.route('/get_categories')
@login_required
def get_categories():
    categories = Category.query.all()
    return jsonify([{
        'id': c.id,
        'name': c.name,
        'description': c.description,
        'image_url': c.image_url
    } for c in categories])

@modify_data_bp.route('/get_category/<int:category_id>')
@login_required
def get_category(category_id):
    category = Category.query.get_or_404(category_id)
    return jsonify({
        'id': category.id,
        'name': category.name,
        'description': category.description,
        'image_url': category.image_url
    })

@modify_data_bp.route('/update_category', methods=['POST'])
@login_required
def update_category():
    try:
        category_id = request.form.get('id')
        if not category_id:
            return jsonify({'message': 'Category ID is required'}), 400
            
        category = Category.query.get_or_404(category_id)
        category.name = request.form.get('name', category.name)
        category.description = request.form.get('description', category.description)

        if 'image' in request.files:
            image_file = request.files['image']
            if image_file.filename != '' and allowed_file(image_file.filename):
                filename = secure_filename(f"category_{int(time.time())}_{image_file.filename}")
                upload_folder = os.path.join(current_app.root_path, 'static', 'uploads', 'category-images')
                os.makedirs(upload_folder, exist_ok=True)
                filepath = os.path.join(upload_folder, filename)
                image_file.save(filepath)
                category.image_url = f"/static/uploads/category-images/{filename}"

        db.session.commit()
        return jsonify({'message': 'Category updated successfully'})
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error updating category: {str(e)}")
        return jsonify({'message': 'Failed to update category'}), 500

@modify_data_bp.route('/delete_category/<int:category_id>', methods=['DELETE'])
@login_required
def delete_category(category_id):
    try:
        category = Category.query.get_or_404(category_id)
        db.session.delete(category)
        db.session.commit()
        return jsonify({'message': 'Category deleted successfully'})
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error deleting category: {str(e)}")
        return jsonify({'message': 'Failed to delete category'}), 500

# ----------------- Product Routes -----------------

@modify_data_bp.route('/get_products')
@login_required
def get_products():
    category_id = request.args.get('category_id')
    query = Product.query.options(db.joinedload(Product.category))
    
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    products = query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'price': float(p.price) if p.price else 0.0,
        'category_id': p.category_id,
        'category_name': p.category.name if p.category else 'No Category',
        'images': p.image_urls.split(',') if p.image_urls else []
    } for p in products])

@modify_data_bp.route('/get_product/<int:product_id>')
@login_required
def get_product(product_id):
    product = Product.query.options(db.joinedload(Product.category)).get_or_404(product_id)
    specs = {}
    if product.specs:
        try:
            specs = json.loads(product.specs) if isinstance(product.specs, str) else product.specs
        except json.JSONDecodeError:
            current_app.logger.error(f"Failed to parse specs for product {product_id}")
    
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': float(product.price) if product.price else 0.0,
        'category_id': product.category_id,
        'images': product.image_urls.split(',') if product.image_urls else [],
        'videos': product.video_url.split(',') if product.video_url else [],
        'specs': specs
    })

@modify_data_bp.route('/update_product', methods=['POST'])
@login_required
def update_product():
    try:
        product_id = request.form.get('id')
        if not product_id:
            return jsonify({'message': 'Product ID is required'}), 400
            
        product = Product.query.get_or_404(product_id)
        product.name = request.form.get('name', product.name)
        product.description = request.form.get('description', product.description)
        product.price = request.form.get('price', product.price)
        product.category_id = request.form.get('category_id', product.category_id)
        
        specs = request.form.get('specs')
        if specs:
            try:
                parsed_specs = json.loads(specs)
                product.specs = json.dumps(parsed_specs)
            except json.JSONDecodeError as e:
                current_app.logger.error(f"Invalid specs JSON: {str(e)}")
                return jsonify({'message': 'Invalid specifications format'}), 400
        else:
            product.specs = None

        if 'images' in request.files:
            image_files = request.files.getlist('images')
            current_images = product.image_urls.split(',') if product.image_urls else []
            
            for image_file in image_files:
                if image_file.filename != '' and allowed_file(image_file.filename):
                    filename = secure_filename(f"product_{int(time.time())}_{image_file.filename}")
                    upload_folder = os.path.join(current_app.root_path, 'static', 'uploads', 'products')
                    os.makedirs(upload_folder, exist_ok=True)
                    filepath = os.path.join(upload_folder, filename)
                    image_file.save(filepath)
                    current_images.append(f"/static/uploads/products/{filename}")
            
            product.image_urls = ','.join(current_images)

        if 'videos' in request.files:
            video_files = request.files.getlist('videos')
            current_videos = product.video_url.split(',') if product.video_url else []
            
            for video_file in video_files:
                if video_file.filename != '' and allowed_video_file(video_file.filename):
                    filename = secure_filename(f"product_video_{int(time.time())}_{video_file.filename}")
                    upload_folder = os.path.join(current_app.root_path, 'static', 'uploads', 'videos')
                    os.makedirs(upload_folder, exist_ok=True)
                    filepath = os.path.join(upload_folder, filename)
                    video_file.save(filepath)
                    current_videos.append(f"/static/uploads/videos/{filename}")
            
            product.video_url = ','.join(current_videos)

        db.session.commit()
        return jsonify({'message': 'Product updated successfully', 'product_id': product.id})
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error updating product: {str(e)}")
        return jsonify({'message': 'Failed to update product'}), 500

@modify_data_bp.route('/remove_product_video/<int:product_id>', methods=['POST'])
@login_required
def remove_product_video(product_id):
    try:
        data = request.json
        if not data or 'video_url' not in data:
            return jsonify({'message': 'Video URL is required'}), 400

        product = Product.query.get_or_404(product_id)
        current_videos = product.video_url.split(',') if product.video_url else []
        updated_videos = [vid for vid in current_videos if vid != data['video_url']]
        product.video_url = ','.join(updated_videos)

        try:
            if data['video_url'].startswith('/static/uploads/videos/'):
                video_path = os.path.join(current_app.root_path, data['video_url'][1:])
                if os.path.exists(video_path):
                    os.remove(video_path)
        except Exception as e:
            current_app.logger.error(f"Error deleting video file: {str(e)}")
        
        db.session.commit()
        return jsonify({'message': 'Video removed successfully'})
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error removing product video: {str(e)}")
        return jsonify({'message': 'Failed to remove video'}), 500

@modify_data_bp.route('/delete_product/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'})
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error deleting product: {str(e)}")
        return jsonify({'message': 'Failed to delete product'}), 500

@modify_data_bp.route('/remove_product_image/<int:product_id>', methods=['POST'])
@login_required
def remove_product_image(product_id):
    try:
        data = request.json
        if not data or 'image_url' not in data:
            return jsonify({'message': 'Image URL is required'}), 400

        product = Product.query.get_or_404(product_id)
        current_images = product.image_urls.split(',') if product.image_urls else []
        updated_images = [img for img in current_images if img != data['image_url']]
        product.image_urls = ','.join(updated_images)

        try:
            if data['image_url'].startswith('/static/uploads/products/'):
                image_path = os.path.join(current_app.root_path, data['image_url'][1:])
                if os.path.exists(image_path):
                    os.remove(image_path)
        except Exception as e:
            current_app.logger.error(f"Error deleting image file: {str(e)}")

        db.session.commit()
        return jsonify({'message': 'Image removed successfully'})
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error removing product image: {str(e)}")
        return jsonify({'message': 'Failed to remove image'}), 500
