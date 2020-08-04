import React from 'react';
import './styles.css';

import Modal from 'react-modal';

Modal.setAppElement('body');

const LoginModal = ({ openModal, closeModal }) => {
  return (
    <Modal
      isOpen={ openModal }
      onRequestClose={ closeModal }
      className={"ReactModal__Content_Login"}
      overlayClassName={"ReactModal__Overlay_Login"}
    >
      <form method="post" className="form-login">
        <h2 className="login-welcome">Welcome</h2>
        <div className="division">
          <div className="line"></div>
            <span className="title">Client</span>
          <div className="line"></div>
        </div>
      
        <div className="wrapper-input validate-input">
          <span className="icon-email"></span>
          <input className="input-form" type="text" name="email" placeholder="Email"></input>
        </div>
      </form>
    </Modal>
  )
}

export default LoginModal;