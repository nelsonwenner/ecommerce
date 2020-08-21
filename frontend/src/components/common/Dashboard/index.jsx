import React from 'react';
import './styles.css';

import Sidebar from './Sidebar';
import Layout from '../Layout';

const Dashboard = () => {
  return (
    <Layout>
      <div className="dashboard-main">
        <div className="container">
          <div className="row">
            <div className="column xlarge-4 large-5 medium-12 small-12">
              <div className="wrapper-dashboard">
                <Sidebar />
              </div>
            </div>
            <div className="column xlarge-8 large-7 medium-12 small-12" style={{ background: 'blue' }}>
              <div className="wrapper-dashboard">

              </div>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  )
}

export default Dashboard;