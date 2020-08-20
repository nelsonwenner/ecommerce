import React from 'react';

import { useAuth } from '../../../providers/AuthProvider';
import LoginModal from '../Login';

const PopUpLogin = () => {
  const { isAuth } = useAuth();
  
  return (
    <LoginModal 
      openModal={ !isAuth() }
      path={ '/' }
    />
  )
}

export default PopUpLogin;