import axios from "axios";
import { AddBranchUrl, GetBranchDetailUrl } from "../../utils/Constants";
import {
  addBranches,
  startLoading,
  stopLoading,
  addSnackbar,
} from "../../reducer/appReducer";
import { handleCatch } from "../../utils/utilityFunctions";

export const addBranch = (data, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = AddBranchUrl.replace(
      ":operator_id",
      getState().auth.loginData.Operator_id
    );

    return axios
      .post(url, data)
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

export const updateBranch = (data, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = AddBranchUrl.replace(
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

export const deleteBranch = (Br_id, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = AddBranchUrl.replace(
      ":operator_id",
      getState().auth.loginData.Operator_id
    );
    return axios
      .delete(`${url}?Br_id=${Br_id}`)
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
export const getBranchList = () => {
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = AddBranchUrl.replace(
      ":operator_id",
      getState().auth.loginData.Operator_id
    );
    return axios
      .get(`${url}?Bbank_id=${getState().auth.loginData.Bbank_id}`)
      .then((response) => {
        dispatch(addBranches(response.data.result));
        dispatch(stopLoading());
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};

export const getbranchInfo = (data, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = GetBranchDetailUrl.replace(
      ":operator_id",
      getState().auth.loginData.Operator_id
    );
    return axios
      .get(`${url}?Br_id=${data.Br_id}`)
      .then((response) => {
        callback(response.data.branch);
        dispatch(stopLoading());
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};
