import React from 'react';

import { CartProvider } from '../../../providers/CartProvider';
import { AuthProvider } from '../../../providers/AuthProvider';
import Header from '../../theme/Header';
import Footer from '../../theme/Footer';
import { Wrapper } from './styles';

const Layout = ({ children }) => {
  return (
    <AuthProvider>
      <CartProvider>
        <Header />
        <Wrapper>
          { children }
        </Wrapper>
        <Footer />
      </CartProvider>
    </AuthProvider>
  )
}

export default Layout;