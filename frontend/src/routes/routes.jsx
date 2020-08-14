import React from "react";
import { Route, BrowserRouter, Switch } from "react-router-dom";

import Identification from '../components/common/Identification';
import PopUpLogin from '../components/common/PopUpLogin';
import { AuthProvider } from '../providers/AuthProvider';
import Address from '../components/common/Address';
import PrivateRoute from './PrivateRoute';
import Cart from '../pages/Cart';
import Home from "../pages/Home";

const Routes = () => {
  return (
    <AuthProvider>
      <BrowserRouter>
          <Route component={ Home } path="/" exact />
          <Route component={ Cart } path="/cart" exact />
          <Route component={ PopUpLogin } path="/login" exact />

          <Switch>
            <Route component={ Identification } path="/checkout" exact />
            <PrivateRoute component={ Address } path="/checkout/address" exact />
          </Switch>
      </BrowserRouter>
    </AuthProvider>
  );
};

export default Routes;