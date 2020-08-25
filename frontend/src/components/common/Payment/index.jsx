import React,{ useEffect, useState } from 'react';
import * as yup from 'yup';
import './styles.css';

import usePersistedState from '../../../hooks/usePersistedState';
import { useCart } from '../../../providers/CartProvider';
import { useAuth } from '../../../providers/AuthProvider';
import ApiAuth from '../../../services/ApiAuth';
import Checkout from '../../../pages/Checkout';
import { useHistory } from 'react-router-dom';
import SummaryDetail from './SummaryDetail';
import card from '../../../assets/card.png';
import slip from '../../../assets/slip.png';
import PaymentMethod from './PaymentMethod';
import { useForm } from "react-hook-form";
import Select from './Select';
import pagarme from 'pagarme';
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
  installments: yup.string().when('payment_method', {
    is: 'credit_card',
    then: yup.string().label('Installments').required(),
  }),
});

const Payment = () => {
  const [checkout, setStatePersistedCheckout] = usePersistedState('checkout_status', false);
  const [addressId, setStatePersisted] = usePersistedState('address', null);
  const [paymentGateway, setPaymentGateway] = useState([]);
  const [paymentMethod, setPaymentMethod] = useState([]);
  const { cart, getCartTotal, getProductQuantity } = useCart();
  const { auth, getUserId } = useAuth();
  const history = useHistory();

  const { register, handleSubmit, errors, watch } = useForm({
    validationSchema: validationSchema,
  });
  
  useEffect(() => {
    ApiAuth(auth.token).get('/paymentmethods')
    .then(({ data }) => {
      setPaymentMethod(data.results);
    });
  }, []);

  useEffect(() => {
    ApiAuth(auth.token).get('/paymentgateways')
    .then(({ data }) => {
      setPaymentGateway(data.results);
    });
  }, []);
 
  const onSubmit = async(data) => {

    const methodPayment = paymentMethod.find(item => item.name === data.payment_method);

    const sendData = {
      customer: getUserId(),
      payment_method: methodPayment.id,
      address: addressId,
      installments: parseInt(data.installments) || 0,
      status: "e1182812-d1b0-4585-99bf-6510497602ab",
      items: cart.map(item => ({
        product: item.product,
        quantity: item.quantity,
        price: item.price
      }))
    }
    
    if (data.payment_method === 'credit_card') {
      const card = {
        card_number: data.card_number,
        card_holder_name: data.card_name,
        card_expiration_date: data.card_expiration.split('/').join(''),
        card_cvv: data.card_cvv,
      }
      const gatewayPayment = paymentGateway.find(gateway => gateway.resourcetype === 'PagarmeGateway');
      const client = await pagarme.client.connect({encryption_key: gatewayPayment.encryption_key});
      sendData['card_hash'] = await client.security.encrypt(card);
    }

    ApiAuth(auth.token).post('/checkouts', sendData)
    .then((res) => {
      setStatePersistedCheckout(true);
      history.push('/checkout/success');
    });
  }

  return (
    <Checkout>
      <div className="payment-main">
        <div className="container">
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
                          register={ register }
                        />

                        <Field
                          classs={ "field-payment" } 
                          errors={ errors.card_cvv }
                          name={ "card_cvv" }
                          placeholder={ "cvv" }
                          register={ register }
                        />
                      </div>
                    
                      <div className="field-group-payment mt-15">
                        <Field
                          classs={ "field-payment" } 
                          errors={ errors.card_name }
                          name={ "card_name" }
                          placeholder={ "card holder" }
                          register={ register }
                        />

                        <Field 
                          classs={ "field-payment" }
                          errors={ errors.card_expiration }
                          name={ "card_expiration" }
                          placeholder={ "MM/AA" }
                          register={ register }
                        />
                      </div>

                      <Select 
                        classs={ "field-select mt-20" }
                        errors={ errors.installments }
                        name={ "installments" }
                        cartTotal={ getCartTotal() }
                        register={ register }
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
      </div>
    </Checkout>
  )
}

export default Payment;