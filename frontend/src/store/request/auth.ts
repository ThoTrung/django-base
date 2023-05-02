import requestInstance from "./base";

export interface ILoginRequestPayload {
  email: string;
  password: string;
}

export const postLogin = async (payload: ILoginRequestPayload) => {
  // console.log('postLogin', payload)
  const res = requestInstance.post('api/token/', payload);
  return res;
}

