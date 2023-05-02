import { all, call, put, takeLatest } from "redux-saga/effects";
import { parseCookies, setCookie, destroyCookie } from 'nookies'
import {LOGIN_SUCCESS, LOGOUT_SUCCESS } from "./actionTypes";
import {
  ILoginSuccess,
} from "./types";

function* requestLoginSuccess(loginSuccessData: ILoginSuccess) {
  try {
    setCookie(null, 'token', JSON.stringify(loginSuccessData.payload.token));
  } catch(e: any) {
    console.log(e.message)
  }
}

function* requestLogoutSuccess() {
  try {
    destroyCookie(null, 'token');
  } catch(e: any) {
    console.log(e.message)
  }
}

function* loginSaga() {
  yield all([takeLatest(LOGIN_SUCCESS, requestLoginSuccess)])
  yield all([takeLatest(LOGOUT_SUCCESS, requestLogoutSuccess)])
}

export default loginSaga;
