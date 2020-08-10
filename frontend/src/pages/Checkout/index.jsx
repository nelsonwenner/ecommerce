import React from 'react';
import './styles.css';

import Layout from '../../components/common/Layout';
import Step from '../../components/common/Step';

const Checkout = ({ children }) => {
  return (
    <Layout>
      <div className="checkout-main">
        <div className="container">
          <div className="step-wrapper">
            <Step />
          </div>
          { children }
        </div>
      </div>
    </Layout>
  )
}

export default Checkout;