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
  fullName: string,
}

export interface ICreateCuser {
  email: string,
  password: string,
  name: string,
  full_name: string,
  gender: string,
  phone_number: string,
  address: string,
  bank: number,
  bank_number: string,
  status: string,
  groups: number[],
}

export const listCUsers = async (params: IFilterCuser) => {
  const res = await requestInstance.get('api/user/cusers', {params: params});
  return res;
}

export const createCusers = async (param: ICreateCuser) => {
  const res = await requestInstance.post('api/user/cusers/', param);
  return res;
}

export const updateCusers = async (id: number, param: ICreateCuser) => {
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