import React from 'react';
import './styles.css';

const SummaryDetail = ({ quantity, total }) => {
  return (
    <div className="payment-summary">
      <div className="payment-detail">
        <h4>Detail Payment</h4>
        
        <div className="list-info">
          <p>{ quantity } products</p>
          <p>$ { total } </p>
        </div>
        
        <div className="list-info-total">
          <div className="list-total-wrapper">
            <p>Total</p>
            <p>$ { total } </p>
          </div>
          <span>in 12x without interest</span>
        </div>
      </div>
    </div>
  )
}

export default SummaryDetail;