import React from 'react';
import './styles.css';

import { useCart } from '../../../../../providers/CartProvider';
import { Link } from 'react-router-dom';

const Cart = () => {
  const { cart, getCartTotal } = useCart();
  
  return (
    <Link to='/cart' >
      <div className="cart">
        <span className="icon-cart"></span>
        <span className="count-cart">{ cart.length }</span>
        <span className="name">Cart</span>
        <p className="total">$ { getCartTotal() }</p>
      </div>
    </Link>
  )
}

export default Cart;