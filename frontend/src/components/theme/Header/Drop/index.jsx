import React from 'react';
import './styles.css';

const Drop = () => {
  return (
    <div className="drop-main">
      <div className="container">
        <div className="drop-wrapper">
          <div className="info-category">
            <span className="icon-hamburger" />
            <p>All Categories</p>
          </div>
          <div className="cart">
            <span className="icon-cart"></span>
            <span className="count-cart">0</span>
            <span className="name">Cart</span>
            <td className="total">$ 0,00</td>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Drop;