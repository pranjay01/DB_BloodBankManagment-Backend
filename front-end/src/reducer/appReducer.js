const defaultState = {
  
  loading: 0,
  snackbarData: [],
  userData: localStorage.loginData
    ? JSON.parse(localStorage.loginData).user
    : null,
    branches:[],
  selectedBranch: null
};

const actionType = {
  ADD_USER_DATA: "ADD_USER_DATA",
  START_LOADING: "START_LOADING",
  STOP_LOADING: "STOP_LOADING",
  ADD_SNACKBAR_DATA: "ADD_SNACKBAR_DATA",
  REMOVE_SNACKBAR_DATA: "REMOVE_SNACKBAR_DATA",
  ADD_BRANCHES: "ADD_BRANCHES",
  RESET_TO_DEFAULT: "RESET_TO_DEFAULT",
  UPDATE_SELECTED_BRANCH: "UPDATE_SELECTED_BRANCH"
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
        snackbarData: [...state.snackbarData, action.payload]
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
    case actionType.RESET_TO_DEFAULT: {
      return { ...defaultState };
    }

    default: {
      return state;
    }
  }
};

export const addUserData = data => {
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


export const updateSelectedBranch = data => {
  return { type: actionType.UPDATE_SELECTED_BRANCH, payload: data };
};

export const addBranches = data => {
  return { type: actionType.ADD_BRANCHES, payload: data };
};
export const resetToDefault = () => {
  return { type: actionType.RESET_TO_DEFAULT };
};

export { appReducer as default };
