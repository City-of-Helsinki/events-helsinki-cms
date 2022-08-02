/* eslint-disable */
import { sleep } from 'k6';
import http from 'k6/http';

export const options = {
  duration: '10m',
  vus: 50,
  //  vus: 1,
  thresholds: {
    //avg is around ?200ms? on https://cms.test.kuva.hel.ninja/api/collections/
    http_req_duration: ['p(95)<5000'],
  },
};

export default () => {
  const url = 'https://cms.test.kuva.hel.ninja/api/collections/';
  const res = http.get(url);

  //10 loads per minute
  sleep(6);
};
