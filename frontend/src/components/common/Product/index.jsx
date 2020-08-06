import React from 'react';
import './styles.css';

const Product = ({ title, price, image_path }) => {
  return (
    <div className="card">
      <div className="card-img">
        <img src={ `${process.env.REACT_APP_ECOMMERCE_API_URL}${image_path}` } alt={title} />
      </div>
      <div className="card-title">
        <p>{ title }</p>
      </div>
      <span className="dolar-icon">{ price }</span>
    </div>  
  )
}

export default Product;