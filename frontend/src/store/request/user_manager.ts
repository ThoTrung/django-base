import { ICreateCUser } from 'store/request/user_manager';
import requestInstance from "./base";

export interface IUserPermissions {
  id: number;
  name: string;
  codename: string;
}

export interface IUserGroups {
  id: number;
  name: string;
  permissions: number[];
}

export interface ICreateUserGroup {
  name: string;
  permissions: number[];
}

export const listUserGroups = async () => {
  const res = await requestInstance.get('api/user/groups');
  return res;
}


export const listUserPermissions = async () => {
  const res = await requestInstance.get('api/user/permissions');
  return res;
}

export const createUserGroups = async (param: ICreateUserGroup) => {
  const res = await requestInstance.post('api/user/groups/', param);
  return res;
}

export const updateUserGroups = async (id: number, param: ICreateUserGroup) => {
  const res = await requestInstance.put(`api/user/groups/${id}/`, param);
  return res;
}

export const deleteUserGroups = async (id: number) => {
  const res = await requestInstance.delete(`api/user/groups/${id}/`);
  return res;
}


export interface IFilterCuser {
  name: string,
  group: number,
  status: string,
  full_name: string,
}

export interface ICreateCUser {
  email: string,
  password: string,
  name: string,
  full_name: string,
  gender: string,
  phone_number: string,
  address: string,
  bank: number | null,
  bank_number: string,
  status: string,
  groups: number[],
}

export const DEFAULT_FILTER_USER = {
	name: '',
	group: 0,
	status: '',
	full_name: '',
}

export interface ICUser extends ICreateCUser {
  id: number
}

export interface IUserBanks {
  id: number,
  name: string,
}

export const STATUS_CHOICES:any = {
  W: 'Làm việc',
  S: 'Đã nghỉ',
}

export const GENDER_CHOICES:any = {
  M: 'Nam',
  F: 'Nữ',
}

export const listCUsers = async (params: IFilterCuser = DEFAULT_FILTER_USER) => {
  const res = await requestInstance.get('api/user/cusers', {params: params});
  return res;
}

export const createCusers = async (param: ICreateCUser) => {
  const res = await requestInstance.post('api/user/cusers/', param);
  return res;
}

export const updateCusers = async (id: number, param: ICreateCUser) => {
  const res = await requestInstance.put(`api/user/cusers/${id}/`, param);
  return res;
}

export const deleteCusers = async (id: number) => {
  const res = await requestInstance.delete(`api/user/cusers/${id}/`);
  return res;
}

export const listUserBanks = async () => {
  const res = await requestInstance.get('api/user/banks');
  return res;
}