import React, { Component } from "react";
import {
  Router,
  Route,
  Switch,
  Link,
  Redirect
} from "react-router-dom";
import { createBrowserHistory } from "history";
import { connect } from "react-redux";
import Loader from "./components/Loader";
import App from './App';
import Login from "./containers/login";
import { logOut } from "./reducer/authReducer";
import { setAuthorizationTokenInHeader } from "./utils/axioConfig";
import store from './reducer/store';
import {resetToDefault} from './reducer/appReducer';
import SnackBar from './containers/snackBar';

export const history = createBrowserHistory();

export const fakeAuth = {
  isAuthenticated: false,
  authenticate(cb) {
    this.isAuthenticated = true;
    setTimeout(cb, 100); // fake async
  },
  signout(cb) {
    this.isAuthenticated = false;
    setTimeout(cb, 100);
  }
};

const PrivateRoute = ({ component: Component, path, ...rest }) => {
  return (
    <Route
      {...rest}
      render={props =>
        fakeAuth.isAuthenticated ? (
          <Component {...props} />
        ) : (
          <Redirect
            to={{
              pathname: `/login`,
              state: { from: props.location }
            }}
          />
        )
      }
    />
  );
};



export const logoutUser = () => {
  localStorage.clear();
  setAuthorizationTokenInHeader();
  fakeAuth.signout(() => {
    store.dispatch(logOut());
    store.dispatch(resetToDefault())
    history.push(`/login`);
  });
};

class Routes extends Component {
  componentDidMount() {
    if (this.props.auth.loginData) {
      setAuthorizationTokenInHeader(this.props.auth.loginData.access_token);
      fakeAuth.authenticate(() => {});
    }
  }

  render() {
    return (
      <div className="App">
        <Router history={history}>
          {this.props.loading > 0 && <Loader />}
          <SnackBar/>
          <div className={`main-container`}>
            <Switch>
              <PrivateRoute path={`/`} component={App} exact={true} />
              <Route path={`/login`} component={Login} />
              <PrivateRoute path={`/app`} component={App} />
              <Route component={PageNotFound} />
            </Switch>
          </div>
        </Router>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    auth: state.auth,
    loading: state.app.loading
  };
};

const mapDispatchToProps = dispatch => {
  return {
    logOut: () => {
      dispatch(logOut());
    }
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Routes);

const PageNotFound = props => {
  return (
    <div>
      Page Not Found
      <Link to={`/`}>To Home</Link>
      <Link to={`/login`}>To Login</Link>
    </div>
  );
};
