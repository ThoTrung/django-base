import Axios from "axios"

import { apiUrl } from "constant/env";

const requestInstance = Axios.create({
  baseURL: apiUrl,
  timeout: 3000,
  headers: {}
});

let isLoading = false;

requestInstance.interceptors.request.use(config => {
  isLoading = true;
  return config;
});

requestInstance.interceptors.response.use(response => {
  isLoading = false;
  return response;
}, error => {
  isLoading = false;
  throw error;
});

export default requestInstance;
