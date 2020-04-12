import { logoutUser } from "../Routes";
import { addSnackbar } from "../reducer/appReducer";
import store from "../reducer/store";

export const moveIemInArray = (array, oldIndex, newIndex) => {
  if (newIndex >= array.length) {
    newIndex = array.length - 1;
  }
  array.splice(newIndex, 0, array.splice(oldIndex, 1)[0]);
  return array;
};

export const fetchFromObject = (obj, prop) => {
  if (typeof obj === "undefined") {
    return false;
  }
  var _index = prop.indexOf(".");
  if (_index > -1) {
    return this.fetchFromObject(
      obj[prop.substring(0, _index)],
      prop.substr(_index + 1)
    );
  }
  return obj[prop];
};

export const setDeep = (obj, path, value, setrecursively = false) => {
  let level = 0;
  path = path.split(".");
  path.reduce((a, b) => {
    level++;

    if (
      setrecursively &&
      typeof a[b] === "undefined" &&
      level !== path.length
    ) {
      a[b] = {};
      return a[b];
    }

    if (level === path.length) {
      a[b] = value;
      return value;
    } else {
      return a[b];
    }
  }, obj);
  return obj;
};

export const downloadCSVTemplate = (header, name) => {
  // const header = ["email", "password","first_name","last_name", "zipcode", "phone_number"];
  var headerRow = header.join(",");
  var csvContent = "data:text/csv;charset=utf-8,";
  csvContent += headerRow + "\r\n";

  var encodedUri = encodeURI(csvContent);
  var link = document.createElement("a");
  link.setAttribute("href", encodedUri);
  link.setAttribute("download", `${name}.csv`);
  document.body.appendChild(link); // Required for FF

  link.click();
};

export const logoutOnSessionExpired = Error => {
  if (Error.response && Error.response.status === 401) {
    logoutUser();
  }
};
export const handleCatch = Error => {
  if (!Error.response) {
    store.dispatch(
      addSnackbar({ success: false, error: Error.message }, store.dispatch)
    );
  } else if (Error.response && (Error.response.status === 422||Error.response.status===409||Error.response.status===400||Error.response.status===403||Error.response.status===404))
    store.dispatch(addSnackbar(Error.response.data, store.dispatch));
  else if (Error.response && Error.response.status === 401) {
    logoutOnSessionExpired(Error);
  }
};
