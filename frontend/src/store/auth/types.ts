import {
  LOGIN_REQUEST,
  LOGIN_SUCCESS,
  LOGIN_FAILURE,
} from "./actionTypes";

export interface ILogin {
  refresh: string;
  access: string;
}

export interface ILoginState {
  pending: boolean;
  token: ILogin | null;
  error: string | null;
}

export interface ILoginRequestPayload {
  email: string;
  password: string;
}

export interface ILoginSuccessPayload {
  token: ILogin;
}

export interface ILoginFailurePayload {
  error: string;
}

export interface ILoginRequest {
  type: typeof LOGIN_REQUEST;
  payload: ILoginRequestPayload;
}

export type ILoginSuccess = {
  type: typeof LOGIN_SUCCESS;
  payload: ILoginSuccessPayload;
}

export type ILoginFailure = {
  type: typeof LOGIN_FAILURE;
  payload: ILoginFailurePayload;
}

export type TLoginAction =
  | ILoginRequest
  | ILoginSuccess
  | ILoginFailure;
