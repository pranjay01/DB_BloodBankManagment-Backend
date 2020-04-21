import React, { Component } from "react";
import { connect } from "react-redux";
import {
  getBloodCountByBloodBankForGuest,
  getBloodCountForBloodBankForGuest,
  getBloodCountForBranchForGuest,
} from "./action";
import { history } from "../../Routes";
class Guest extends Component {
  state = {
    selectedBloodBank: null,
    selectedBranch: null,
  };

  componentDidMount() {
    this.props.getBloodCountByBloodBankForGuest();
  }
  changeSelectedBloodbank = (Bbank_id) => {
    this.setState({ selectedBloodBank: Bbank_id, selectedBranch: null }, () => {
      this.props.getBloodCountForBloodBankForGuest(Bbank_id);
    });
  };
  changeSelectedBranch = (Br_id) => {
    this.setState({ selectedBranch: Br_id }, () => {
      this.props.getBloodCountForBranchForGuest(Br_id);
    });
  };
  render() {
    const { selectedBloodBank, selectedBranch } = this.state;
    let {
      loginData,
      blood_banks,
      blood_bank_branches,
      blood_groups,
    } = this.props;
    // blood_banks = [
    //   { Bbank_id: 1, Blood_Bank_Name: "Red Cross", Blood_Unit_Count: 50 },
    //   { Bbank_id: 2, Blood_Bank_Name: "Prathma", Blood_Unit_Count: 500 },
    // ];
    // blood_bank_branches = [
    //   { Br_id: 1, Br_Type: "Main", Blood_Unit_Count: 50 },
    //   { Br_id: 2, Br_Type: "Sub", Blood_Unit_Count: 500 },
    // ];
    // blood_groups = [
    //   { Blood_Group: "A+", Blood_Unit_Count: 10 },
    //   { Blood_Group: "A-", Blood_Unit_Count: 10 },
    //   { Blood_Group: "AB+", Blood_Unit_Count: 10 },
    // ];
    return (
      <div>
        {!loginData && (
          <div>
            <button
              className="commonbtn"
              onClick={() => {
                history.push(`/login`);
              }}
              style={{
                float: "right",
                marginRight: "15px",
                marginBottom: "10px",
              }}
            >
              Login
            </button>
          </div>
        )}
        <div
          className="card "
          style={{
            width: "28%",
            display: "inline-block",
            verticalAlign: "top",
          }}
        >
          <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>
            Total Blood units available in Bloodbank
          </h4>
          {blood_banks &&
            blood_banks.map((item) => (
              <BloodBankRow
                data={item}
                select={this.changeSelectedBloodbank}
                selected={selectedBloodBank}
              />
            ))}
        </div>
        {selectedBloodBank && (
          <div
            className="card "
            style={{
              width: "28%",
              display: "inline-block",
              verticalAlign: "top",
            }}
          >
            <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>
              Total Blood units available in diffrent branches
            </h4>
            {blood_bank_branches &&
              blood_bank_branches.map((item) => (
                <BranchRow
                  data={item}
                  select={this.changeSelectedBranch}
                  selected={selectedBranch}
                />
              ))}
          </div>
        )}
        {selectedBranch && (
          <div
            className="card "
            style={{
              width: "28%",
              display: "inline-block",
              verticalAlign: "top",
            }}
          >
            <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>
              Total Blood units available for diffrent blood groups
            </h4>
            {blood_groups &&
              blood_groups.map((item) => <BloodGroupRow data={item} />)}
          </div>
        )}
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    loginData: state.auth.loginData,
    blood_banks: state.app.bloodBanksUnitForGuest,
    blood_bank_branches: state.app.bloodBankBranchesUnitsForGuest,
    blood_groups: state.app.branchBloodGroupUnitsForGuest,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    getBloodCountByBloodBankForGuest: () => {
      dispatch(getBloodCountByBloodBankForGuest());
    },
    getBloodCountForBloodBankForGuest: (Bbank_id) => {
      dispatch(getBloodCountForBloodBankForGuest(Bbank_id));
    },
    getBloodCountForBranchForGuest: (Br_id) => {
      dispatch(getBloodCountForBranchForGuest(Br_id));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Guest);

class BloodBankRow extends Component {
  select = () => {
    const { data } = this.props;
    this.props.select(data.Bbank_id);
  };
  render() {
    const { data: item, selected } = this.props;
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
        className={item.Bbank_id == selected && "selected"}
        onClick={this.select}
      >
        <a href="#">{item.Blood_Bank_Name}</a>
        <span style={{ float: "right" }}>
          <b>{item.Blood_Unit_Count}</b> Units
        </span>
      </div>
    );
  }
}

class BranchRow extends Component {
  select = () => {
    const { data } = this.props;
    this.props.select(data.Br_id);
  };
  render() {
    const { data: item, selected } = this.props;
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
        className={item.Br_id == selected && "selected"}
        onClick={this.select}
      >
        <a href="#">{item.Br_Type}</a>
        <span style={{ float: "right" }}>
          <b>{item.Blood_Unit_Count}</b> Units
        </span>
      </div>
    );
  }
}

class BloodGroupRow extends Component {
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
        onClick={this.select}
      >
        <a href="#">{item.Blood_Group}</a>
        <span style={{ float: "right" }}>
          <b>{item.Blood_Unit_Count}</b> Units
        </span>
      </div>
    );
  }
}
