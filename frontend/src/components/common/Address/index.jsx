import React, { useEffect, useState } from 'react';
import * as yup from 'yup';
import './styles.css';

import usePersistedState from '../../../hooks/usePersistedState';
import { useAuth } from '../../../providers/AuthProvider';
import { useHistory } from 'react-router-dom';
import Checkout from '../../../pages/Checkout';
import ApiAuth from '../../../services/ApiAuth';
import { useForm } from "react-hook-form";
import Select from './Select';
import Field from './Field';

const validationSchema = yup.object().shape({
  street: yup.string().label('Street').required().max(255),
  zipcode: yup.string().label('Zipcode').required().max(10),
  city: yup.string().label('City').required().max(10),
  suite: yup.string().label('Suite').required().max(25),
})

const Address = () => {
  const [statePersisted, setStatePersisted] = usePersistedState('address', null);
  const [selectedAddress, setSelectedAddress] = useState();
  const [address, setAddress] = useState([]);
  const history = useHistory();
  const { auth } = useAuth();

  const { register, handleSubmit, errors } = useForm({
    validationSchema: validationSchema,
  });

  useEffect(() => {
    ApiAuth(auth.token).get(`/address`)
    .then(({ data }) => {
      setAddress(data);
    });
  }, []);
  
  const handlerSelectAddress = (event) => {
    const currentAddresSelected = JSON.parse(event.target.value);
    setSelectedAddress(currentAddresSelected);
  }
  
  const onSubmit = async(data) => {
    
    if (selectedAddress) {
      setStatePersisted(selectedAddress.id);
      return history.push('/checkout/payment');
    }
    
    ApiAuth(auth.token).post('/address', 
    {customer: auth.id, ...data})
    .then(({ data }) => {
      setStatePersisted(data.id);
      history.push('/checkout/payment');
    });
  }
  
  return (
    <Checkout>
      <div className="address-main">
        <div className="container">
          <div className="register">
            <form onSubmit={ handleSubmit(onSubmit) } className="form-register">
              <h2>Register Address</h2>

              <Select 
                classs={ 'field-select' }
                address={ address }
                name={ 'select-address' }
                htmlFor={ 'select-address' }
                handlerSelectAddress={ handlerSelectAddress }
              />

              <div className="line-address"></div>

              <div className="field-group">
                <Field 
                  errors={ errors.street }
                  name={ 'street' }
                  placeholder={ 'Street' }
                  htmlFor={ 'street' }
                  label={ 'Street' }
                  register={ register }
                  selectedAddress={ selectedAddress }
                />
      
                <Field 
                  id={ 'zipecode' }
                  errors={ errors.zipcode }
                  name={ 'zipcode' }
                  placeholder={ 'Zipcode' }
                  htmlFor={ 'zipcode' }
                  label={ 'Zipcode' }
                  register={ register }
                  selectedAddress={ selectedAddress }
                />
              </div>

              <div className="field-group">
                <Field 
                  errors={ errors.city }
                  name={ 'city' }
                  placeholder={ 'City' }
                  htmlFor={ 'city' }
                  label={ 'City' }
                  register={ register }
                  selectedAddress={ selectedAddress }
                />

                <Field 
                  errors={ errors.suite }
                  name={ 'suite' }
                  placeholder={ 'Suite' }
                  htmlFor={ 'suite' }
                  label={ 'Suite' }
                  register={ register }
                  selectedAddress={ selectedAddress }
                />
              </div>

              <button type="submit" className="btn btn-primary btn-effect">Next</button>
            </form>
          </div>
        </div>
      </div>
    </Checkout>
  )
}

export default Address;