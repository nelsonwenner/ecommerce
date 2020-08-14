import React from 'react';

import { Route, Redirect } from 'react-router-dom';

const PrivateRoute = ({ component: Component, ...otherProps }) => {
  const isAuth = JSON.parse(localStorage.getItem('@Auth')).authorized;

  return (
    <Route 
      { ...otherProps }
      render={props => (
        isAuth
        ?
        <Component { ...props } />
        :
        <Redirect to={ otherProps.redirectTo ? otherProps.redirectTo : '/login' } />
      )}
    />
  )
}

export default PrivateRoute;