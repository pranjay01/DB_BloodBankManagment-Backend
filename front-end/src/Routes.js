import React, { Component } from "react";
import { Router, Route, Switch, Link, Redirect } from "react-router-dom";
import { createBrowserHistory } from "history";
import { connect } from "react-redux";
import Loader from "./components/Loader";
import App from "./App";
import Dashboard from "./containers/dashboard";
import Login from "./containers/login";
import { logOut } from "./reducer/authReducer";
import { setAuthorizationTokenInHeader } from "./utils/axioConfig";
import store from "./reducer/store";
import { resetToDefault } from "./reducer/appReducer";
import SnackBar from "./containers/snackBar";

import BranchList from "./containers/branch/BranchList";

import SearchDonor from "./containers/donor/SearchDonor";

import BloodCountForBranch from "./containers/blood/BloodCountForBranch";
import BloodUnitListForBranchForBloodGroup from "./containers/blood/BloodUnitListForBranchForBloodGroup";
import MoveBlood from "./containers/blood/MoveBlood";
import ExpiredBloodUnitList from "./containers/blood/ExpiredBloodUnitList";
import Guest from "./containers/blood/Guest";
import BloodBankList from "./containers/bloodbank/BloodBankList";
import UpdateBloodBank from "./containers/bloodbank/UpdateBloodBank";
import AddBloodBank from "./containers/bloodbank/AddBloodBank";
import AddBranch from "./containers/branch/AddBranch";
import UpdateBranch from "./containers/branch/UpdateBranch";
import AddOperator from "./containers/operator/AddOperator";
import UpdateOperator from "./containers/operator/UpdateOperator";
import OperatorList from "./containers/operator/OperatorList";
import AddDonor from "./containers/donor/AddDonor";
import UpdateDonor from "./containers/donor/UpdateDonor";
import EventList from "./containers/event/EventList";
import UpdateEvent from "./containers/event/UpdateEvent";
import AddEvent from "./containers/event/AddEvent";
import BloodLimitList from "./containers/bloodLimit/BloodLimitList";
import UpdateBloodLimit from "./containers/bloodLimit/UpdateBloodLimit";

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
  },
};

const PrivateRoute = ({ component: Component, path, ...rest }) => {
  return (
    <Route
      {...rest}
      render={(props) =>
        fakeAuth.isAuthenticated ? (
          <Component {...props} />
        ) : (
          <Redirect
            to={{
              pathname: `/login`,
              state: { from: props.location },
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
    store.dispatch(resetToDefault());
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
          {this.props.auth &&
            this.props.auth.loginData &&
            this.props.auth.loginData.access_token && (
              <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <button
                  class="navbar-toggler"
                  type="button"
                  data-toggle="collapse"
                  data-target="#navbarNav"
                  aria-controls="navbarNav"
                  aria-expanded="false"
                  aria-label="Toggle navigation"
                >
                  <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                  <ul class="navbar-nav">
                    <li
                      class="nav-item"
                      onClick={() => {
                        history.push("/Dashboard");
                      }}
                    >
                      <a class="nav-link" href="#">
                        Home <span class="sr-only">(current)</span>
                      </a>
                    </li>
                    <li
                      class="nav-item"
                      onClick={() => {
                        history.push("/");
                      }}
                    >
                      <a class="nav-link" href="#">
                        Guest
                      </a>
                    </li>

                    <li
                      class="nav-item"
                      onClick={() => {
                        history.push(`/ListBranch`);
                      }}
                    >
                      <a class="nav-link" href="#">
                        Branch List
                      </a>
                    </li>
                    <li
                      class="nav-item"
                      onClick={() => {
                        history.push(`/ListOperator`);
                      }}
                    >
                      <a class="nav-link" href="#">
                        Operator List
                      </a>
                    </li>
                    <li
                      class="nav-item"
                      onClick={() => {
                        history.push(`/BloodBankList`);
                      }}
                    >
                      <a class="nav-link" href="#">
                        Blood Bank List
                      </a>
                    </li>
                    <li
                      class="nav-item"
                      onClick={() => {
                        history.push(`/EventList`);
                      }}
                    >
                      <a class="nav-link" href="#">
                        Event List
                      </a>
                    </li>
                    <li
                      class="nav-item"
                      onClick={() => {
                        history.push(`/BloodLimitList`);
                      }}
                    >
                      <a class="nav-link" href="#">
                        Blood Limit List
                      </a>
                    </li>
                    <li
                      class="nav-item"
                      onClick={() => {
                        history.push(`/SearchDonor`);
                      }}
                    >
                      <a class="nav-link" href="#">
                        Search Donor
                      </a>
                    </li>
                  </ul>
                </div>
              </nav>
            )}
          <SnackBar />
          <div className={`main-container`}>
            <Switch>
              <PrivateRoute
                path={`/Dashboard`}
                component={Dashboard}
                exact={true}
              />

              <PrivateRoute
                path={`/AddBranch`}
                component={AddBranch}
                type="create"
                exact={true}
              />
              <PrivateRoute
                path={`/UpdateBranch/:Br_id`}
                component={UpdateBranch}
                type="modify"
                exact={true}
              />
              <PrivateRoute
                path={`/ListBranch`}
                component={BranchList}
                exact={true}
              />
              <PrivateRoute
                path={`/AddOperator`}
                component={AddOperator}
                type="create"
                exact={true}
              />
              <PrivateRoute
                path={`/UpdateOperator/:Operator_id`}
                component={UpdateOperator}
                type="modify"
                exact={true}
              />
              <PrivateRoute
                path={`/ListOperator`}
                component={OperatorList}
                exact={true}
              />
              <PrivateRoute
                path={`/branch/bloodunits/:Br_id/:Br_Type`}
                component={BloodCountForBranch}
                exact={true}
              />
              <PrivateRoute
                path={`/branch/bloodgroup/bloodunits/:Blood_Group/:Br_id/:Br_Type`}
                component={BloodUnitListForBranchForBloodGroup}
                exact={true}
              />
              <PrivateRoute
                path={`/moveblood`}
                component={MoveBlood}
                exact={true}
              />
              <PrivateRoute
                path={`/expiredbloodunits`}
                component={ExpiredBloodUnitList}
                exact={true}
              />
              <PrivateRoute
                path={"/SearchDonor"}
                component={SearchDonor}
                exact={true}
              />
              <PrivateRoute
                path={"/UpdateDonor/:Donor_id"}
                component={UpdateDonor}
                type="modify"
                exact={true}
              />

              <PrivateRoute
                path={"/AddDonor"}
                component={AddDonor}
                exact={true}
                type="create"
              />
              <PrivateRoute
                path={"/BloodBankList"}
                component={BloodBankList}
                exact={true}
                type="create"
              />
              <PrivateRoute
                path={"/UpdateBloodBank/:Bbank_id"}
                component={UpdateBloodBank}
                exact={true}
                type="create"
              />

              <PrivateRoute
                path={"/AddBloodBank"}
                component={AddBloodBank}
                exact={true}
                type="create"
              />
              <PrivateRoute
                path={"/EventList"}
                component={EventList}
                exact={true}
                type="create"
              />
              <PrivateRoute
                path={"/UpdateEvent/:Drive_id"}
                component={UpdateEvent}
                exact={true}
                type="create"
              />
              <PrivateRoute
                path={"/BloodLimitList"}
                component={BloodLimitList}
                exact={true}
              />
              <PrivateRoute
                path={"/UpdateBloodLimit/:Br_id/:Blood_Group"}
                component={UpdateBloodLimit}
                exact={true}
              />
              <PrivateRoute
                path={"/AddEvent"}
                component={AddEvent}
                exact={true}
                type="create"
              />
              <Route path={`/login`} component={Login} />
              <Route path={`/`} component={Guest} />
              <PrivateRoute path={`/app`} component={App} />
              <Route component={PageNotFound} />
            </Switch>
          </div>
        </Router>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    auth: state.auth,
    loading: state.app.loading,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    logOut: () => {
      dispatch(logOut());
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Routes);

const PageNotFound = (props) => {
  return (
    <div>
      Page Not Found
      <Link to={`/`}>To Home</Link>
      <Link to={`/login`}>To Login</Link>
    </div>
  );
};
