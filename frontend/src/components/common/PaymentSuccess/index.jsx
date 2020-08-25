import React, { useEffect, useState } from 'react';
import './styles.css';

import usePersistedState from '../../../hooks/usePersistedState';
import { useCart } from '../../../providers/CartProvider';
import redirect from '../../../routes/redirect';
import Checkout from '../../../pages/Checkout';
import { useHistory } from 'react-router-dom';

const PaymentSuccess = () => {
  const [checkoutState, setStatePersistedCheckout] = usePersistedState('checkout_status', null);
  const [address, setStatePersistedAddress] = usePersistedState('address', null);
  const [resumeCart, setResumeCart] = useState([]);
  const { cart, cleanCart } = useCart();
  const history = useHistory();

  useEffect(() => {
    
    if (!JSON.parse(localStorage.getItem('checkout_status'))) {
      history.push('/');
    }

    if (checkoutState) {
      setResumeCart(cart);
      localStorage.removeItem('checkout_status');
      setStatePersistedAddress(null);
      cleanCart();
    }

  }, []);
  
  useEffect(() => {
    setTimeout(() => {
      redirect('/');
    }, 3000);
  }, []);

  return (
    <Checkout>
      <div className="payment-success-main">
        <div className="container">
          <h4 className="title-checkout-success">Purchase completed successfully</h4>
          <div className="order-summary-wrapper">
            {resumeCart.map((product, index) => (
              <div className="card-resume" key={ index }>
                <img src={ `${process.env.REACT_APP_ECOMMERCE_API_URL}${ product.image_url }` } alt="cart-item" />
                <div className="card-details">
                  <p>{ product.title }</p>
                  <p>x{ product.quantity }</p>
                  <p>${ product.price }</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </Checkout>
  )
}

export default PaymentSuccess;