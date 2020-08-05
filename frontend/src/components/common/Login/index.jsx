import React from 'react';
import './styles.css';

import Modal from 'react-modal';
import { CustomInput } from '../CustomInput';

Modal.setAppElement('body');

const LoginModal = ({ openModal, closeModal }) => {
  return (
    <Modal
      isOpen={ openModal }
      onRequestClose={ closeModal }
      className={"ReactModal__Content_Login"}
      overlayClassName={"ReactModal__Overlay_Login"}
      contentLabel="Modal"
    >
      <form method="post" className="form-login card-hover">
        <h2 className="login-welcome">Welcome</h2>
        <div className="division">
          <div className="line"></div>
            <span className="title">Client</span>
          <div className="line"></div>
        </div>

        <div className="input-container">
          <CustomInput 
            classs={'wrapper-input' }
            type={ 'email' }
            icon={ 'email' }
            name={ 'email' }
            placeholder={ 'Email' }
          />

          <CustomInput 
            classs={'wrapper-input' }
            type={ 'password' }
            icon={ 'password' }
            name={ 'password' }
            placeholder={ 'Password' }
          />

          <button className="btn btn-rounded black-btn btn-outlined">Login</button>
        </div>
      </form>
    </Modal>
  )
}

export default LoginModal;