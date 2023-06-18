import { toast } from 'components/sweetalert2/instance';
import Axios from "axios"
import { parseCookies, setCookie, destroyCookie } from 'nookies'

import { apiUrl } from "constant/env";
import { useDispatch, useSelector } from "react-redux";
import { getSLoginToken } from "store/auth/selectors";
import { ILogin } from 'store/auth/types';
import { isUnauthenticate, isInvalid } from './helper';
import { swal } from 'components/sweetalert2/instance'
import { AShowLoading, AHideLoading } from 'store/common/actions'
import { put, call } from 'redux-saga/effects';

console.log('apiUrl 11-----------------', apiUrl, process.browser);

const requestInstance = Axios.create({
  baseURL: process.browser ? apiUrl : 'http://app:8000/',
  timeout: 300000,
  headers: {}
});

// let isLoading = false;

requestInstance.interceptors.request.use(function (config) {
  // isLoading = true;
  // const token = useSelector(getSLoginToken);

  // TODO: use token from store instead of localstorage
  // yield call(requestShowLoading);
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
  // isLoading = false;
  if (response) {
    return response;
  } else {
    swal.fire({ text: 'Có lỗi xảy ra. Vui long liên hệ Admin để xử lý.', icon: 'error' })
  }
}, error => {
  console.log('error .....', error)
  // isLoading = false;
  if (error.response) {
    if (isInvalid(error.response)) {
      return error.response;
    } else if (isUnauthenticate(error.response)) {
      swal.fire({ text: 'Thông tin đăng nhập không đúng. Xin vui lòng đăng nhập lại', icon: 'error' })
    } else {
      swal.fire({ text: 'Có lỗi xảy ra. Vui long liên hệ Admin.', icon: 'error' })
    }
  } else {
    swal.fire({ text: 'Có lỗi xảy ra với server. Vui long liên hệ Admin.', icon: 'error' })
  }
  return null;
  // throw error;
});

export default requestInstance;
