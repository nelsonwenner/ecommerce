import React, { useState } from 'react';
import './styles.css';

import { Overlay } from './styles';
import Sidebar from './Sidebar';
import Layout from '../Layout';
import Order from './Order';

const Dashboard = () => {
  const [sidebar, setSidebar] = useState(false);

  const showSidebar = () => setSidebar(!sidebar);
  
  return (
    <Layout>
      <Overlay sidebar={ sidebar } onClick={ showSidebar } />
      <div className="dashboard-main">
        <div className="container">
          <div className="row">
            <div className="column xlarge-4 large-5 medium-0 small-0">
              <div className="wrapper-dashboard">
                <Sidebar
                  isToolbar={ sidebar }
                />
              </div>
            </div>
            <div className="column xlarge-8 large-7 medium-12 small-12">
              <div className="wrapper-dashboard-content">
                <span className="icon-hamburger-sidebar" onClick={ showSidebar } ></span>
                <Order />
              </div>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  )
}

export default Dashboard;