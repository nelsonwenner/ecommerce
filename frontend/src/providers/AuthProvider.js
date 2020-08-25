import React, { createContext, useContext } from 'react';

import usePersistedState from '../hooks/usePersistedState';
import redirect from '../routes/redirect';
import api from '../services/Api';

const AuthContext = createContext();
export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [auth, setAuth] = usePersistedState('@Auth', {});

  const logout = () => {
    localStorage.removeItem('@Auth');
    redirect('/');
  }

  const isAuth = () => auth.authorized;
  
  const getUserId = () => auth.id;

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

  const signUp = async (data) => {
    return await api.post('/clients', data);
  }

  return (
    <AuthContext.Provider value={ {auth, signIn, signUp, logout, isAuth, getUserId} }>
      { children }
    </AuthContext.Provider>
  )
}