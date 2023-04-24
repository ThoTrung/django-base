import requestInstance from "./base";

export interface IListFolderFromDisk {
  driverPath: string;
  dropboxPath: string;
  startTime: string;
  endTime: string;
}

export interface IOneFolder {
  path: string;
  lastModifiedFolder: string;
  files: string[];
}

export interface ISettingSearchFolder {
  subkey: string;
  value: string;
}

export const listFolderFromDisk = async (params: IListFolderFromDisk) => {
  const res = await requestInstance.get('api/job-managers/list-folder-from-disk', {params});
  return res;
}
export const listSpecifyFolderFromDisk = async (params: IListFolderFromDisk) => {
  const res = await requestInstance.get('api/job-managers/list-specify-folder-from-disk', {params});
  return res;
}


export const getSearchFolderSetting = () => {
  const res = requestInstance.get('api/job-managers/search-folder-setting', {});
  return res;
}


export const putSearchFolderSetting = async (params: ISettingSearchFolder) => {
  const res = await requestInstance.put('api/job-managers/search-folder-setting', params);
  return res;
}
