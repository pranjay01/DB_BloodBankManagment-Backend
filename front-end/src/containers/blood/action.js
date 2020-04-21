import axios from "axios";
import {
  AddBloodUnitUrl,
  ExpiredBloodUnitUrl,
  BloodLimitUrl,
  GuestBloodUnitUrl,
} from "../../utils/Constants";
import {
  startLoading,
  stopLoading,
  addSnackbar,
  addBloodCountForBloodBank,
  addBloodCountForBranch,
  addBloodCountForBloodGroup,
  addBloodCountandBloodBankName,
  addExpiredBloodUnitList,
  addBloodBanksUnitsCountForGuest,
  addBloodBankBranchesUnitsCountForGuest,
  addBranchBloodGroupUnitsCountForGuest,
} from "../../reducer/appReducer";
import { handleCatch } from "../../utils/utilityFunctions";

export const addBloodUnit = (data, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = AddBloodUnitUrl.replace(
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

export const getBloodCountForBloodBank = (Bbank_id) => {
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = AddBloodUnitUrl.replace(
      ":operator_id",
      getState().auth.loginData.Operator_id
    );

    if (!Bbank_id) {
      Bbank_id = getState().auth.loginData.Bbank_id;
    }

    return axios
      .get(`${url}?case=1&Bbank_id=${Bbank_id}`)
      .then((response) => {
        dispatch(addBloodCountForBloodBank(response.data.result));
        dispatch(stopLoading());
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};

export const getBloodCountForBranch = (Br_id) => {
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = AddBloodUnitUrl.replace(
      ":operator_id",
      getState().auth.loginData.Operator_id
    );

    return axios
      .get(`${url}?case=2&Br_id=${Br_id}`)
      .then((response) => {
        dispatch(addBloodCountForBranch(response.data.result));
        dispatch(stopLoading());
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};

export const getBloodCountForBranchForBloodGroup = (Br_id, Blood_Group) => {
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = AddBloodUnitUrl.replace(
      ":operator_id",
      getState().auth.loginData.Operator_id
    );

    return axios
      .get(`${url}?case=3&Br_id=${Br_id}&Blood_Group=${Blood_Group}`)
      .then((response) => {
        dispatch(addBloodCountForBloodGroup(response.data.result));
        dispatch(stopLoading());
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};

export const getBloodcountAndBloodBankName = (Bbank_id) => {
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = AddBloodUnitUrl.replace(
      ":operator_id",
      getState().auth.loginData.Operator_id
    );

    if (!Bbank_id) {
      Bbank_id = getState().auth.loginData.Bbank_id;
    }
    return axios
      .get(`${url}?case=4&Bbank_id=${Bbank_id}`)
      .then((response) => {
        dispatch(addBloodCountandBloodBankName(response.data.result));
        dispatch(stopLoading());
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};

export const updateBloodUnit = (data, callback) => {
  data.Case = 1;
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = AddBloodUnitUrl.replace(
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

export const moveBlood = (data, callback) => {
  data.Case = 2;
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = AddBloodUnitUrl.replace(
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

export const deleteBloodUnit = (Br_id, Blood_id, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = AddBloodUnitUrl.replace(
      ":operator_id",
      getState().auth.loginData.Operator_id
    );

    return axios
      .delete(`${url}?case=2&Br_id=${Br_id}&Blood_id=${Blood_id}`)
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

export const getExpiredBloodUnitInBloodBank = (Bbank_id) => {
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = ExpiredBloodUnitUrl.replace(
      ":operator_id",
      getState().auth.loginData.Operator_id
    );

    if (!Bbank_id) {
      Bbank_id = getState().auth.loginData.Bbank_id;
    }
    return axios
      .get(`${url}?Bbank_id=${Bbank_id}`)
      .then((response) => {
        dispatch(addExpiredBloodUnitList(response.data.result));
        dispatch(stopLoading());
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};

export const deleteExpiredBloodUnitInBloodBank = (Bbank_id, callback) => {
  return (dispatch, getState) => {
    dispatch(startLoading());
    const url = ExpiredBloodUnitUrl.replace(
      ":operator_id",
      getState().auth.loginData.Operator_id
    );
    if (!Bbank_id) {
      Bbank_id = getState().auth.loginData.Bbank_id;
    }
    return axios
      .delete(`${url}?Bbank_id=${Bbank_id}`)

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



export const getBloodCountByBloodBankForGuest = () => {
  return (dispatch, getState) => {
    dispatch(startLoading());
    return axios
      .get(`${GuestBloodUnitUrl}?case=1`)
      .then((response) => {
        dispatch(addBloodBanksUnitsCountForGuest(response.data.result));
        dispatch(stopLoading());
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};
export const getBloodCountForBloodBankForGuest = (Bbank_id) => {
  return (dispatch, getState) => {
    dispatch(startLoading());

    return axios
      .get(`${GuestBloodUnitUrl}?case=2&Bbank_id=${Bbank_id}`)
      .then((response) => {
        dispatch(addBloodBankBranchesUnitsCountForGuest(response.data.result));
        dispatch(stopLoading());
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};

export const getBloodCountForBranchForGuest = (Br_id) => {
  return (dispatch, getState) => {
    dispatch(startLoading());

    return axios
      .get(`${GuestBloodUnitUrl}?case=3&Br_id=${Br_id}`)
      .then((response) => {
        dispatch(addBranchBloodGroupUnitsCountForGuest(response.data.result));
        dispatch(stopLoading());
      })
      .catch((e) => {
        dispatch(stopLoading());
        handleCatch(e);
      });
  };
};
