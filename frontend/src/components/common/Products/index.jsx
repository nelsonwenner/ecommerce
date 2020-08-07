import React, { useState, useEffect } from 'react';
import './styles.css';

import { useCart } from '../../../providers/CartProvider';
import ProductDetail from './ProductDetail';
import api from '../../../services/Api';

const Products = () => {
  const [products, setProducts] = useState([]);
  const { addProduct } = useCart();
  
  useEffect(() => {
    api.get('/products').then(({ data }) => {
      setProducts(data.results);
    });
  }, []);
  
  return (
    <div className="container wrapper-products">
      {products.map((product, index) => (
        <ProductDetail
          key={ index }   
          title={ product.title }
          price={ product.price }
          image_path={ product.image_url }
          onClick={ () => addProduct(product) }
        />
      ))}
    </div>
  )
}

export default Products; 