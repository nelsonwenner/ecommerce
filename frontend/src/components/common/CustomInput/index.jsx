import React from 'react';

const CustomInput = ({classs, icon, type, placeholder, errors, name, register}) => (
  <div className={`${classs}`}>
    <span className={`${icon}-icon`}/>
    <input 
      className={'input-field form-controll' + (errors ? ' is-invalid' : '') }
      type={type}
      placeholder={placeholder}
      ref={register}
      name={name}
    />
    <div className="invalid-feedback">
      { errors && errors.message }
    </div>
  </div>
)

export { CustomInput }