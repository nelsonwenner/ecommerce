import React, { useEffect, useState } from 'react';
import './styles.css';

import { useAuth } from '../../../providers/AuthProvider';
import Checkout from '../../../pages/Checkout';
import ApiAuth from '../../../services/ApiAuth';

const Address = () => {
  const [selectedAddress, setSelectedAddress] = useState();
  const [address, setAddress] = useState([]);
  const { auth } = useAuth();
  
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
                  />
                </div>
                
                <div className="field" id="zipecode">
                  <label htmlFor="zipcode">Zipcode</label>
                  <input 
                    type="text"
                    name="zipecode"
                    placeholder={ selectedAddress ? selectedAddress.zipcode : 'Zipcode' }
                    className={ selectedAddress ? 'disabled' : '' }
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
                  />
                </div>

                <div className="field">
                  <label htmlFor="suite">Suite</label>
                  <input 
                    type="text"
                    name="suite"
                    placeholder={ selectedAddress ? selectedAddress.suite : 'Suite' }
                    className={ selectedAddress ? 'disabled' : '' }
                  />
                </div>
              </div>
              <div className="btn btn-primary">Next</div>
            </form>
          </div>
        </div>
      </div>
    </Checkout>
  )
}

export default Address;