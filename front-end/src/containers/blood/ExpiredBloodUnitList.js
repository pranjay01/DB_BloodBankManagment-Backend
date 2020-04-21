import React, { Component } from "react";
import { connect } from "react-redux";
import { addExpiredBloodUnitList } from "../../reducer/appReducer";
import {
  getExpiredBloodUnitInBloodBank,
  deleteExpiredBloodUnitInBloodBank,
} from "./action";
import { history } from "../../Routes";
import BloodUnitList from "./BloodUnitList";
class BloodUnitListForBranchForBloodGroup extends Component {
  componentDidMount() {
    this.props.getData(1, "A+");
  }
  componentWillUnmount() {
    this.props.reset();
  }
  delete = () => {
    this.props.deleteAll(() => {
      history.push("/");
    });
  };
  render() {
    let { data } = this.props;
    // data = [
    //   {
    //     Blood_id: 1,
    //     Blood_Group: "A+",
    //     Donor_id: 1,
    //     Donation_Date: "1/22/2020",
    //     Date_of_Expiry: "4/22/2020",
    //     Special_Attributes: "rare",
    //   },
    //   {
    //     Blood_id: 2,
    //     Blood_Group: "A+",
    //     Donor_id: 1,
    //     Donation_Date: "2/22/2020",
    //     Date_of_Expiry: "5/22/2020",
    //     Special_Attributes: "rare",
    //   },
    // ];

    return (
      <div className="card">
        <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>
          Expired Blood units in all branches{" "}
          <button
            className="commonbtn"
            style={{ float: "right", marginRight: "10px" }}
            onClick={this.delete}
          >
            Delete All
          </button>
        </h4>
        <BloodUnitList data={data} />
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    data: state.app.expiredBloodUnits,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    getData: () => {
      dispatch(getExpiredBloodUnitInBloodBank());
    },
    deleteAll: (callback) => {
      dispatch(deleteExpiredBloodUnitInBloodBank(null, callback));
    },
    reset: () => {
      dispatch(addExpiredBloodUnitList([]));
    },
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(BloodUnitListForBranchForBloodGroup);
