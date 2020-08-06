import React from 'react';
import './styles.css';

import SectionInfoAll from '../../components/common/SectionInfoAll';
import { CartProvider } from '../../providers/CartProvider';
import Products from '../../components/common/Products';
import Carousel from '../../components/common/Carousel';
import Footer from '../../components/theme/Footer';
import Header from '../../components/theme/Header';

const Home = () => {
  return (
    <CartProvider>
      <Header />
      <Carousel />
      <SectionInfoAll />
      <Products />
      <Footer />
    </CartProvider>
  )
}

export default Home;