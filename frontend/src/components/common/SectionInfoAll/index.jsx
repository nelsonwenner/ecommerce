import React from 'react';
import { Link } from 'react-router-dom'; 
import './styles.css';

const SectionInfoAll = () => {
  return (
    <div className="container mt-30">
      <div className="section-info-all-main">
        <div className="section-title">
          Products
        </div>
        <div className="section-button">
          <Link to={'/'}>
            <span className="btn btn-primary btn-black" >View All</span>
          </Link>
        </div>
      </div>
    </div>
  )
}

export default SectionInfoAll;