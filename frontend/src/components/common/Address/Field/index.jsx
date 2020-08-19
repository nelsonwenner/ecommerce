import React from 'react';

const Field = ({ errors, id, htmlFor, label, name, register, selectedAddress, placeholder }) => {
  return (
    <div className="field" id={ id }>
      <label htmlFor={ htmlFor }>{ label }</label>
      <input 
        type="text"
        name={ name }
        placeholder={ selectedAddress ? selectedAddress[name] : placeholder }
        className={ `form-controll ${(errors ? 'is-invalid' : '')} ${ selectedAddress ? 'disabled' : '' }` }
        ref={ register }
        defaultValue={ selectedAddress ? selectedAddress[name] : '' }
      />
      <div className="invalid-feedback">
        { errors && errors.message }
      </div>
    </div>
  )
}

export default Field;