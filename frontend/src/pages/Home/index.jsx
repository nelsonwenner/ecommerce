import React from 'react';
import './styles.css';

import SectionInfoAll from '../../components/common/SectionInfoAll';
import Products from '../../components/common/Products';
import Carousel from '../../components/common/Carousel';
import Layout from '../../components/common/Layout';

const Home = () => {
  return (
    <Layout>
      <Carousel />
      <SectionInfoAll />
      <Products />
    </Layout>
  )
}

export default Home;