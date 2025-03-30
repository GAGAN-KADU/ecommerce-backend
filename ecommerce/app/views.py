from flask import Blueprint, jsonify
from app.models import Product

views_bp = Blueprint('views', __name__)

@views_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products])

