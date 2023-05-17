import requestInstance from "./base";

export interface ICreateCustomer {
  code: string,
  name: string,
  email: string,
  expose: string,
  style: string,
  pay_name: string,
  phone_number: string,
  contact_channel: string,
  state: string,
  deadline: string,
  // description: string,
}

export interface ICustomer extends ICreateCustomer {
  id: number,
}

export interface IFilterCustomer {
  name: string,
  email: string,
}

export const listCustomers = async (params: IFilterCustomer) => {
  const res = await requestInstance.get('api/customer-manager', {params: params});
  return res;
}

export const createCustomers = async (param: ICreateCustomer) => {
  const res = await requestInstance.post('api/customer-manager/', param);
  return res;
}

export const updateCustomers = async (id: number, param: ICreateCustomer) => {
  const res = await requestInstance.put(`api/customer-manager/${id}/`, param);
  return res;
}

export const deleteCustomers = async (id: number) => {
  const res = await requestInstance.delete(`api/customer-manager/${id}/`);
  return res;
}
