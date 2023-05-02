import { all, call, put, takeLatest } from "redux-saga/effects";
import { SHOW_LOADING, HIDE_LOADING } from "./actionTypes";
import { AShowLoading, AHideLoading } from "./actions";


function* requestShowLoading() {
    yield put(AShowLoading())
}
function* requestHideLoading() {
    yield put(AShowLoading())
}

function* commonSaga() {
  yield all([takeLatest(SHOW_LOADING, requestShowLoading)]);
  yield all([takeLatest(HIDE_LOADING, requestHideLoading)]);
}

export default commonSaga;
