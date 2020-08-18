import React from 'react';

const Select = ({ errors, classs, name, ref, cartTotal }) => {
  return (
    <div className={ classs }>
      <select
        className={'form-controll' + (errors ? ' is-invalid' : '') }  
        name={ name }
        ref={ ref }
      >
        <option value="0" >Select Installments</option>
      
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