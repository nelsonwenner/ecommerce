import React from "react";
import { Route, BrowserRouter, Switch } from "react-router-dom";

import { AuthProvider } from '../providers/AuthProvider';

import Identification from '../components/common/Identification';
import Address from '../components/common/Address';
import Cart from '../pages/Cart';
import Home from "../pages/Home";

const Routes = () => {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Route component={ Home } path="/" exact />
        <Route component={ Cart } path="/cart" exact />
        
        <Switch>
          <Route component={ Identification } path="/checkout" exact />
          <Route component={ Address } path="/checkout/address" exact />
        </Switch>
      </AuthProvider>
    </BrowserRouter>
  );
};

export default Routes;