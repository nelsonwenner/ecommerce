import React from 'react';
import './styles.css';

import logo from '../../../../assets/logo-nav.png';

const Navbar = () => {
  return (
    <div className="navbar-main">
      <div className="container">
        <div className="navbar">
          <a href="/" className="logo">
            <img alt="logo" src={ logo } />
          </a>
          <div className="icon-user">
            <span>Login</span>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Navbar;