import React from 'react';
import './styles.css';

import CartSummary from '../../components/common/CartSummary';
import CartItem from '../../components/common/CartItem';
import Layout from '../../components/common/Layout';

const Cart = () => {
  return (
    <Layout>
      <div className="cart-main">
        <div className="container cart-main">
          <h4 className="path-page">Home / Cart</h4>
          <h4 className="cart-title">Cart</h4>
          <div className="row">
            <div className="column xlarge-8 large-12 medium-12 small-12" >
              <div className="cart-table-header mt-30">
                <div className="product">Product</div>
                <div className="price">Price</div>
              </div>
              <CartItem />
            </div>
            <div className="column xlarge-4 large-12 medium-12 small-12">
              <CartSummary />
            </div>
          </div>
        </div>
      </div>
    </Layout>
  )
}

export default Cart;