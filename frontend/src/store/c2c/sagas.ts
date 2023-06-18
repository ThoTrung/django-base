import { all, call, put, takeLatest } from "redux-saga/effects";
import { SET_CREATE_JOB_DATA, DELETE_CREATE_JOB_DATA } from "./actionTypes";
import { ASetCreateJobData, ADeleteCreateJobData } from "./actions";
import { ICreateJobData } from "./types";


function* requestSetCreatJobData() {
    yield put(ASetCreateJobData(null))
}
function* requestDeleteCreateJobData() {
    yield put(ADeleteCreateJobData())
}

function* c2cSaga() {
  yield all([takeLatest(SET_CREATE_JOB_DATA, requestSetCreatJobData)]);
  yield all([takeLatest(DELETE_CREATE_JOB_DATA, requestDeleteCreateJobData)]);
}

export default c2cSaga;
