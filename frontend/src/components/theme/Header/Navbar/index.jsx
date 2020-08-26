import React,{ useState } from 'react';
import './styles.css';

import { useAuth } from '../../../../providers/AuthProvider';
import WrapperAuth from '../../../common/WrapperAuth';
import logo from '../../../../assets/logo-nav.png';
import { Link } from 'react-router-dom';
import DropDown from '../Dropdown';

const Navbar = () => {
  const [modalLogin, setModalLogin] = useState(false);
  const { auth, isAuth } = useAuth();

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
          <Link to={ '/' } className="logo">
            <img alt="logo" src={ logo } />
          </Link>
          {
            isAuth() 
            ? (
              <div className="box-user">
                <div className="icon-user">
                  <span>{ auth.name }</span>
                </div>

                <DropDown />
              </div>
            )
            : (
              <div className="icon-user-lock" onClick={ openModal }>
                <span>Login</span>
              </div>
            ) 
          }
        </div>
      </div>
      <WrapperAuth 
        openModal={ modalLogin }
        closeModal={ closeModal }
        path={ '/' }
      />
    </div>
  )
}

export default Navbar;