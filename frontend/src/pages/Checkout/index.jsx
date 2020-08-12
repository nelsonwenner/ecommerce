import React from 'react';
import './styles.css';

import Layout from '../../components/common/Layout';
import Step from '../../components/common/Step';

const Checkout = ({ children }) => {
  return (
    <Layout>
      <Step />
      { children }
    </Layout>
  )
}

export default Checkout;