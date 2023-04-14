import { put, PutEffect, select, SelectEffect, takeEvery } from 'redux-saga/effects'
import { menuActiveLinkPartialChange } from 'store/actions'
import { State } from 'store/reducers'
import PAGE from 'config/page.config'
import requestInstance from '../request/base'

export const delay = (ms:number) => new Promise(res => setTimeout(res, ms))

export function* separatingActiveLink(): Generator<SelectEffect | PutEffect, void, string> {
	const activeLink: string = yield select((state: State) => state.menu.activeLink)
	const activeLinkPartial = activeLink?.split(PAGE.menuLinkSeparator) ?? []

	yield put(menuActiveLinkPartialChange(activeLinkPartial))
}

export function* helloSaga() {
  console.log('Hello Sagas!')
}

export function* incrementAsync() {
  yield delay(1000)
  yield put({ type: 'INCREMENT' })
}

export function* watchIncrementAsync() {
  yield takeEvery('INCREMENT_ASYNC', incrementAsync)
}

// export function* login(payload: any) {
//   try {
//     const response = yield call(requestInstance.post, '/api/token', payload);
//     const { token } = response.data;
//     // yield put(loginSuccess(token));
//   } catch (error) {
//     // yield put(loginFailure(error));
//   }
// }

// export default function* authSaga() {
//   yield takeLatest('LOGIN_REQUEST', login);
// }


// post(API_URL, {email: "member1@gmail.com", password: "12345"})
// .then((response) => {
//   console.log(response);
//   return response
// });
