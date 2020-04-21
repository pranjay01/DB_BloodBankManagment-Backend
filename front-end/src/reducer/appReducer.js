const defaultState = {
  loading: 0,
  snackbarData: [],
  userData: localStorage.loginData
    ? JSON.parse(localStorage.loginData).user
    : null,
  branches: [],
  selectedBranch: null,
  bloodCountForBloodBank: [],
  bloodCountForBranch: [],
  bloodUnitsForBloodGroup: [],
  bloodBankCountAndBloodBankName: null,
  expiredBloodUnits: [],
  bloodBanksUnitForGuest: [],
  bloodBankBranchesUnitsForGuest: [],
  branchBloodGroupUnitsForGuest: [],
  allOperators: [],
  bloodBankList: [],
  allEvents: [],
  searchDonor: null,
  bloodLimit: [],
};

const actionType = {
  ADD_USER_DATA: "ADD_USER_DATA",
  START_LOADING: "START_LOADING",
  STOP_LOADING: "STOP_LOADING",
  ADD_SNACKBAR_DATA: "ADD_SNACKBAR_DATA",
  REMOVE_SNACKBAR_DATA: "REMOVE_SNACKBAR_DATA",
  ADD_BRANCHES: "ADD_BRANCHES",
  RESET_TO_DEFAULT: "RESET_TO_DEFAULT",
  UPDATE_SELECTED_BRANCH: "UPDATE_SELECTED_BRANCH",
  ADD_BLOOD_COUNT_FOR_BLODD_BANK: "ADD_BLOOD_COUNT_FOR_BLODD_BANK",
  ADD_BLOOD_COUNT_FOR_BRANCH: "ADD_BLOOD_COUNT_FOR_BRANCH",
  ADD_BLOOD_UNITS_FOR_BLOOD_GROUP: "ADD_BLOOD_UNITS_FOR_BLOOD_GROUP",
  ADD_BLOOD_COUNT_AND_BLOOD_BANK_NAME: "ADD_BLOOD_COUNT_AND_BLOOD_BANK_NAME",
  ADD_EXPIRED_BLOOD_UNITS: "ADD_EXPIRED_BLOOD_UNITS",
  ADD_BLOOD_BANKS_UNITS_COUNT_FOR_GUEST:
    "ADD_BLOOD_BANKS_UNITS_COUNT_FOR_GUEST",
  ADD_BLOOD_BANK_BRANCH_UNITS_COUNT_FOR_GUEST:
    "ADD_BLOOD_BANK_BRANCH_UNITS_COUNT_FOR_GUEST",
  ADD_BRANCH_BLOOD_GROUP_UNITS_COUNT_FOR_GUEST:
    "ADD_BRANCH_BLOOD_GROUP_UNITS_COUNT_FOR_GUEST",
  ADD_ALL_OPERATORS: "ADD_ALL_OPERATORS",
  ADD_BLOOD_BANK_LIST: "ADD_BLOOD_BANK_LIST",
  ADD_ALL_EVENTS: "ADD_ALL_EVENTS",
  ADD_SEARCH_DONOR_LIST: "ADD_SEARCH_DONOR_LIST",
  ADD_BLOOD_LIMIT: "ADD_BLOOD_LIMIT",
};

const appReducer = (state = defaultState, action) => {
  switch (action.type) {
    case actionType.ADD_USER_DATA: {
      return { ...state, userData: action.payload };
    }
    case actionType.START_LOADING: {
      return { ...state, loading: state.loading + 1 };
    }
    case actionType.STOP_LOADING: {
      return { ...state, loading: state.loading - 1 };
    }
    case actionType.ADD_SNACKBAR_DATA: {
      return {
        ...state,
        snackbarData: [...state.snackbarData, action.payload],
      };
    }
    case actionType.REMOVE_SNACKBAR_DATA: {
      let snackbarData = [...state.snackbarData];
      snackbarData.splice(0, 1);
      return { ...state, snackbarData };
    }
    case actionType.UPDATE_SELECTED_BRANCH: {
      return {
        ...state,
        selectedBranch: action.payload,
      };
    }
    case actionType.ADD_BRANCHES: {
      return { ...state, branches: action.payload };
    }
    case actionType.ADD_BLOOD_COUNT_FOR_BLODD_BANK: {
      return { ...state, bloodCountForBloodBank: action.payload };
    }
    case actionType.ADD_BLOOD_COUNT_FOR_BRANCH: {
      return { ...state, bloodCountForBranch: action.payload };
    }
    case actionType.ADD_BLOOD_UNITS_FOR_BLOOD_GROUP: {
      return { ...state, bloodUnitsForBloodGroup: action.payload };
    }
    case actionType.ADD_EXPIRED_BLOOD_UNITS: {
      return { ...state, expiredBloodUnits: action.payload };
    }
    case actionType.ADD_BLOOD_BANKS_UNITS_COUNT_FOR_GUEST: {
      return { ...state, bloodBanksUnitForGuest: action.payload };
    }
    case actionType.ADD_BLOOD_BANK_BRANCH_UNITS_COUNT_FOR_GUEST: {
      return { ...state, bloodBankBranchesUnitsForGuest: action.payload };
    }
    case actionType.ADD_BRANCH_BLOOD_GROUP_UNITS_COUNT_FOR_GUEST: {
      return { ...state, branchBloodGroupUnitsForGuest: action.payload };
    }
    case actionType.ADD_BLOOD_COUNT_AND_BLOOD_BANK_NAME: {
      return { ...state, bloodBankCountAndBloodBankName: action.payload };
    }
    case actionType.ADD_ALL_OPERATORS: {
      return { ...state, allOperators: action.payload };
    }
    case actionType.ADD_BLOOD_BANK_LIST: {
      return { ...state, bloodBankList: action.payload };
    }
    case actionType.ADD_SEARCH_DONOR_LIST: {
      return { ...state, searchDonor: action.payload };
    }
    case actionType.ADD_ALL_EVENTS: {
      return { ...state, allEvents: action.payload };
    }
    case actionType.ADD_BLOOD_LIMIT: {
      return { ...state, bloodLimit: action.payload };
    }
    case actionType.RESET_TO_DEFAULT: {
      return { ...defaultState };
    }

    default: {
      return state;
    }
  }
};

export const addUserData = (data) => {
  return { type: actionType.ADD_USER_DATA, payload: data };
};
export const startLoading = () => {
  return { type: actionType.START_LOADING };
};
export const stopLoading = () => {
  return { type: actionType.STOP_LOADING };
};
export const addSnackbar = (message, dispatch) => {
  setTimeout(() => {
    dispatch(removeSnackbar());
  }, 3000);
  return { type: actionType.ADD_SNACKBAR_DATA, payload: message };
};

const removeSnackbar = () => {
  return { type: actionType.REMOVE_SNACKBAR_DATA };
};

export const updateSelectedBranch = (data) => {
  return { type: actionType.UPDATE_SELECTED_BRANCH, payload: data };
};

export const addBranches = (data) => {
  return { type: actionType.ADD_BRANCHES, payload: data };
};

export const addBloodCountForBloodBank = (data) => {
  return { type: actionType.ADD_BLOOD_COUNT_FOR_BLODD_BANK, payload: data };
};

export const addBloodCountForBranch = (data) => {
  return { type: actionType.ADD_BLOOD_COUNT_FOR_BRANCH, payload: data };
};
export const addExpiredBloodUnitList = (data) => {
  return { type: actionType.ADD_EXPIRED_BLOOD_UNITS, payload: data };
};
export const addBloodCountForBloodGroup = (data) => {
  return { type: actionType.ADD_BLOOD_UNITS_FOR_BLOOD_GROUP, payload: data };
};
export const addBloodCountandBloodBankName = (data) => {
  return {
    type: actionType.ADD_BLOOD_COUNT_AND_BLOOD_BANK_NAME,
    payload: data,
  };
};

export const addBloodBanksUnitsCountForGuest = (data) => {
  return {
    type: actionType.ADD_BLOOD_BANKS_UNITS_COUNT_FOR_GUEST,
    payload: data,
  };
};
export const addBloodBankBranchesUnitsCountForGuest = (data) => {
  return {
    type: actionType.ADD_BLOOD_BANK_BRANCH_UNITS_COUNT_FOR_GUEST,
    payload: data,
  };
};

export const addBranchBloodGroupUnitsCountForGuest = (data) => {
  return {
    type: actionType.ADD_BRANCH_BLOOD_GROUP_UNITS_COUNT_FOR_GUEST,
    payload: data,
  };
};
export const addAllOperators = (data) => {
  return { type: actionType.ADD_ALL_OPERATORS, payload: data };
};
export const addBloodBankList = (data) => {
  return { type: actionType.ADD_BLOOD_BANK_LIST, payload: data };
};

export const addAllEvents = (data) => {
  return { type: actionType.ADD_ALL_EVENTS, payload: data };
};
export const addSearchDonorList = (data) => {
  return { type: actionType.ADD_SEARCH_DONOR_LIST, payload: data };
};
export const addBloodLimit = (data) => {
  return { type: actionType.ADD_BLOOD_LIMIT, payload: data };
};
export const resetToDefault = () => {
  return { type: actionType.RESET_TO_DEFAULT };
};

export { appReducer as default };
