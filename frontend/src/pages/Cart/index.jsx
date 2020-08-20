import React, { useEffect } from 'react';
import './styles.css';

import CartSummary from '../../components/common/CartSummary';
import CartItem from '../../components/common/CartItem';
import { useCart } from '../../providers/CartProvider';
import Layout from '../../components/common/Layout';
import { useHistory } from 'react-router-dom';

const Cart = () => {
  const history = useHistory();
  const { cart } = useCart();

  useEffect(() => {

    if (!cart.length) {
      history.push('/');
    }

  });

  return (
    <Layout>
      <div className="cart-main">
        <div className="container cart-main">
          <h4 className="path-page">Home / Cart</h4>
          <h4 className="cart-title">Cart</h4>
          <div className="row">
            <div className="column xlarge-8 large-12 medium-12 small-12" >
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