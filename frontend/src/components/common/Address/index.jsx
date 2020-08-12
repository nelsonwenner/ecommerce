import React from 'react';
import './styles.css';

import Checkout from '../../../pages/Checkout';

const Address = () => {
  return (
    <Checkout>
      <div className="address-main">
        <div className="container">
          <div className="register">
            <form className="form-register">
              <h2>Register Address</h2>
              <div className="field-group">
                <div className="field">
                  <label htmlFor="street">Street</label>
                  <input 
                    type="text"
                    name="street"
                    placeholder="Street"
                    id="street"
                  />
                </div>

                <div className="field" id="zipecode">
                  <label htmlFor="zipecode">Zipecode</label>
                  <input 
                    type="text"
                    name="zipecode"
                    placeholder="Zipecode"
                  />
                </div>
              </div>

              <div className="field-group">
                <div className="field">
                  <label htmlFor="city">City</label>
                  <input 
                    type="text"
                    name="city"
                    placeholder="City"
                  />
                </div>

                <div className="field">
                  <label htmlFor="suite">Suite</label>
                  <input 
                    type="text"
                    name="suite"
                    placeholder="Suite"
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