import React, { Component } from "react";
import { connect } from "react-redux";
import { updateBloodUnit, deleteBloodUnit } from "./action";
class BloodUnitList extends Component {
  render() {
    const { data, Br_id } = this.props;
    return (
      <div>
        <div
          style={{
            textAlign: "left",
            marginLeft: "10px",
            marginRight: "10px",
            borderBottom: "grey solid 1px",
            marginBottom: "5px",
            cursor: "pointer",
          }}
        >
          <div style={{ minWidth: "100px", display: "inline-block" }}>
            Unit Id
          </div>
          <div style={{ minWidth: "120px", display: "inline-block" }}>
            Blood Group
          </div>
          <div style={{ minWidth: "150px", display: "inline-block" }}>
            Donation Date
          </div>
          <div style={{ minWidth: "150px", display: "inline-block" }}>
            Expiry Date
          </div>
          <div style={{ minWidth: "250px", display: "inline-block" }}>
            Special_Attributes
          </div>
          <div style={{ minWidth: "50px", display: "inline-block" }}>Edit</div>
          <div style={{ minWidth: "50px", display: "inline-block" }}>
            Delete
          </div>
        </div>
        {data&&data.map((item) => (
          <BloodUnitRow
            data={item}
            updateBloodUnit={this.props.updateBloodUnit}
            deleteBloodUnit={this.props.deleteBloodUnit}
            Br_id={Br_id}
          />
        ))}
      </div>
    );
  }
}
const mapDispatchToProps = (dispatch) => {
  return {
    updateBloodUnit: (data, callback) => {
      dispatch(updateBloodUnit(data, callback));
    },
    deleteBloodUnit: (Br_id, Blood_id, callback) => {
      dispatch(deleteBloodUnit(Br_id, Blood_id, callback));
    },
  };
};

export default connect(null, mapDispatchToProps)(BloodUnitList);

class BloodUnitRow extends Component {
  delete = () => {
    let { Br_id, data } = this.props;
    if (!Br_id) {
      Br_id = data.Br_id;
    }
    this.props.deleteBloodUnit(Br_id, data.Blood_id, () => {});
  };

  render() {
    const { data: item } = this.props;
    return (
      <div
        style={{
          textAlign: "left",
          marginLeft: "10px",
          marginRight: "10px",
          borderBottom: "grey solid 1px",
          marginBottom: "5px",
          cursor: "pointer",
        }}
      >
        <div style={{ minWidth: "100px", display: "inline-block" }}>
          {item.Blood_id}
        </div>
        <div style={{ minWidth: "120px", display: "inline-block" }}>
          {item.Blood_Group}
        </div>
        <div style={{ minWidth: "150px", display: "inline-block" }}>
          {item.Donation_Date}
        </div>
        <div style={{ minWidth: "150px", display: "inline-block" }}>
          {item.Date_of_Expiry}
        </div>
        <div style={{ minWidth: "250px", display: "inline-block" }}>
          {item.Special_Attributes}
        </div>
        <div style={{ minWidth: "50px", display: "inline-block" }}>
          <a href="#">Edit</a>
        </div>
        <div
          style={{ minWidth: "50px", display: "inline-block" }}
          onClick={this.delete}
        >
          <a href="#">Delete</a>
        </div>
      </div>
    );
  }
}
