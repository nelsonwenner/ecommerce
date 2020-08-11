import React, { useState } from 'react';
import './styles.css';

import Checkout from '../../../pages/Checkout';
import LoginModal from '../Login';

const Identification = () => {
  const [modalLogin, setModalLogin] = useState(true); //State login isAuth
  
  return (
    <Checkout>
      <div className="identification-main"></div>
      <LoginModal 
        openModal={ modalLogin }
      />
    </Checkout>
  )
}

export default Identification;