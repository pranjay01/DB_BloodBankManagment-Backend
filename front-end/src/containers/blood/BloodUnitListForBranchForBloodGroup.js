import React, { Component } from "react";
import { connect } from "react-redux";
import { addBloodCountForBloodGroup } from "../../reducer/appReducer";
import { getBloodCountForBranchForBloodGroup } from "./action";
import BloodUnitList from "./BloodUnitList";
class BloodUnitListForBranchForBloodGroup extends Component {
  componentDidMount() {
    const { Blood_Group, Br_id } = this.props.match.params;
    let map = [
      { key: "O+", value: "1" },
      { key: "A+", value: "2" },
      { key: "B+", value: "3" },
      { key: "AB+", value: "4" },
      { key: "O-", value: "5" },
      { key: "A-", value: "6" },
      { key: "B-", value: "7" },
      { key: "AB-", value: "8" },
    ];
 let BG_id=   map.filter(i=>i.key==Blood_Group)[0].value
    this.props.getData(Br_id, BG_id);
  }
  componentWillUnmount() {
    this.props.reset();
  }
  render() {
    let { data } = this.props;
    const { Blood_Group, Br_id, Br_Type } = this.props.match.params;
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
          Available Blood units of {Blood_Group} in {Br_Type} branch
        </h4>
        <BloodUnitList data={data} Br_id={Br_id} />
        {/* {data.map((item) => {
          return (
            <div>
              {item.Blood_id} - {item.Blood_Group} - {item.Donor_id} -{" "}
              {item.Donation_Date} - {item.Date_of_Expiry} -{" "}
              {item.Special_Attributes}
            </div>
          );
        })} */}
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    data: state.app.bloodUnitsForBloodGroup,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    getData: (Br_id, Blood_Group) => {
      dispatch(getBloodCountForBranchForBloodGroup(Br_id, Blood_Group));
    },
    reset: () => {
      dispatch(addBloodCountForBloodGroup([]));
    },
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(BloodUnitListForBranchForBloodGroup);
