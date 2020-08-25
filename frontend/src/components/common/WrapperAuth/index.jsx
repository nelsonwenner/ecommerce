import React, { useState } from 'react';
import './styles.css';

import Register from '../Register';
import Modal from 'react-modal';
import Login from '../Login';

Modal.setAppElement('body');

const WrapperAuth = ({ openModal, closeModal, path }) => {
  const [signUp, setSignUp] = useState(false);

  const activeSignUp = () => {
    setSignUp(!signUp);
  }
  
  return (
    <Modal
      isOpen={ openModal }
      onRequestClose={ closeModal }
      className={"ReactModal__Content_Login"}
      overlayClassName={"ReactModal__Overlay_Login"}
      contentLabel="Modal"
    >
      {
        !signUp 
        ? (
          <Login 
            activeSignUp={ activeSignUp }
            path={ path }
          />
        )
        : (
          <Register />
        )
      }
      
    </Modal> 
  )
}

export default WrapperAuth;