import {
  LOGIN_REQUEST,
  LOGIN_SUCCESS,
  LOGIN_FAILURE,
} from "./actionTypes";
import {
  ILoginSuccessPayload,
  ILoginFailurePayload,
  ILoginRequestPayload,
  ILoginRequest,
  ILoginSuccess,
  ILoginFailure,
} from "./types";

export const ALoginRequest = (payload:ILoginRequestPayload): ILoginRequest => ({
  type: LOGIN_REQUEST,
  payload
})

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
