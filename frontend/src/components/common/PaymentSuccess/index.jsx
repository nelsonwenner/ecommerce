import React, { useEffect, useState } from 'react';
import './styles.css';

import usePersistedState from '../../../hooks/usePersistedState';
import { useCart } from '../../../providers/CartProvider';
import Checkout from '../../../pages/Checkout';

const PaymentSuccess = () => {
  const [checkoutState, setStatePersistedCheckout] = usePersistedState('checkout_status', null);
  const [resumeCart, setResumeCart] = useState([]);
  const { cart, cleanCart } = useCart();

  useEffect(() => {
    
    if (checkoutState) {
      setResumeCart(cart);
      setStatePersistedCheckout(false);
      cleanCart();
    }

  }, []);

  return (
    <Checkout>
      <div className="container">
        <h4 className="title-checkout-success">Purchase completed successfully</h4>
        <div className="order-summary-wrapper">
          {resumeCart.map((product, index) => (
            <div className="card-resume" key={ index }>
              <div className="card-img">
                <img src={ `${process.env.REACT_APP_ECOMMERCE_API_URL}${ product.image_url }` } alt="cart-item" />
              </div>
              <div className="card-details">
                <p>{ product.title }</p>
                <p>x{ product.quantity }</p>
                <p>${ product.price }</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </Checkout>
  )
}

export default PaymentSuccess;