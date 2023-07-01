import requestInstance from "./base";


export const apis: any = {
  email_manager: {
    path: 'email-manager'
  }, 
  email_setting: {
    path: 'email-manager/setting'
  }
}


export const listCommon = async (key: string, params: any) => {
  const res = await requestInstance.get(`api/${apis[key].path}`, {params: params});
  return res;
}

export const detailCommon = async (key: string, id: number) => {
  const res = await requestInstance.get(`api/${apis[key].path}/${id}`);
  return res;
}

export const createCommon = async (key: string, param: any) => {
  const res = await requestInstance.post(`api/${apis[key].path}`, param);
  return res;
}

export const updateCommon = async (key: string, id: number, param: any) => {
  const res = await requestInstance.put(`api/${apis[key].path}/${id}/`, param);
  return res;
}

export const deleteCommon = async (key: string, id: number) => {
  const res = await requestInstance.delete(`api/${apis[key].path}/${id}/`);
  return res;
}
