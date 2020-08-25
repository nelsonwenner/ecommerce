import React,{ useState } from 'react';
import * as yup from 'yup';
import './styles.css';

import { useAuth } from '../../../providers/AuthProvider';
import redirect from '../../../routes/redirect';
import { CustomInput } from '../CustomInput';
import { useForm } from "react-hook-form";

const validationSchema = yup.object().shape({
  email: yup.string().label('Email').required().max(50),
  password: yup.string().label('Password').required().max(25),
})

const Login = ({ activeSignUp, path }) => {
  const { register, handleSubmit, errors } = useForm({
    validationSchema: validationSchema,
  });

  const [error, setError] = useState('');
  const { signIn } = useAuth();
  
  const onSubmit = async (data) => {

    const error = await signIn(data);
    
    if (error) {
      return setError('authentication failure');
    }
    
    redirect(path);
  }
  
  return (
    <form onSubmit={ handleSubmit(onSubmit) } className="form-login card-hover">
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
          errors={ errors.email }
          register={ register }
        />

        <CustomInput 
          classs={'wrapper-input' }
          type={ 'password' }
          icon={ 'password' }
          name={ 'password' }
          placeholder={ 'Password' }
          errors={ errors.password }
          register={ register }
        />

        <button className="btn btn-rounded black-btn btn-outlined">Login</button>

        { 
          error && (
            <div className="error-login">
              <p style={{color: 'red'}}>{ error }</p>
            </div>
          )
        }
      </div>

      <div className="link-register" onClick={ activeSignUp }>
        <p>Sign up</p> 
        <span>&rarr;</span>
      </div>
    </form>
  )
}

export default Login;