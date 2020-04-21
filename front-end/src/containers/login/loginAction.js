import axios from "axios";
import { addLoginData } from "../../reducer/authReducer";
import {
  startLoading,
  stopLoading,
  addUserData,
} from "../../reducer/appReducer";
import { LoginUrl } from "../../utils/Constants";
import { setAuthorizationTokenInHeader } from "../../utils/axioConfig";
import { handleCatch } from "../../utils/utilityFunctions";
// import {getUserData} from '../CommonActions';
export const login = (data, callback) => {
  const loginDetail = { Email: data.email, Password: data.password };
  return (dispatch, getState) => {
    dispatch(startLoading());
    return axios
      .post(LoginUrl, loginDetail)
      .then(async (response) => {
        localStorage.setItem("loginData", JSON.stringify(response.data));
        await setAuthorizationTokenInHeader(response.data.access_token);
        dispatch(addLoginData(response.data));
        //dispatch(addUserData(response.data.user));
        dispatch(stopLoading());
        //  dispatch(getUserData())
        return callback();
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};
