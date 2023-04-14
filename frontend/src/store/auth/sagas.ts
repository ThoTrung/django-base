import { all, call, put, takeLatest } from "redux-saga/effects";
import { parseCookies, setCookie, destroyCookie } from 'nookies'
import {LOGIN_REQUEST, LOGIN_SUCCESS } from "./actionTypes";
import {
  ILogin,
  ILoginRequest,
  ILoginRequestPayload,
  ILoginSuccess,
} from "./types";
import {
  ALoginSuccess,
  ALoginFailure,
} from "./actions";
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
  } catch(e: any) {
    console.log(e.message)
  }
}

function* loginSaga() {
  console.log('loginSaga---');
  yield all([takeLatest(LOGIN_REQUEST, requestLogin)])
  yield all([takeLatest(LOGIN_SUCCESS, requestLoginSuccess)])
}

export default loginSaga;
