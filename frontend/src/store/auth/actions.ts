import {
  LOGIN_SUCCESS,
  LOGIN_FAILURE,
  LOGOUT_SUCCESS,
} from "./actionTypes";
import {
  ILoginSuccessPayload,
  ILoginFailurePayload,
  ILoginSuccess,
  ILoginFailure,
  ILogoutSuccess,
} from "./types";


export const ALoginSuccess = (
  payload: ILoginSuccessPayload
): ILoginSuccess => ({
  type: LOGIN_SUCCESS,
  payload,
});

export const ALoginFailure = (
  payload: ILoginFailurePayload
): ILoginFailure => ({
  type: LOGIN_FAILURE,
  payload,
});

export const ALogoutSuccess = (): ILogoutSuccess => ({
  type: LOGOUT_SUCCESS,
});
