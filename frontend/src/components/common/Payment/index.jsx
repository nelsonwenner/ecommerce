import React,{ useEffect, useState } from 'react';
import './styles.css';

import Checkout from '../../../pages/Checkout';
import card from '../../../assets/card.png';
import slip from '../../../assets/slip.png';

import { useCart } from '../../../providers/CartProvider';
import { useAuth } from '../../../providers/AuthProvider';
import ApiAuth from '../../../services/ApiAuth';
import PaymentMethod from './PaymentMethod';
import { useForm } from "react-hook-form";

const Payment = () => {
  const [paymentMethod, setPaymentMethod] = useState([]);
  const { register, handleSubmit, errors, watch } = useForm({});
  const { cart, getCartTotal } = useCart();
  const { auth } = useAuth();
  
  useEffect(() => {
    ApiAuth(auth.token).get('/paymentmethods')
    .then(({ data }) => {
      setPaymentMethod(data.results);
    });
  }, []);

  return (
    <Checkout>
      <div className="container mt">
        <div className="row">
          <div className="column xlarge-8 large-12 medium-12 small-12" >
            <div className="payment-wrapper">
              <div className="payment-card">
                <h4>Payment Methods</h4>
                <form>
                  <div className="form-check-wrapper">
                    <PaymentMethod 
                      register={ register }
                      value={ "credit_card" }
                      img={ card }
                    />

                    <PaymentMethod 
                      register={ register }
                      value={ "bank_slip" }
                      img={ slip }
                    />
                  </div>

                  <fieldset hidden={ watch('payment_method') !== 'credit_card' }>
                    <div className="field-group-payment">
                      <div className="field-payment">
                        <input 
                          type="text"
                          name=""
                          placeholder="number"
                        />
                      </div>

                      <div className="field-payment">
                        <input 
                          type="text"
                          name="suite"
                          placeholder="cvv"
                        />
                      </div>
                    </div>
                  
                    <div className="field-group-payment mt-15">
                      <div className="field-payment">
                        <input 
                          type="text"
                          name=""
                          placeholder="card holder"
                        />
                      </div>

                      <div className="field-payment">
                        <input 
                          type="text"
                          name="suite"
                          placeholder="expiration"
                        />
                      </div>
                    </div>

                    <div className="field-select mt-20">
                      <select 
                        name="select-installments" 
                      >
                      <option value="0">Select Installments</option>
                      
                      {Array.from(Array(12).keys()).map(i => (
                        <option key={i} value={i+1}>{i+1} x {(getCartTotal()/(i+1)).toFixed(2)}</option>
                      ))}
                      </select>
                    </div>

                    <button type="submit" className="btn btn-primary btn-effect">Save</button>
                  </fieldset>

                  <fieldset hidden={ watch('payment_method') !== 'bank_slip' }>
                    <button type="submit" className="btn btn-primary btn-effect">pay with bank slip</button>
                  </fieldset>
                </form>
              </div>
            </div>
          </div>
          <div className="column xlarge-4 large-12 medium-12 small-12">
            <div className="payment-summary">

            </div>
          </div>
        </div>
      </div>
    </Checkout>
  )
}

export default Payment;