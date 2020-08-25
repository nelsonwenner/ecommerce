import React, { useEffect } from 'react';
import './styles.css';

import { useAuth } from '../../../providers/AuthProvider';
import Checkout from '../../../pages/Checkout';
import { useHistory } from 'react-router-dom';
import WrapperAuth from '../WrapperAuth';

const Identification = () => {
  const history = useHistory();
  const { isAuth } = useAuth();

  useEffect(() => {

    if (isAuth()) {
      history.push('/checkout/address');
    }
    
  });

  return (
    <Checkout>
      <div className="identification-main"></div>
      <WrapperAuth 
        openModal={ !isAuth() }
        path={ '/checkout/address' }
      />
    </Checkout>
  )
}

export default Identification;