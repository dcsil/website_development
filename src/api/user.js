import { service } from './utils';

export function UserLogin(username, password) {
  const data = {
    username: username,
    password: password,
  };
  return service.request({
    method: 'post',
    url: `/login/${username}`,
    data,
  });
}

export function UserRegister(username, password) {
  const data = {
    username: username,
    password: password,
  };
  return service.request({
    method: 'put',
    url: `/register/${username}`,
    data,
  });
}

export function GetUser(username) {
  return service.request({
    method: 'get',
    url: `/user/${username}`,
  });
}
