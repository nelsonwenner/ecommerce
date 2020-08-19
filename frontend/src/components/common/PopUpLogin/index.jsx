import React from 'react';

import { useAuth } from '../../../providers/AuthProvider';
import LoginModal from '../Login';

const PopUpLogin = () => {
  const { auth } = useAuth();
  
  return (
    <LoginModal 
      openModal={ !auth.authorized }
      path={ '/' }
    />
  )
}

export default PopUpLogin;