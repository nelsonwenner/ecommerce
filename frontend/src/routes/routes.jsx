import React from "react";
import { Route, BrowserRouter, Switch } from "react-router-dom";

import Checkout from '../pages/Checkout';
import Cart from '../pages/Cart';
import Home from "../pages/Home";

const Routes = () => {
  return (
    <BrowserRouter>
      <Route component={ Home } path="/" exact />
      <Route component={ Cart } path="/cart" exact />
      <Route component={ Checkout } path="/checkout" exact />
    </BrowserRouter>
  );
};

export default Routes;