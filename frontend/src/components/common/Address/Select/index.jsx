import React from 'react';

const Select = ({ classs, address, name, htmlFor, handlerSelectAddress }) => {
  return (
    <div className={ classs }>
      <label htmlFor={ htmlFor }>Selected Address</label>
      
      <select 
        name={ name } 
        onChange={ handlerSelectAddress }
      >
        <option value="0">Select a Address Exists</option>
        {address.map((addrr, index) => (
          <option key={index} value={JSON.stringify(addrr)}>
            { `Address #${index + 1} Zipcode: ${addrr.zipcode}` }
          </option>
        ))}
      </select>
    </div>
  )
}

export default Select;