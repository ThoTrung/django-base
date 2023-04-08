import {
  GET_MYINFO_REQUEST,
  GET_MYINFO_SUCCESS,
  GET_MYINFO_FAILURE,
} from './actionTypes'

import {
  IGetMyInfoSuccessPayload,
  IGetMyInfoFailurePayload,
  IGetMyInfoRequest,
  IGetMyInfoSuccess,
  IGetMyInfoFailure,
} from "./types"

export const AMyInfoRequest = (): IGetMyInfoRequest => ({
  type: GET_MYINFO_REQUEST,
})

export const AMyInfoSuccess = (payload: IGetMyInfoSuccessPayload): IGetMyInfoSuccess  => ({
  type: GET_MYINFO_SUCCESS,
  payload
})

export const AMyInfoFailure = (payload: IGetMyInfoFailurePayload): IGetMyInfoFailure => ({
  type: GET_MYINFO_FAILURE,
  payload,
})
