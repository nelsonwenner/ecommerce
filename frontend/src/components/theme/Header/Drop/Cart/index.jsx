import React from 'react';
import './styles.css';

const Cart = () => {
  return (
    <div className="cart">
      <span className="icon-cart"></span>
      <span className="count-cart">0</span>
      <span className="name">Cart</span>
      <td className="total">$ 0,00</td>
    </div>
  )
}

export default Cart;