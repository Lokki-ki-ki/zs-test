// axios-config.js
import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:5000', // Replace this with your backend server URL
});

export default axiosInstance;
