import React from 'react';

const CustomInput = ({classs, icon, type, placeholder, autoComplete, value, name, onChange}) => (
  <div className={`${classs}`}>
    <span className={`${icon}-icon`}></span>
    <input className="input-field"
      type={type}
      placeholder={placeholder}
      autoComplete={autoComplete}
      value={value}
      onChange={onChange}
      name={name}
    />
  </div>
)

export { CustomInput }