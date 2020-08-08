import React from 'react';
import './styles.css';

import { useCart } from '../../../../../providers/CartProvider';
import { Link } from 'react-router-dom';

const Cart = () => {
  const { cart } = useCart();
  
  return (
    <Link to='/cart' >
      <div className="cart">
        <span className="icon-cart"></span>
        <span className="count-cart">{ cart.length }</span>
        <span className="name">Cart</span>
        <td className="total">$ { cart.reduce((acc, current) => acc + (current.price * current.quantity), 0) } ,00</td>
      </div>
    </Link>
  )
}

export default Cart;