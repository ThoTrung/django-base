import { takeEvery, all, fork } from 'redux-saga/effects'
import { separatingActiveLink, helloSaga, watchIncrementAsync } from './menuSaga'
import todoSaga from "../reducers/todo/sagas";


// function* rootSaga() {
// 	yield takeEvery('MENU_ACTIVE_LINK_CHANGE', separatingActiveLink)
// 	yield all([helloSaga(), watchIncrementAsync()])
// }

export function* rootSaga() {
  yield all([fork(todoSaga)]);
}

export default rootSaga
