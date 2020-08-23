import React, { useEffect, useState } from 'react';
import './styles.css';

import { useAuth } from '../../../../providers/AuthProvider';
import ApiAuth from '../../../../services/ApiAuth';

const Order = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    ApiAuth()
  }, []);
  
  return (
    <div className="order-wrapper">
      <h4 className="order-title">Past orders</h4>
      <div className="order-box-item">

      </div>
    </div>
  )
}

export default Order;