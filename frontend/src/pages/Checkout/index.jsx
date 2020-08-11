import React from 'react';
import './styles.css';

import Layout from '../../components/common/Layout';
import Step from '../../components/common/Step';

const Checkout = ({ children }) => {
  return (
    <Layout>
      <div className="container">
        <div className="step-wrapper">
          <Step />
        </div>
      </div>
      { children }
    </Layout>
  )
}

export default Checkout;