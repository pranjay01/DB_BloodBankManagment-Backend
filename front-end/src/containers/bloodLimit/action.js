import axios from "axios";
import { BloodLimitUrl } from "../../utils/Constants";
import {
  startLoading,
  stopLoading,
  addSnackbar,
  addBloodLimit,
} from "../../reducer/appReducer";
import { handleCatch } from "../../utils/utilityFunctions";
export const getBloodLimit = () => {
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = BloodLimitUrl.replace(
      ":operator_id",
      getState().auth.loginData.Operator_id
    );

    return axios
      .get(`${url}?Bbank_id=${getState().auth.loginData.Bbank_id}`)
      .then((response) => {
        dispatch(addBloodLimit(response.data.list));
        dispatch(stopLoading());
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};
export const updateBloodLimit = (data, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = BloodLimitUrl.replace(
      ":operator_id",
      getState().auth.loginData.Operator_id
    );

    return axios
      .put(url, data)
      .then((response) => {
        dispatch(
          addSnackbar({ success: true, error: response.data.message }, dispatch)
        );
        dispatch(stopLoading());
        callback && callback();
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};
