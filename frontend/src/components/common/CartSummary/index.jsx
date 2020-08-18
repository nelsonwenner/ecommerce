import React from 'react';
import './styles.css';

import { useCart } from '../../../providers/CartProvider';
import { Link } from 'react-router-dom';

const CartSummary = () => {
  const { cart } = useCart();
  
  return (
    <div className="cart-summary">
      <div className="cart-summary-item">
        <h4 className="summary-title">Order Summary</h4>
        <div className="summary-wrapper">
          {cart.map((product, index) => (
            <div className="summary-items" key={ index }>
              <h4 className="summary-item-title">
                <p>
                  { product.title }
                  <span> x{ product.quantity }</span>
                </p>
              </h4>
              <span className="summary-item-price">
                $ { product.price },00
              </span>
            </div>
          ))}
        </div>
        <div className="summary-total">
          <div className="summary-wrapper">
            <span className="summary-total-title">Total</span>
            <span className="summary-total-value">
              $ { cart.reduce((acc, current) => acc + (current.price * current.quantity), 0) },00
            </span>
          </div>
          <p>in 12x installments</p>
        </div>
        <span className="summary-line"></span>
        
        <Link to={ '/checkout' }>
          <div className="btn btn-primary btn-effect">Checkout</div>
        </Link>
      </div>
    </div>
  )
}

export default CartSummary;