import React from 'react';
import './styles.css';

const DropDown = () => {
  return (
    <div className="dropdown">
      <ul className="dropdown-wrapper">
        <li className="dropdown-item">
          <p>Account</p>
          <span className="icon-account"></span>
        </li>
        <li className="dropdown-item" >
          <p>Logout</p>
          <span className="icon-logout"></span>
        </li>
      </ul>
    </div>
  )
}

export default DropDown;