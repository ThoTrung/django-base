import {
  GET_MYINFO_REQUEST,
  GET_MYINFO_SUCCESS,
  GET_MYINFO_FAILURE,
} from "./actionTypes";

export interface IMyInfo {
  id: number,
  email: string,
  name: string,
  full_name: string,
  gender: string,
  phone_number: string,
  address: string,
  bank: number,
  bank_number: string,
  status: string,
  groups: number[],
  permissions: string[],
}

export interface IState {
  pending: boolean,
  error: string | null,
  data: IMyInfo | null,
}

export interface IGetMyInfoSuccessPayload {
  myInfo: IMyInfo;
}
export interface IGetMyInfoFailurePayload {
  error: string;
}

export interface IGetMyInfoRequest {
  type: typeof GET_MYINFO_REQUEST;
}
export interface IGetMyInfoSuccess {
  type: typeof GET_MYINFO_SUCCESS;
  payload: IGetMyInfoSuccessPayload;
}
export interface IGetMyInfoFailure {
  type: typeof GET_MYINFO_FAILURE;
  payload: IGetMyInfoFailurePayload;
}

export type TMyInfoAction = 
  | IGetMyInfoRequest
  | IGetMyInfoSuccess
  | IGetMyInfoFailure
