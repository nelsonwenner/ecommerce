import React from 'react';
import './styles.css';

import { Link } from 'react-router-dom';

const Step = () => {
  return (
    <div className="step-main">
      <ul className="progress-bar">
        <li className="active">
          <span className="circle">
            <span className="icon-v"></span>
          </span>
          <h4>My Cart</h4>
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