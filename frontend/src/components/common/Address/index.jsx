import React, { useEffect, useState } from 'react';
import './styles.css';

import usePersistedState from '../../../hooks/usePersistedState';
import { useAuth } from '../../../providers/AuthProvider';
import { useHistory } from 'react-router-dom';
import Checkout from '../../../pages/Checkout';
import ApiAuth from '../../../services/ApiAuth';

const Address = () => {
  const [statePersisted, setStatePersisted] = usePersistedState('address', null);
  const [selectedAddress, setSelectedAddress] = useState();
  const [address, setAddress] = useState([]);
  const history = useHistory();
  const { auth } = useAuth();

  const [formData, setFormData] = useState({
    street: '',
    suite: '',
    city: '',
    zipcode: '',
    error: null
  });
  
  useEffect(() => {
    ApiAuth(auth.token).get(`/address`)
    .then(({ data }) => {
      setAddress(data);
    })
  }, []);
  
  const handlerSelectAddress = (event) => {
    const currentAddresSelected = JSON.parse(event.target.value);
    setSelectedAddress(currentAddresSelected);
  }

  const handlerChange = (event) => {
    setFormData({...formData, [event.target.name]: event.target.value});
  }

  const handlerClicked = async (event) => {
    event.preventDefault();
    
    if (selectedAddress) {
      setStatePersisted(selectedAddress.id);
      //history.push('/checkout/payment');
    }
    
    const { street, suite, city, zipcode } = formData;

    if (!street | !suite | !city | !zipcode) {
      setFormData({error: 'Fill in all the fields'});
    } else {
      ApiAuth(auth.token).post('/address', 
      {customer: auth.id, street, suite, city, zipcode})
      .then(({ data }) => {
        setStatePersisted(data.id);
        //history.push('/checkout/payment');
      });
    }
  }
  
  return (
    <Checkout>
      <div className="address-main">
        <div className="container">
          <div className="register">
            <form className="form-register">
              <h2>Register Address</h2>

              <div className="field-select">
                <label htmlFor="select-address">Selected Address</label>
                
                <select 
                  name="select-address" 
                  onChange={ handlerSelectAddress }
                >
                  <option value="0">Select a Address Exists</option>
                  {address.map((addrr, index) => (
                    <option key={index} value={JSON.stringify(addrr)}>
                      { `Address #${index + 1} Zipcode: ${addrr.zipcode}` }
                    </option>
                  ))}
                </select>
              </div>
              
              <div className="line-address"></div>

              <div className="field-group">
                <div className="field">
                  <label htmlFor="street">Street</label>
                  <input 
                    type="text"
                    name="street"
                    placeholder={ selectedAddress ? selectedAddress.street : 'Street' }
                    id="street"
                    className={ selectedAddress ? 'disabled' : '' }
                    onChange={ handlerChange }
                  />
                </div>
                
                <div className="field" id="zipecode">
                  <label htmlFor="zipcode">Zipcode</label>
                  <input 
                    type="text"
                    name="zipcode"
                    placeholder={ selectedAddress ? selectedAddress.zipcode : 'Zipcode' }
                    className={ selectedAddress ? 'disabled' : '' }
                    onChange={ handlerChange }
                  />
                </div>
              </div>

              <div className="field-group">
                <div className="field">
                  <label htmlFor="city">City</label>
                  <input 
                    type="text"
                    name="city"
                    placeholder={ selectedAddress ? selectedAddress.city : 'City' }
                    className={ selectedAddress ? 'disabled' : '' }
                    onChange={ handlerChange }
                  />
                </div>

                <div className="field">
                  <label htmlFor="suite">Suite</label>
                  <input 
                    type="text"
                    name="suite"
                    placeholder={ selectedAddress ? selectedAddress.suite : 'Suite' }
                    className={ selectedAddress ? 'disabled' : '' }
                    onChange={ handlerChange }
                  />
                </div>
              </div>
              <div className="btn btn-primary" onClick={ handlerClicked }>Next</div>
            </form>
          </div>
        </div>
      </div>
    </Checkout>
  )
}

export default Address;