import React, { useState, useEffect } from 'react';
import './styles.css';

import ProductDetail from './ProductDetail';
import api from '../../../services/Api';

const Products = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    api.get('/products').then(({ data }) => {
      setProducts(data.results);
    });
  }, []);
  
  const handlerClicked = (item) => {
    console.log(item)
  }
  
  return (
    <div className="container wrapper-products">
      {products.map((product, index) => (
        <ProductDetail
          key={ index }   
          title={ product.title }
          price={ product.price }
          image_path={ product.image_url }
          onClick={ () => handlerClicked(product) }
        />
      ))}
    </div>
  )
}

export default Products; 