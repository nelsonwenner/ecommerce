import React from 'react';
import './styles.css';

import Search from './Search';
import Cart from './Cart';
import Info from './Info';

const Drop = () => {
  return (
    <div className="drop-main">
      <div className="container">
        <div className="drop-wrapper">
          <Info />
          <Search />
          <Cart />
        </div>
      </div>
    </div>
  )
}

export default Drop;