import { useState, useEffect } from 'react';

const usePersistedState = (key, structure) => {
  const [state, setState] = useState(() => {
    const storageValue = localStorage.getItem(key);
    
    if (storageValue) {
      return JSON.parse(storageValue);
    } else {
      return structure;
    } 
  });
  
  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(state));
  }, [key, state]);

  return [state, setState];
}

export default usePersistedState;