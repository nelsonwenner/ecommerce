import React from 'react';

import Header from '../../components/theme/Header';
import Carousel from '../../components/common/Carousel';
import SectionInfoAll from '../../components/common/SectionInfoAll';

const Home = () => {

  return (
    <div className="home">
      <Header />
      <Carousel />
      <SectionInfoAll />
      
    </div>
  )
}

export default Home;