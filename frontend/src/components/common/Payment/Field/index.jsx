import React from 'react';
import './styles.css';

const Field = ({ errors, name, placeholder, ref , classs }) => {
  return (
    <div className={ classs }>
      <input
        className={'form-controll' + (errors ? ' is-invalid' : '') } 
        type="text"
        name={ name }
        placeholder={ placeholder }
        ref={ ref }
      />
      <div className="invalid-feedback">
        { errors && errors.message }
      </div>
    </div>
  )
}

export default Field;