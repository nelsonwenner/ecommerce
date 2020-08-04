import React from 'react';
import './styles.css';

const Search = () => {
  return (
    <div className="search">
      <div className="input-group">
        <input type="text" className="form-control" placeholder="Search products" />
        <div className="search-btn">
          <span className="icon-search"></span>
        </div>
      </div>
    </div>
  )
}

export default Search;