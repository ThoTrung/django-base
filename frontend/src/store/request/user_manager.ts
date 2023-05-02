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

