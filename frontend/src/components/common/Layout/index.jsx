import React from 'react';

import Header from '../../theme/Header';
import Footer from '../../theme/Footer';
import { Wrapper } from './styles';

const Layout = ({ children }) => {
  return (
    <>
      <Header />
      <Wrapper>
        { children }
      </Wrapper>
      <Footer />
    </>
  )
}

export default Layout;