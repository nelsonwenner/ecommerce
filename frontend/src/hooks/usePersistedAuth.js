import { useState, useEffect } from 'react';

const usePersistedAuth = (key) => {
  const [auth, setAuth] = useState(() => {
    const storageValue = localStorage.getItem(key);
    
    if (storageValue) {
      return JSON.parse(storageValue);
    } else {
      return {
        authorized: false, 
        token: null,
        id: null, 
        name: '', 
        email: '', 
        address: []
      };
    } 
  });
  
  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(auth));
  }, [key, auth]);

  return [auth, setAuth];
}

export default usePersistedAuth;