import {
  SET_CREATE_JOB_DATA,
  DELETE_CREATE_JOB_DATA,
} from './actionTypes'

import {
  ISetCreateJobData,
  IDeleteCreateJobData,
  ICreateJobData,
} from "./types"

export const ASetCreateJobData = (payload: ICreateJobData | null): ISetCreateJobData => ({
  type: SET_CREATE_JOB_DATA,
  payload
})

export const ADeleteCreateJobData = (): IDeleteCreateJobData => ({
  type: DELETE_CREATE_JOB_DATA,
})
