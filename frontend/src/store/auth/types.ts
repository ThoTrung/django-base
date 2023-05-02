import {
  LOGIN_SUCCESS,
  LOGIN_FAILURE,
  LOGOUT_SUCCESS,
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

export interface ILoginSuccessPayload {
  token: ILogin;
}

export interface ILoginFailurePayload {
  error: string;
}

export type ILoginSuccess = {
  type: typeof LOGIN_SUCCESS;
  payload: ILoginSuccessPayload;
}

export type ILoginFailure = {
  type: typeof LOGIN_FAILURE;
  payload: ILoginFailurePayload;
}

export type ILogoutSuccess = {
  type: typeof LOGOUT_SUCCESS;
}
export type TLoginAction =
  | ILoginSuccess
  | ILogoutSuccess
  | ILoginFailure;
