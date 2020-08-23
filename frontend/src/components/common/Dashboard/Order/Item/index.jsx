import React from 'react';

const Item = ({ date, items_checkout, total }) => {
  
  const dateFormat = (date) => {
    return new Date(date)
    .toISOString()
    .replace(/T/, ' ')
    .replace(/\..+/, '');
  }

  return (
    <div className="order-box-item">
      <div className="order-content">
        <div className="order-date">
          <p>Order in { dateFormat(date) }</p>
        </div>
        <div className="order-products-wrapper">
          {items_checkout.map((i, index) => (
            <div className="order-product" key={ index }>
              <span className="icon-product"></span>
              <span className="product-quantity">{ i.quantity }</span>
              <p className="product-title">{ 'Batman' }</p>
            </div>
          ))}
        </div>
        <p className="order-product-total">{ total }</p>
      </div>
    </div>
  )
}

export default Item;