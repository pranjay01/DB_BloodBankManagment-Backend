import axios from "axios";
import { AddBloodBankUrl } from "../../utils/Constants";
import {
  startLoading,
  stopLoading,
  addSnackbar,
  addBloodBankList,
} from "../../reducer/appReducer";
import { handleCatch } from "../../utils/utilityFunctions";

export const addBloodBank = (data, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());

    return axios
      .post(`${AddBloodBankUrl}`, data)
      .then((response) => {
        dispatch(stopLoading());
        callback && callback();
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};

export const updateBloodBank = (data, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());

    return axios
      .put(`${AddBloodBankUrl}`, data)
      .then((response) => {
        dispatch(stopLoading());
        callback && callback();
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};

export const deleteBloodBank = (Bbank_id, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());

    return axios
      .delete(`${AddBloodBankUrl}?Bbank_id=${Bbank_id}`)
      .then((response) => {
        dispatch(stopLoading());
        callback && callback();
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};

export const getAllBloodBankInfo = () => {
  return (dispatch, getState) => {
    dispatch(startLoading());

    return axios
      .get(`${AddBloodBankUrl}?case=1`)
      .then((response) => {
        dispatch(addBloodBankList(response.data.result));
        dispatch(stopLoading());
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};

export const getBloodBankInfo = (Bbank_id, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());

    return axios
      .get(`${AddBloodBankUrl}?case=2&Bbank_id=${Bbank_id}`)
      .then((response) => {
        callback(response.data.result);
        dispatch(stopLoading());
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};
