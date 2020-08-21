import React, { useState } from 'react';
import './styles.css';

import { Overlay } from './styles';
import Sidebar from './Sidebar';
import Layout from '../Layout';

const Dashboard = () => {
  const [sidebar, setSidebar] = useState(false);

  return (
    <Layout>
      <Overlay sidebar={ sidebar } />
      <div className="dashboard-main">
        <div className="container">

          <div className="row">
            <div className="hidden column xlarge-4 large-5 medium-12 small-12">
              <div className="wrapper-dashboard">
                <Sidebar />
              </div>
            </div>
            <div className="column xlarge-8 large-7 medium-12 small-12" style={{ background: 'blue' }}>
              <div className="wrapper-dashboard-content">
                <span className="icon-hamburger-sidebar" onClick={ () => setSidebar(!sidebar) } ></span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  )
}

export default Dashboard;