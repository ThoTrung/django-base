import axios from "axios";
import { all, call, put, takeLatest } from "redux-saga/effects";
import { parseCookies, setCookie, destroyCookie } from 'nookies'

import {
  fetchTodoFailure,
  fetchTodoSuccess,
  ALoginSuccess,
  ALoginFailure,
} from "./actions";
import { FETCH_TODO_REQUEST, LOGIN_REQUEST, LOGIN_SUCCESS } from "./actionTypes";
import {
  ITodo,
  ILogin,
  ILoginRequest,
  ILoginRequestPayload,
  ILoginSuccess,
} from "./types";
import requestInstance from "../request/base"

const postLogin = (payload: ILoginRequestPayload) => {
  console.log('postLogin', payload)
  return requestInstance.post<ILogin>('api/token/', payload);
}

function* requestLogin(action: ILoginRequest) {
  console.log('action', action)
  try {
    const res = yield call(postLogin, action.payload);
    yield put(
      ALoginSuccess({
        token: res.data
      })
    )
  } catch(e: any) {
    console.log(e.message);
    yield put(
      ALoginFailure({
        error: e.message
      })
    )
  }
}

function* requestLoginSuccess(loginSuccessData: ILoginSuccess) {
  try {
    setCookie(null, 'token', JSON.stringify(loginSuccessData.payload.token));
    // setCookie(null, 'refreshToken', token.refresh);
  } catch(e: any) {
    console.log(e.message)
  }
}

const getTodos = () => {
  axios.get<ITodo[]>("https://jsonplaceholder.typicode.com/todos");
}

/*
  Worker Saga: Fired on FETCH_TODO_REQUEST action
*/
function* fetchTodoSaga() {
  console.log('fetchTodoSaga');
  try {
    const response = yield call(getTodos);
    yield put(
      fetchTodoSuccess({
        todos: response.data,
      })
    );
  } catch (e: any) {
    yield put(
      fetchTodoFailure({
        error: e.message,
      })
    );
  }
}

/*
  Starts worker saga on latest dispatched `FETCH_TODO_REQUEST` action.
  Allows concurrent increments.
*/
function* todoSaga() {
  console.log('todoSaga---')
  yield all([takeLatest(FETCH_TODO_REQUEST, fetchTodoSaga)]);
}

function* loginSaga() {
  console.log('loginSaga---');
  yield all([takeLatest(LOGIN_REQUEST, requestLogin)])
  yield all([takeLatest(LOGIN_SUCCESS, requestLoginSuccess)])
}

export { loginSaga };
export default todoSaga;
