import React from 'react';

import { Route, Redirect } from 'react-router-dom';
import { useAuth } from '../providers/AuthProvider';

const PrivateRoute = ({ component: Component, ...otherProps }) => {
  const { isAuth } = useAuth();

  return (
    <Route 
      { ...otherProps }
      render={props => (
        isAuth()
        ?
        <Component { ...props } />
        :
        <Redirect to={ otherProps.redirectTo ? otherProps.redirectTo : '/login' } />
      )}
    />
  )
}

export default PrivateRoute;