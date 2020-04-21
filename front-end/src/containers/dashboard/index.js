import React, { Component } from "react";
import { connect } from "react-redux";
import { getBloodcountAndBloodBankName } from "../blood/action";
import BlooCountForBloodBank from "../blood/BlooCountForBloodBank";
import { history } from "../../Routes";
class index extends Component {
  componentDidMount() {
    if (!this.props.data) {
      this.props.getBloodcountAndBloodBankName();
    }
  }
  render() {
    let { data } = this.props;
    //data = { Blood_Bank_Name: "First Bank", Blood_Unit_Count: 40 };
    return (
      <div className="dashboard">
        {data && (
          <div
            className="blood-bank-name card"
            style={{ display: "inline-block" }}
          >
            <h3
              style={{
                textAlign: "left",
                width: "70%",
                margin: "15 5 15 5",
                display: "inline-block",
              }}
            >
              {data.Blood_Bank_Name}
            </h3>
            <span
              className="float-right"
              style={{ width: "20%", display: "inline-block" }}
            >
              Total <b style={{ fontSize: "27px" }}>{data.Blood_Unit_Count}</b>{" "}
              Units
            </span>
          </div>
        )}
        <div
          className="card "
          style={{ width: "46%", display: "inline-block" }}
        >
          <BlooCountForBloodBank />
        </div>
        <div
          className="card"
          style={{
            width: "46%",
            display: "inline-block",
            verticalAlign: "top",
          }}
        >
          <div
            style={{
              textAlign: "left",
              marginLeft: "10px",
              marginRight: "10px",
              borderBottom: "grey solid 1px",
              marginBottom: "5px",
              cursor: "pointer",
            }}
            on
          >
            <h5
              style={{
                textAlign: "left",
                paddingLeft: "10px",
                marginTop: "5px",
              }}
              onClick={() => {
                history.push(`/moveblood`);
              }}
            >
              <a href="#">Move Blood Units</a>
            </h5>
          </div>
          <div
            style={{
              textAlign: "left",
              marginLeft: "10px",
              marginRight: "10px",
              borderBottom: "grey solid 1px",
              marginBottom: "5px",
              cursor: "pointer",
            }}
            onClick={() => {
              history.push(`/expiredbloodunits`);
            }}
          >
            <h5
              style={{
                textAlign: "left",
                paddingLeft: "10px",
                marginTop: "5px",
              }}
            >
              <a href="#">List Expired Blood Units</a>
            </h5>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    data: state.app.bloodBankCountAndBloodBankName,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    getBloodcountAndBloodBankName: () => {
      dispatch(getBloodcountAndBloodBankName());
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(index);
