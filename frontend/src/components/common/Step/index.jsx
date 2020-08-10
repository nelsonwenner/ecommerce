import React,{ useEffect } from 'react';
import './styles.css';

import { useCart } from '../../../providers/CartProvider';
import { Link, useHistory } from 'react-router-dom';

const Step = () => {
  const history = useHistory();
  const { cart } = useCart();

  useEffect(() => {

    if (!cart.length) {
      history.push('/');
    }
    
  })

  return (
    <div className="step-main">
      <ul className="progress-bar">
        <li className={ `${cart.length ? 'active' : ''}` }>
          <span className="circle">
            <span className="icon-v"></span>
          </span>
          <Link to={ '/cart' }>
            <h4>My Cart</h4>
          </Link>
        </li>
        <li>
          <span className="circle">
            <span className="icon-v"></span>
          </span>
          
          <h4>Identification</h4>
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
  )
}

export default Step;