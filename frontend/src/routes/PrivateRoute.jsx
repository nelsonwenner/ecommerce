import React from 'react';

import { Route, Redirect } from 'react-router-dom';
import { useAuth } from '../providers/AuthProvider';

const PrivateRoute = ({ component: Component, ...otherProps }) => {
  const [auth] = useAuth();

  return (
    <Route 
      { ...otherProps }
      render={props => (
        auth.authorized 
        ?
        <Component { ...props } />
        :
        <Redirect to={ otherProps.redirectTo ? otherProps.redirectTo : '/' } />
      )}
    />
  )
}

export default PrivateRoute;