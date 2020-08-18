import React,{ useEffect, useState } from 'react';
import * as yup from 'yup';
import './styles.css';

import { useCart } from '../../../providers/CartProvider';
import { useAuth } from '../../../providers/AuthProvider';
import ApiAuth from '../../../services/ApiAuth';
import Checkout from '../../../pages/Checkout';
import SummaryDetail from './SummaryDetail';
import card from '../../../assets/card.png';
import slip from '../../../assets/slip.png';
import PaymentMethod from './PaymentMethod';
import { useForm } from "react-hook-form";
import Select from './Select';
import Field from './Field';

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
  installments: yup.number().when('payment_method', {
    is: 'credit_card',
    then: yup.number().label('Installments').required(),
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
                      <Field 
                        classs={ "field-payment" }
                        errors={ errors.card_number }
                        name={ "card_number" }
                        placeholder={ "number" }
                        ref={ register }
                      />

                      <Field
                        classs={ "field-payment" } 
                        errors={ errors.card_cvv }
                        name={ "card_cvv" }
                        placeholder={ "cvv" }
                        ref={ register }
                      />
                    </div>
                  
                    <div className="field-group-payment mt-15">
                      <Field
                        classs={ "field-payment" } 
                        errors={ errors.card_name }
                        name={ "card_name" }
                        placeholder={ "card holder" }
                        ref={ register }
                      />

                      <Field 
                        classs={ "field-payment" }
                        errors={ errors.card_expiration }
                        name={ "card_expiration" }
                        placeholder={ "MM/AA" }
                        ref={ register }
                      />
                    </div>

                    <Select 
                      classs={ "field-select mt-20" }
                      errors={ errors.installments }
                      name={ "select-installments" }
                      cartTotal={ getCartTotal() }
                      ref={ register }
                    />

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