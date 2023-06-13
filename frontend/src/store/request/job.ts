import requestInstance from "./base";

export interface ICreateJob {
  folder_path: string,
  name: string,
  customer: string,
  files: string,
  file_number: number,
  expose: string,
  style: string,
  note: string,
  deadline: string,
  number_sub_job: number,
  editor: string,
  customer_price: string,
  editor_price: string,
}

export interface IJob extends ICreateJob {
  id: number,
}

// export interface IFilterCustomer {
//   name: string,
//   email: string,
// }

// export const listCustomers = async (params: IFilterCustomer) => {
//   const res = await requestInstance.get('api/job', {params: params});
//   return res;
// }

export const createJob = async (param: ICreateJob) => {
  const res = await requestInstance.post('api/job-managers/job/', param);
  return res;z``
}

export const updateJob = async (id: number, param: ICreateJob) => {
  const res = await requestInstance.put(`api/job-managers/job/${id}/`, param);
  return res;
}

// export const deleteCustomers = async (id: number) => {
//   const res = await requestInstance.delete(`api/job/${id}/`);
//   return res;
// }
