import { service } from './utils';

export function GetInfluencer(id) {
  return service.request({
    method: 'get',
    url: `/influencer/${id}`,
  });
}

export function GetInfluencerByTag(tag) {
  return service.request({
    method: 'get',
    url: `/tag/${tag}`,
  });
}
