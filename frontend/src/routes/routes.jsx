import React from "react";
import { Route, BrowserRouter } from "react-router-dom";

import Cart from '../pages/Cart';
import Home from "../pages/Home";

const Routes = () => {
  return (
    <BrowserRouter>
      <Route component={ Home } path="/" exact />
      <Route component={ Cart } path="/cart" exact />
    </BrowserRouter>
  );
};

export default Routes;