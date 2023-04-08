import {
  FETCH_TODO_REQUEST,
  FETCH_TODO_FAILURE,
  FETCH_TODO_SUCCESS,
  LOGIN_REQUEST,
  LOGIN_SUCCESS,
  LOGIN_FAILURE,
} from "./actionTypes";
import {
  FetchTodoRequest,
  FetchTodoSuccess,
  FetchTodoSuccessPayload,
  FetchTodoFailure,
  FetchTodoFailurePayload,
  ILoginSuccessPayload,
  ILoginFailurePayload,
  ILoginRequestPayload,
  ILoginRequest,
  ILoginSuccess,
  ILoginFailure,
} from "./types";

export const fetchTodoRequest = (): FetchTodoRequest => ({
  type: FETCH_TODO_REQUEST,
});

export const fetchTodoSuccess = (
  payload: FetchTodoSuccessPayload
): FetchTodoSuccess => ({
  type: FETCH_TODO_SUCCESS,
  payload,
});

export const fetchTodoFailure = (
  payload: FetchTodoFailurePayload
): FetchTodoFailure => ({
  type: FETCH_TODO_FAILURE,
  payload,
});

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
