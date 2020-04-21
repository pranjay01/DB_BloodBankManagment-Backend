import axios from "axios";
import {
  AddDonorUrl,
  UpdateDonorUrl,
  DeleteDonorUrl,
  GetDonorByEmailIdUrl,
} from "../../utils/Constants";
import {
  startLoading,
  stopLoading,
  addSnackbar,
  addSearchDonorList,
} from "../../reducer/appReducer";
import { handleCatch } from "../../utils/utilityFunctions";

export const addDonor = (data, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());

    return axios
      .post(`${AddDonorUrl}`, data)
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

export const updateDonor = (data, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());

    return axios
      .put(`${UpdateDonorUrl}`, data)
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

export const deleteDonor = (data, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());

    return axios
      .delete(
        `${DeleteDonorUrl}?Donor_id=${data.Donor_id}&Operator_id=${
          getState().auth.loginData.Operator_id
        }&Bbank_id=${data.Bbank_id || getState().auth.loginData.Bbank_id}`
      )
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

export const getDonorByEmailId = (data) => {
  return (dispatch, getState) => {
    dispatch(startLoading());

    return axios
      .get(`${GetDonorByEmailIdUrl}?Email_id=${data.Email_id}`)
      .then((response) => {
        debugger;
        
        dispatch(addSearchDonorList(response.data.message));
        dispatch(stopLoading());
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};
