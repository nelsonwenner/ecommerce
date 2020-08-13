import React,{ useEffect, } from 'react';
import './styles.css';

import { useAuth } from '../../../providers/AuthProvider';
import { useCart } from '../../../providers/CartProvider';
import { Link, useHistory } from 'react-router-dom';

const Step = () => {
  const history = useHistory();
  const { auth } = useAuth();
  const { cart } = useCart();

  useEffect(() => {

    if (!cart.length) {
      history.push('/');
    }
    
    if (auth.authorized) {
      history.push('/checkout/address');
    }

  }, [auth]);
  
  return (
    <div className="step-main">
      <div className="container">
        <ul className="progress-bar">
          <li className={ `${cart.length ? 'active' : ''}` }>
            <span className="circle">
              <span className="icon-v"></span>
            </span>
            <Link to={ '/cart' }>
              <h4>My Cart</h4>
            </Link>
          </li>
          <li className={ `${auth.authorized ? 'active' : ''}` }>
            <span className="circle">
              <span className="icon-v"></span>
            </span>
            
            <h4>Identification</h4>
          </li>
          <li className={ `${ JSON.parse(localStorage.getItem('address')) ? 'active' : ''}` }>
            <span className="circle">
              <span className="icon-v"></span>
            </span>
            <h4>Address</h4>
          </li>
          <li>
            <span className="circle">
              <span className="icon-v"></span>
            </span>
            <h4>Payment</h4>
          </li>
          <li>
            <span className="circle">
              <span className="icon-v"></span>
            </span>
            <h4>Thank You</h4>
          </li>
        </ul>
      </div>
    </div>
  )
}

export default Step;