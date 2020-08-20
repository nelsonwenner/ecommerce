import React from 'react';
import './styles.css';

import Navbar from './Navbar';
import Drop from './Drop';

const Header = () => {
  return (
    <div className="fixed-top">
      <Navbar />
      <Drop />
    </div>
  )
}

export default Header;