from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import db, Cart, Product, Order

checkout_bp = Blueprint('checkout', __name__)

@checkout_bp.route('/process', methods=['POST'])
@login_required
def checkout():
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    if not cart_items:
        return jsonify(message="Cart is empty"), 400
    
    total_amount = 0
    for item in cart_items:
        product = Product.query.get(item.product_id)
        total_amount += product.price * item.quantity
    
    order = Order(user_id=current_user.id, total_amount=total_amount)
    db.session.add(order)
    
    # Deduct stock and clear the cart
    for item in cart_items:
        product = Product.query.get(item.product_id)
        product.stock -= item.quantity
        db.session.delete(item)
    
    db.session.commit()
    return jsonify(message="Order placed successfully", order_id=order.id)

