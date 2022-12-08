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

export function ChangeUsername(username, new_name) {
  const data = {
    new_name: new_name,
  };
  return service.request({
    method: 'post',
    url: `/username/${username}`,
    data,
  });
}

export function ChangePassword(username, password) {
  const data = {
    password: password,
  };
  return service.request({
    method: 'post',
    url: `/password/${username}`,
    data,
  });
}

export function AddHistory(username, influ_id) {
  const data = {
    influ_id: influ_id,
  };
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

export function AddLike(username, influ_id) {
  const data = {
    influ_id: influ_id,
  };
  return service.request({
    method: 'post',
    url: `/likes/${username}`,
    data,
  });
}

export function RemoveLike(username, influ_id) {
  const data = {
    influ_id: influ_id,
  };
  return service.request({
    method: 'delete',
    url: `/likes/${username}`,
    data,
  });
}
