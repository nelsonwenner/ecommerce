import React,{ useState } from 'react';
import './styles.css';

import { useAuth } from '../../../providers/AuthProvider';
import { CustomInput } from '../CustomInput';
import Modal from 'react-modal';

Modal.setAppElement('body');

const LoginModal = ({ openModal, closeModal }) => {
  const { signIn } = useAuth();
  
  const [data, setData] = useState({
    email: '',
    password: '',
    error: null
  });

  const handleChange = (event) => {
    event.preventDefault();
    setData({...data, [event.target.name]: event.target.value});
  }
  
  const onSubmit = async (event) => {
    event.preventDefault();
    
    const { email, password } = data;
    
    if (!email || !password) {
      setData(() => ({error: 'Fill in all the fields'}));
    } else {
      const error = await signIn({email, password});
      
      if (error) {
        setData(() => ({error: error}));
      }
    }
  }
  
  return (
    <Modal
      isOpen={ openModal }
      onRequestClose={ closeModal }
      className={"ReactModal__Content_Login"}
      overlayClassName={"ReactModal__Overlay_Login"}
      contentLabel="Modal"
    > 
      <form onSubmit={ onSubmit } method="post" className="form-login card-hover">
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
            onChange={ handleChange }
          />

          <CustomInput 
            classs={'wrapper-input' }
            type={ 'password' }
            icon={ 'password' }
            name={ 'password' }
            placeholder={ 'Password' }
            onChange={ handleChange }
          />
          
          <button className="btn btn-rounded black-btn btn-outlined">Login</button>
        </div>
      </form>
    </Modal>
  )
}

export default LoginModal;