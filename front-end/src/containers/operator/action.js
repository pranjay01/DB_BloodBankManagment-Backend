import axios from "axios";
import { AddOperatorUrl, UpdateOpeatorUrl } from "../../utils/Constants";
import {
  startLoading,
  stopLoading,
  addSnackbar,
  addAllOperators,
} from "../../reducer/appReducer";
import { handleCatch } from "../../utils/utilityFunctions";

export const addOpeator = (data, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());

    return axios
      .post(`${AddOperatorUrl}`, data)
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

export const updateOperator = (data, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());

    return axios
      .put(`${UpdateOpeatorUrl}`, data)
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

export const deleteOperator = (Operator_id, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());

    return axios
      .delete(`${UpdateOpeatorUrl}?Operator_id=${Operator_id}`)
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

export const getAllOpeators = () => {
  return (dispatch, getState) => {
    dispatch(startLoading());

    return axios
      .get(`${UpdateOpeatorUrl}`)
      .then((response) => {
        dispatch(addAllOperators(response.data.operator_list));
        dispatch(stopLoading());
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};
