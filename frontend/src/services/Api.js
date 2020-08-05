import Axios from 'axios';

const api = Axios.create({
  baseURL: `${process.env.REACT_APP_ECOMMERCE_API_URL}`,
  headers: {
    "Content-Type": "application/json"
  }
})

export default api;