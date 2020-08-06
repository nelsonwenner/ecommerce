import React, { useEffect, useState } from 'react';
import './styles.css';

import SectionInfoAll from '../../components/common/SectionInfoAll';
import Carousel from '../../components/common/Carousel';
import Product from '../../components/common/Product';
import Footer from '../../components/theme/Footer';
import Header from '../../components/theme/Header';
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
      
      <Footer />
    </div>
  )
}

export default Home;