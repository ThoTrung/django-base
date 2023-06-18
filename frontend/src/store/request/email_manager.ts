import requestInstance from "./base";

export interface ICreateEmail {
  primary_email: string,
  password: string,
  first_name: string,
  last_name: string,
  phone_number: string,
  // status: string,
}

export interface IEmail extends ICreateEmail {
  id: number,
}

export interface IFilterEmail {
  email: string,
}

export const DEFAULT_FILTER_EMAIL = {
	email: '',
}

export const listEmails = async (params: IFilterEmail = DEFAULT_FILTER_EMAIL) => {
  const res = await requestInstance.get('api/email-manager', {params: params});
  return res;
}

export const createEmails = async (param: ICreateEmail) => {
  const res = await requestInstance.post('api/email-manager/', param);
  return res;
}

export const updateEmails = async (id: number, param: ICreateEmail) => {
  const res = await requestInstance.put(`api/email-manager/${id}/`, param);
  return res;
}

export const deleteEmails = async (id: number) => {
  const res = await requestInstance.delete(`api/email-manager/${id}/`);
  return res;
}

export interface IEmailSetting {
  domain: string;
  max_email: string;
}

export const getEmailSetting = async (owner: number) => {
  const res = await requestInstance.get(`api/email-manager/setting/${owner}`);
  return res;
}