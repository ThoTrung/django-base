import { AxiosResponse } from 'axios';

export const isSuccessRequest = (res: AxiosResponse<any, any>) => {
  
  return res ? [200, 201, 204].includes(res.status) : false;
}

export const isInvalid = (res: AxiosResponse<any, any>) => {
  return res ? [400, 422].includes(res.status) : false;
}

export const isUnauthenticate = (res: AxiosResponse<any, any>) => {
  return res ? [401].includes(res.status) : false;
}

// export const isError = (res: AxiosResponse<any, any>) => {
//   return [400, 422].includes(res.status);
// }
