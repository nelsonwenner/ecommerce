import React from "react";
import { Route, BrowserRouter, Switch } from "react-router-dom";

import Identification from '../components/common/Identification';
import Cart from '../pages/Cart';
import Home from "../pages/Home";

const Routes = () => {
  return (
    <BrowserRouter>
      <Route component={ Home } path="/" exact />
      <Route component={ Cart } path="/cart" exact />
      
      <Switch>
        <Route component={ Identification } path="/checkout" exact />
      </Switch>
    </BrowserRouter>
  );
};

export default Routes;