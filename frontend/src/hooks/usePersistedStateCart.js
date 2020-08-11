import { useState, useEffect } from 'react';

const usePersistedStateCart = (key) => {
  const [cart, setCart] = useState(() => {
    const storageValue = localStorage.getItem(key);
    
    if (storageValue) {
      return JSON.parse(storageValue);
    } else {
      return [];
    } 
  });
  
  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(cart));
  }, [key, cart]);

  return [cart, setCart];
}

export default usePersistedStateCart;