import React,{ useState } from 'react';
import './styles.css';

import logo from '../../../../assets/logo-nav.png';
import LoginModal from '../../../common/Login';

const Navbar = () => {
  const [modalLogin, setModalLogin] = useState(false);

  const openModal = () => {
    setModalLogin(true);
  }

  const closeModal = () => {
    setModalLogin(false);
  }
  
  return (
    <div className="navbar-main">
      <div className="container">
        <div className="navbar">
          <a href="/" className="logo">
            <img alt="logo" src={ logo } />
          </a>
          <div className="icon-user" onClick={ openModal }>
            <span>Login</span>
          </div>
        </div>
      </div>
      <LoginModal 
        openModal={ modalLogin }
        closeModal={ closeModal }
      />
    </div>
  )
}

export default Navbar;