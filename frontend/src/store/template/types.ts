import {
  FETCH_TODO_REQUEST,
  FETCH_TODO_SUCCESS,
  FETCH_TODO_FAILURE,
  LOGIN_REQUEST,
  LOGIN_SUCCESS,
  LOGIN_FAILURE,
} from "./actionTypes";

export interface ITodo {
  userId: number;
  id: number;
  title: string;
  completed: boolean;
}

export interface TodoState {
  pending: boolean;
  todos: ITodo[];
  error: string | null;
}

export interface FetchTodoSuccessPayload {
  todos: ITodo[];
}

export interface FetchTodoFailurePayload {
  error: string;
}

export interface FetchTodoRequest {
  type: typeof FETCH_TODO_REQUEST;
}

export type FetchTodoSuccess = {
  type: typeof FETCH_TODO_SUCCESS;
  payload: FetchTodoSuccessPayload;
};

export type FetchTodoFailure = {
  type: typeof FETCH_TODO_FAILURE;
  payload: FetchTodoFailurePayload;
};

export type TodoActions =
  | FetchTodoRequest
  | FetchTodoSuccess
  | FetchTodoFailure;

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
