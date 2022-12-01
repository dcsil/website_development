import axios from 'axios';

export const service = axios.create({
  baseURL: process.env.VUE_APP_SERVER,
  timeout: 10000, //overtime
});

// export default service;
