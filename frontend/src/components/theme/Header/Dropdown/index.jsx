import React from 'react';
import './styles.css';

import { useAuth } from '../../../../providers/AuthProvider';

const DropDown = () => {
  const { logout } = useAuth();
  
  return (
    <div className="dropdown">
      <ul className="dropdown-wrapper">
        <li className="dropdown-item">
          <p>Account</p>
          <span className="icon-account"></span>
        </li>
        <li className="dropdown-item" onClick={ () => logout() } >
          <p>Logout</p>
          <span className="icon-logout"></span>
        </li>
      </ul>
    </div>
  )
}

export default DropDown;