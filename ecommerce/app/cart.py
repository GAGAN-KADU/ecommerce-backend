from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import db, Cart, Product

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/add', methods=['POST'])
@login_required
def add_to_cart():
    data = request.get_json()
    product_id = data['product_id']
    quantity = data['quantity']
    
    product = Product.query.get(product_id)
    if not product or product.stock < quantity:
        return jsonify(message="Product not available"), 400

    cart_item = Cart.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = Cart(user_id=current_user.id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)
    
    db.session.commit()
    return jsonify(message="Product added to cart")

@cart_bp.route('/remove', methods=['POST'])
@login_required
def remove_from_cart():
    data = request.get_json()
    product_id = data['product_id']
    
    cart_item = Cart.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify(message="Product removed from cart")
    return jsonify(message="Product not found in cart"), 404

