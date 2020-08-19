import React from 'react';
import './styles.css';

import { useAuth } from '../../../providers/AuthProvider';
import Checkout from '../../../pages/Checkout';
import LoginModal from '../Login';

const Identification = () => {
  const { isAuth } = useAuth();

  return (
    <Checkout>
      <div className="identification-main"></div>
      <LoginModal 
        openModal={ !isAuth() }
        path={ '/checkout/address' }
      />
    </Checkout>
  )
}

export default Identification;