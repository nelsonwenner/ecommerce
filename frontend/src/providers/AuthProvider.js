import React, { createContext, useContext } from 'react';

import usePersistedState from '../hooks/usePersistedState';
import api from '../services/Api';

const AuthContext = createContext();
export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [auth, setAuth] = usePersistedState('@Auth', {
    authorized: false, 
    token: null,
    id: null, 
    name: '', 
    email: '', 
    address: []
  });

  const signIn = async (data) => {
    try { 
      const res = await api.post('/api-token', data);
 
      if (res.status >= 400) {
        throw new Error("Bad response");
      }

      const dataSerialized = {
        authorized: true,
        token: res.data.access,
        id: res.data.id,
        name: res.data.username,
        email: res.data.email,
        address: {}
      }

      setAuth(dataSerialized);
      
      return false;

    } catch (error) {
      return error;
    }
  }

  return (
    <AuthContext.Provider value={ {auth, signIn} }>
      { children }
    </AuthContext.Provider>
  )
}