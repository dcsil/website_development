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

export function AddHistory(username) {
  return service.request({
    method: 'post',
    url: `/history/${username}`,
    data,
  });
}

export function ClearHistory(username) {
  return service.request({
    method: 'delete',
    url: `/history/${username}`,
  });
}

export function AddLike(username) {
  return service.request({
    method: 'post',
    url: `/likes/${username}`,
    data,
  });
}

export function RemoveLike(username) {
  return service.request({
    method: 'delete',
    url: `/likes/${username}`,
    data,
  });
}
