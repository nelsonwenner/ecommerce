import React from 'react';

import { CartProvider } from '../../../providers/CartProvider';
import Header from '../../theme/Header';
import Footer from '../../theme/Footer';
import { Wrapper } from './styles';

const Layout = ({ children }) => {
  return (
    <CartProvider>
      <Header />
      <Wrapper>
        { children }
      </Wrapper>
      <Footer />
    </CartProvider>
  )
}

export default Layout;