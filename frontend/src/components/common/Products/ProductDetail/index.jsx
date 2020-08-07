import React from 'react';
import './styles.css';

const ProductDetail = ({ title, price, image_path, onClick }) => {
  return (
    <div className="card" onClick={ onClick }>
      <div className="card-img">
        <img src={ `${process.env.REACT_APP_ECOMMERCE_API_URL}${image_path}` } alt={title} />
      </div>
      <div className="card-title">
        <p>{ title }</p>
      </div>
      <span className="dolar-icon">{ price }</span>
      <div className="overlay">
        <div className="card-button">Add To Cart</div>
      </div>
    </div>  
  )
}

export default ProductDetail;