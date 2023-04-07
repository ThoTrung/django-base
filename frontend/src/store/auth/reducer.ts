import { AnyAction } from 'redux';
import { parseCookies, setCookie, destroyCookie } from 'nookies'

import {
  FETCH_TODO_REQUEST,
  FETCH_TODO_SUCCESS,
  FETCH_TODO_FAILURE,
  LOGIN_REQUEST,
  LOGIN_SUCCESS,
  LOGIN_FAILURE,
} from "./actionTypes";

import {
  TodoActions, TodoState,
  TLoginAction, ILoginState, ILogin
} from "./types";
// import { UserInfo } from 'firebase-admin/lib/auth/user-record';

const cookies = parseCookies();
let token = null;
if (cookies.token) {
  token = JSON.parse(cookies.token);
}

console.log('cookies -----', token);
const initLoginState: ILoginState = {
  pending: false,
  token: token,
  error: null,
}

const initialState: TodoState = {
  pending: false,
  todos: [],
  error: null,
};

const loginReducer = (state=initLoginState, action: TLoginAction) => {
  switch(action.type) {
    case LOGIN_REQUEST:
      console.log('LOGIN_REQUEST');
      return {
        ...state,
        pending: true,
      };
    case LOGIN_SUCCESS:
      console.log('LOGIN_SUCCESS');
      return {
        ...state,
        pending: false,
        token: action.payload.token,
        error: null,
      };
    case LOGIN_FAILURE:
      console.log('LOGIN_FAILURE');
      return {
        ...state,
        pending: false,
        token: null,
        error: action.payload.error
      };
    default:
      return {
        ...state,
      }
  }
}

const todoReducer = (state = initialState, action: TodoActions) => {
  switch (action.type) {
    case FETCH_TODO_REQUEST:
      console.log('FETCH_TODO_REQUEST');
      return {
        ...state,
        pending: true,
      };
    case FETCH_TODO_SUCCESS:
      console.log('FETCH_TODO_SUCCESS');
      return {
        ...state,
        pending: false,
        todos: action.payload.todos,
        error: null,
      };
    case FETCH_TODO_FAILURE:
      console.log('FETCH_TODO_FAILURE');
      return {
        ...state,
        pending: false,
        todos: [],
        error: action.payload.error,
      };
    default:
      return {
        ...state,
      };
  }
};

export interface UserInfo {
  email: string,
  name: string,
}

const UserInfoInitState = {
  email: 'example@gmail.com',
  name: 'example',
}

const layoutUserReducer = (state: UserInfo = UserInfoInitState, action: AnyAction) => {
  switch (action.type) {
    case `GET_USER_INFO`:
      return { ...state, ...action.payload };
    default:
      return state;
  }
}

export { loginReducer };
export default todoReducer;
