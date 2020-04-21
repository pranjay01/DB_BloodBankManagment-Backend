import React, { Component } from "react";
import { connect } from "react-redux";
import { addBloodCountForBranch } from "../../reducer/appReducer";
import { getBloodCountForBranch } from "./action";
import { history } from "../../Routes";
class BlooCountForBranch extends Component {
  componentDidMount() {
    const { Br_id } = this.props.match.params;
    this.props.getData(Br_id);
  }
  componentWillUnmount() {
    this.props.reset();
  }
  render() {
    let { data } = this.props;
    const { Br_Type, Br_id } = this.props.match.params;
    // data = [
    //   { Blood_Group: "A+", Blood_Unit_Count: 10 },
    //   { Blood_Group: "A-", Blood_Unit_Count: 10 },
    //   { Blood_Group: "AB+", Blood_Unit_Count: 10 },
    // ];
    return (
      <div className="card">
        <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>
          Blood group wise blood unit availability for branch : {Br_Type}
        </h4>
        {data&&data.map((item) => {
          return (
            <BloodCountForBranchItem
              data={item}
              Br_id={Br_id}
              Br_Type={Br_Type}
            />
          );
        })}
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    data: state.app.bloodCountForBranch,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    getData: (Br_id) => {
      dispatch(getBloodCountForBranch(Br_id));
    },
    reset: () => {
      dispatch(addBloodCountForBranch([]));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(BlooCountForBranch);

class BloodCountForBranchItem extends Component {
  redirect = () => {
    const { data, Br_id, Br_Type } = this.props;
    history.push(
      `/branch/bloodgroup/bloodunits/${data.Blood_Group}/${Br_id}/${Br_Type}`
    );
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
        onClick={this.redirect}
      >
        <a href="#">{item.Blood_Group}</a>
        <span style={{ float: "right" }}>
          <b>{item.Blood_Unit_Count}</b> Units
        </span>
      </div>
    );
  }
}
