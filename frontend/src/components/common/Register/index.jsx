import React from 'react';
import * as yup from 'yup';
import './styles.css';

import { useAuth } from '../../../providers/AuthProvider';
import redirect from '../../../routes/redirect';
import { CustomInput } from '../CustomInput';
import { useForm } from "react-hook-form";

const validationSchema = yup.object().shape({
  name: yup.string().label('Name').required().max(50),
  email: yup.string().label('Email').required().max(50),
  password: yup.string().label('Password').required().max(25),
  personal_document: yup.string().label('Personal document').required().max(13),
  phone: yup.string().label('Phone').required().max(12),
})

const Register = () => {
  const { register, handleSubmit, errors } = useForm({
    validationSchema: validationSchema,
  });
  
  const { signUp } = useAuth();

  const onSubmit = async (data) => {
    await signUp(data);
    redirect('/');
  }

  return (
    <form onSubmit={ handleSubmit(onSubmit) } className="form-signup card-hover">
      <h2 className="login-welcome">Sign up</h2>
      
      <div className="input-container">
        <CustomInput 
          classs={'wrapper-input' }
          type={ 'text' }
          name={ 'name' }
          icon={ 'user-signup' }
          placeholder={ 'Name' }
          errors={ errors.name }
          register={ register }
        />

        <CustomInput 
          classs={'wrapper-input' }
          type={ 'email' }
          name={ 'email' }
          icon={ 'email' }
          placeholder={ 'Email' }
          errors={ errors.email }
          register={ register }
        />

        <CustomInput 
          classs={'wrapper-input' }
          type={ 'password' }
          name={ 'password' }
          icon={ 'password' }
          placeholder={ 'Password' }
          errors={ errors.password }
          register={ register }
        />

        <CustomInput 
          classs={'wrapper-input' }
          name={ 'personal_document' }
          icon={ 'document' }
          placeholder={ 'Personal document' }
          errors={ errors.personal_document }
          register={ register }
        />

<       CustomInput 
          classs={'wrapper-input' }
          name={ 'phone' }
          icon={ 'phone-user' }
          placeholder={ 'Phone' }
          errors={ errors.phone }
          register={ register }
        />

        <button className="btn btn-rounded black-btn btn-outlined">Register</button>
      </div>
    </form>
  )
}

export default Register;