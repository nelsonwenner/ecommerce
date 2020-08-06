import React, { useEffect, useState } from 'react';
import './styles.css';

import Header from '../../components/theme/Header';
import Carousel from '../../components/common/Carousel';
import SectionInfoAll from '../../components/common/SectionInfoAll';

import Product from '../../components/common/Product';
import api from '../../services/Api';

const Home = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    api.get('/products').then(({ data }) => {
      setProducts(data.results);
    });
  }, []);

  return (
    <div className="home">
      <Header />
      <Carousel />
      <SectionInfoAll />
      
      <div className="container wrapper-home">
        {products.map((product, index) => (
          <Product 
            key={ index }   
            title={ product.title }
            price={ product.price }
            image_path={ product.image_url }
          />
        ))}
      </div>
    </div>
  )
}

export default Home;