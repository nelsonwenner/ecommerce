import React from 'react';
import './styles.css';

import { useCart } from '../../../../../providers/CartProvider';

const Cart = () => {
  const { cart } = useCart();
  
  return (
    <div className="cart">
      <span className="icon-cart"></span>
      <span className="count-cart">{ cart.length }</span>
      <span className="name">Cart</span>
      <td className="total">$ { cart.reduce((acc, current) => acc + (current.price * current.quantity), 0) } ,00</td>
    </div>
  )
}

export default Cart;