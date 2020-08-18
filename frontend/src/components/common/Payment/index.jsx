import React,{ useEffect, useState } from 'react';
import * as yup from 'yup';
import './styles.css';

import Checkout from '../../../pages/Checkout';
import SummaryDetail from './SummaryDetail';
import card from '../../../assets/card.png';
import slip from '../../../assets/slip.png';

import { useCart } from '../../../providers/CartProvider';
import { useAuth } from '../../../providers/AuthProvider';
import ApiAuth from '../../../services/ApiAuth';
import PaymentMethod from './PaymentMethod';
import { useForm } from "react-hook-form";

const validationSchema = yup.object().shape({
  card_number: yup.string().when('payment_method', {
    is: 'credit_card',
    then: yup.string().label('Number card').required(),
  }),
  card_cvv: yup.string().when('payment_method', {
    is: 'credit_card',
    then: yup.string().label('CVV').required(),
  }),
  card_name: yup.string().when('payment_method', {
    is: 'credit_card',
    then: yup.string().label('Card Holder').required(),
  }),
  card_expiration: yup.string().when('payment_method', {
    is: 'credit_card',
    then: yup.string().label('Expiration').required(),
  }),
});

const Payment = () => {
  const [paymentMethod, setPaymentMethod] = useState([]);
  const { getCartTotal, getProductQuantity } = useCart();
  const { auth } = useAuth();

  const { register, handleSubmit, errors, watch } = useForm({
    validationSchema: validationSchema,
  });

  useEffect(() => {
    ApiAuth(auth.token).get('/paymentmethods')
    .then(({ data }) => {
      setPaymentMethod(data.results);
    });
  }, []);

  const onSubmit = async(data) => {
    console.log(data)
  }

  return (
    <Checkout>
      <div className="container mt">
        <div className="row">
          <div className="column xlarge-8 large-12 medium-12 small-12" >
            <div className="payment-wrapper">
              <div className="payment-card">
                <h4>Payment Methods</h4>
                <form onSubmit={ handleSubmit(onSubmit) }>
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
                          className={'form-controll' + (errors.card_number ? ' is-invalid' : '') } 
                          type="text"
                          name="card_number"
                          placeholder="number"
                          ref={ register }
                        />
                        <div className="invalid-feedback">
                          { errors.card_number && errors.card_number.message }
                        </div>
                      </div>

                      <div className="field-payment">
                        <input
                          className={'form-controll' + (errors.card_cvv ? ' is-invalid' : '') } 
                          type="text"
                          name="card_cvv"
                          placeholder="cvv"
                        />
                        <div className="invalid-feedback">
                          { errors.card_cvv && errors.card_cvv.message }
                        </div>
                      </div>
                    </div>
                  
                    <div className="field-group-payment mt-15">
                      <div className="field-payment">
                        <input
                          className={'form-controll' + (errors.card_name ? ' is-invalid' : '') } 
                          type="text"
                          name="card_name"
                          placeholder="card holder"
                        />
                        <div className="invalid-feedback">
                          { errors.card_name && errors.card_name.message }
                        </div>
                      </div>

                      <div className="field-payment">
                        <input
                          className={'form-controll' + (errors.card_expiration ? ' is-invalid' : '') } 
                          type="text"
                          name="card_expiration"
                          placeholder="MM/AA"
                        />
                        <div className="invalid-feedback">
                          { errors.card_expiration && errors.card_expiration.message }
                        </div>
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
            <SummaryDetail 
              quantity={ getProductQuantity() }
              total={ getCartTotal() }
            />
          </div>
        </div>
      </div>
    </Checkout>
  )
}

export default Payment;