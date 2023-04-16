import { toast } from 'components/sweetalert2/instance';
import Axios from "axios"
import { parseCookies, setCookie, destroyCookie } from 'nookies'

import { apiUrl } from "constant/env";
import { useDispatch, useSelector } from "react-redux";
import { getSLoginToken } from "store/auth/selectors";
import { ILogin } from 'store/auth/types';

console.log('11111111111', apiUrl);

const requestInstance = Axios.create({
  baseURL: apiUrl,
  timeout: 3000,
  headers: {}
});

let isLoading = false;

requestInstance.interceptors.request.use(config => {
  isLoading = true;
  // const token = useSelector(getSLoginToken);

  // TODO: use token from store instead of localstorage
  const cookies = parseCookies();
  let token: ILogin | null = null;
  if (cookies && cookies.token) {
    token = JSON.parse(cookies.token);
  }
  if (token) {
    config.headers.Authorization = `Bearer ${token.access}`;
  }
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
