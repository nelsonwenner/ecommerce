import React from 'react';
import './styles.css';

import { useCart } from '../../../providers/CartProvider';

const CartItem = () => {
  const { cart, removeProduct } = useCart();

  return (
    <div className="cart-wrapper">
      <div className="cart-table-header mt-30">
        <div className="product">Product</div>
        <div className="price">Price</div>
      </div>
      {cart.map((product, index) => (
        <div className="cart-item" key={ index }>
          <img src={ `${process.env.REACT_APP_ECOMMERCE_API_URL}${ product.image_url }` } alt="cart-item" />
          <div className="cart-detail">
            <p>{ product.title }</p>
            <p>$ { product.price }</p>
            <p onClick={ () => removeProduct(product) }>X</p>
          </div>
        </div>
      ))}
    </div>
  )
}

export default CartItem;