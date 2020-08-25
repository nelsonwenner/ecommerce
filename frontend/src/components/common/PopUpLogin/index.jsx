import React from 'react';

import { useAuth } from '../../../providers/AuthProvider';
import WrapperAuth from '../WrapperAuth';

const PopUpLogin = () => {
  const { isAuth } = useAuth();
  
  return (
    <WrapperAuth 
      openModal={ !isAuth() }
      path={ '/' }
    />
  )
}

export default PopUpLogin;