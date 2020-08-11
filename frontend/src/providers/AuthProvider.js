import React, { createContext, useContext } from 'react';

import useProviderAuth from '../hooks/usePersistedAuth';
import api from '../services/Api';

const AuthContext = createContext();
export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [auth, setAuth] = useProviderAuth('@Auth');

  const signIn = async (data) => {
    try { 
      const res = await api.post('/api-token', data);

      if (res.status >= 400) {
        throw new Error("Bad response");
      }

      const dataSerialized = {
        auth: true,
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
    <AuthContext.Provider value={ auth, signIn }>
      { children }
    </AuthContext.Provider>
  )
}