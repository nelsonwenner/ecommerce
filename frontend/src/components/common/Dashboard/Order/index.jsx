import React, { useEffect, useState } from 'react';
import './styles.css';

import { useAuth } from '../../../../providers/AuthProvider';
import ApiAuth from '../../../../services/ApiAuth';
import Item from './Item';

const Order = () => {
  const [orders, setOrders] = useState([]);
  const { auth } = useAuth();

  useEffect(() => {
    ApiAuth(auth.token).get('/checkouts')
    .then(({ data }) => {
      setOrders(data)
    });
  }, []);

  return (
    <div className="order-wrapper">
      <h4 className="order-title">Past orders</h4>
      <div className="order-wrapper-content-scroll">
        {orders.map((order, index) => (
          <Item 
            key={ index } 
            date={ order.created_at }
            items_checkout={ order.items }
            total={ order.total }
            status={ order.status.message }
          />
        ))}
      </div>
    </div>
  )
}

export default Order;