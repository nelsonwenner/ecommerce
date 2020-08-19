import Axios from 'axios';

const ApiAuth = (token) => Axios.create({
  baseURL: `${process.env.REACT_APP_ECOMMERCE_API_URL}`,
  headers: {
    "Content-Type": "application/json",
    "Authorization": `Bearer ${token}`
  }
})

export default ApiAuth;