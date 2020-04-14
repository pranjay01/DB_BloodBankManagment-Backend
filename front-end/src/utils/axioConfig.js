import axios from "axios";

//Axios base url configuration

//-----------------------For Development-----------------------//
axios.defaults.baseURL = "http://test.com/v1/";


export const setAuthorizationTokenInHeader = (token = "") => {
  axios.defaults.headers.common["Authorization"] = `bearer ${token}`; // for all requests
};
