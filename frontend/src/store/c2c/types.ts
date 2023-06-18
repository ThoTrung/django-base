import {
  SET_CREATE_JOB_DATA,
  DELETE_CREATE_JOB_DATA,
} from "./actionTypes";

export interface ICreateJobData {
  folder_path: string,
  file_number: number,
  files: string[],
}

export interface ISetCreateJobData {
  type: typeof SET_CREATE_JOB_DATA;
  payload: ICreateJobData | null;
}
export interface IDeleteCreateJobData {
  type: typeof DELETE_CREATE_JOB_DATA;
}

export type TData = 
  | ISetCreateJobData
  | IDeleteCreateJobData

export interface IState{
  create_job: ICreateJobData | null,
}