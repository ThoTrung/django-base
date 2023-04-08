import { parseCookies, setCookie, destroyCookie } from 'nookies'
import {
  LOGIN_REQUEST,
  LOGIN_SUCCESS,
  LOGIN_FAILURE,
} from "./actionTypes";

import {
  TLoginAction, ILoginState
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
// const layoutUserReducer = (state: UserInfo = UserInfoInitState, action: AnyAction) => {
//   switch (action.type) {
//     case `GET_USER_INFO`:
//       return { ...state, ...action.payload };
//     default:
//       return state;
//   }
// }

export default loginReducer;
