import axios from "axios";

//Axios base url configuration

//-----------------------For Development-----------------------//
axios.defaults.baseURL = 'http://ec2-18-219-43-192.us-east-2.compute.amazonaws.com:5000/';

console.log(process.env.API_URL);
export const setAuthorizationTokenInHeader = (token = "") => {
  axios.defaults.headers.common["Authorization"] = `JWT ${token}`; // for all requests
};
