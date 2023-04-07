import { takeEvery, all, fork } from 'redux-saga/effects'
import { separatingActiveLink, helloSaga, watchIncrementAsync } from './menuSaga'
import todoSaga, { loginSaga } from "../auth/sagas";


// function* rootSaga() {
// 	yield takeEvery('MENU_ACTIVE_LINK_CHANGE', separatingActiveLink)
// 	yield all([helloSaga(), watchIncrementAsync()])
// }

function* rootSaga() {
  yield all([loginSaga()]);
}

export default rootSaga
