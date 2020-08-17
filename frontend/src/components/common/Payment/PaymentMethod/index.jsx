import React from 'react';

const PaymentMethod = ({ register, img, value }) => {
  return (
    <div className="form-check">
      <input className="form-check-input"
        type="radio"
        name="payment_method"
        value={ value }
        ref={ register }
      />
      <label className="form-check-label" htmlFor="card">
        <img src={ img } alt="card" className="img-fluid"/>
      </label>  
    </div>
  )
}

export default PaymentMethod;