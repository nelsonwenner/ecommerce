import React, { createContext, useState, useContext } from 'react';

const CartContext = createContext();
export const useCart = () => useContext(CartContext);

export const CartProvider = ({ children }) => {
  const [cart, setCart] = useState([]);

  const addProduct = (product) => {

    const productSerialized = {
      product: product.id,
      price: product.price,
      quantity: 1
    }
    
    const alreadySelected = cart.find(item => item.product === product.id);

    if (alreadySelected) {
      productSerialized.quantity += alreadySelected.quantity;
      const filteredProducts = cart.filter(item => item.product !== product.id);
      setCart([...filteredProducts, productSerialized]);
    } else {
      setCart((prev) => [...prev, productSerialized]);
    }
  }

  return (
    <CartContext.Provider value={ [cart, addProduct] } >
      { children }
    </CartContext.Provider>
  )
}
