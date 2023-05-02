import { AxiosResponse } from 'axios';

export const isSuccessRequest = (res: AxiosResponse<any, any>) => {
  return [200, 201, 204].includes(res.status);
}

export const isInvalid = (res: AxiosResponse<any, any>) => {
  return [400, 422].includes(res.status);
}

export const isUnauthenticate = (res: AxiosResponse<any, any>) => {
  return [401].includes(res.status);
}

// export const isError = (res: AxiosResponse<any, any>) => {
//   return [400, 422].includes(res.status);
// }
