import React, { createContext, useContext } from 'react';

import usePersistedState from '../hooks/usePersistedState';

const CartContext = createContext();
export const useCart = () => useContext(CartContext);

export const CartProvider = ({ children }) => {
  const [cart, setCart] = usePersistedState('cart', []);
  
  const getCartTotal = () => (cart.reduce((acc, current) => acc + (current.price * current.quantity), 0)).toFixed(2);

  const getProductQuantity = () => cart.map(product => product.quantity).reduce((accum, curr) => accum + curr);

  const addProduct = (product) => {
    
    const productSerialized = {
      image_url: product.image_url,
      title: product.title,
      product: product.id,
      price: product.price,
      quantity: 1,
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

  const removeProduct = (product) => {
    const filteredProducts = cart.filter(item => item.product !== product.product);

    if (product.quantity > 1) {
      product.quantity -= 1;
      setCart([...filteredProducts, product]);
    } else {
      setCart([...filteredProducts]);
    }
  }

  return (
    <CartContext.Provider value={ {cart, getCartTotal, getProductQuantity, addProduct, removeProduct} } >
      { children }
    </CartContext.Provider>
  )
}
