import React from 'react';
import './styles.css';

import { useAuth } from '../../../providers/AuthProvider';
import Checkout from '../../../pages/Checkout';
import LoginModal from '../Login';

const Identification = () => {
  const { auth } = useAuth();

  return (
    <Checkout>
      <div className="identification-main"></div>
      <LoginModal 
        openModal={ !auth.authorized }
      />
    </Checkout>
  )
}

export default Identification;