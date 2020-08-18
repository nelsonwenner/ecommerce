import React from 'react';

const Select = ({ errors, classs, name, register, cartTotal }) => {
  return (
    <div className={ classs }>
      <select
        className={'form-controll' + (errors ? ' is-invalid' : '') }  
        defaultValue=""
        name={ name }
        ref={ register }
      >
        <option value="" disabled="disabled" >Select Installments</option>
      
        {Array.from(Array(12).keys()).map(i => (
          <option key={ i } value={ i+1 }> 
            { i+1 } x { ( cartTotal /(i+1)).toFixed(2) }
          </option>
        ))}
      </select>
      <div className="invalid-feedback">
        { errors && errors.message }
      </div>
  </div>
  )
}

export default Select;