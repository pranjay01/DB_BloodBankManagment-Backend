import React, { Component } from "react";
import { updateBranch, getbranchInfo } from "./action";
import { connect } from "react-redux";
import { history } from "../../Routes";
import { setAuthorizationTokenInHeader } from "../../utils/axioConfig";

class UpdateBranch extends Component {
  state = {
    data: {
      Br_Type: 1,
      Street: "",
      City: "",
      Zip: "",
      Bbank_id: "",
      Phone_no: [],
    },
  };
  componentDidMount() {
    const { Br_id } = this.props.match.params;
    this.props.getbranchInfo({ Br_id }, (data) => {
      data.Br_Type = data.Br_Type == "Sub Branch" ? 2 : 1;
      let Phone_no = [];
      let keys = Object.keys(data.Phone_no);
      keys.forEach((item) => {
        Phone_no.push(item);
      });
      data.Phone_no = Phone_no;
      this.setState({ data });
    });
  }
  addPhone = () => {
    let data = this.state.data;
    data.Phone_no.push(0);
    this.setState({ data });
  };

  deletePhone = (index) => {
    let data = this.state.data;
    data.Phone_no.splice(index, 1);
    this.setState({ data });
  };
  handleChange = (e) => {
    const key = e.target.name;
    let { data } = this.state;
    if (key.includes("Phone_no")) {
      data.Phone_no[key.split(".")[1]] = e.target.value;
    } else {
      data[key] = e.target.value;
    }

    this.setState({ data });
  };
  update = (e) => {
    e.preventDefault();
    const { data } = this.state;
    const { Br_Type, Street, City, Zip, Phone_no } = data;
    if (Br_Type && Street && City && Zip && Phone_no.length > 0) {
      let obj = {};
      Phone_no.forEach((item, index) => {
        let i = index + 1;
        obj[i + ""] = item;
      });
      this.props.updateBranch({ ...data, Phone_no: obj }, () => {
        history.push("/");
      });
    } else {
      alert("Please enter valid data");
    }
  };
  render() {
    const { Br_Type, Street, City, Zip, Phone_no } = this.state.data;
    return (
      <div className="card" style={{ textAlign: "left", padding: "10px" }}>
        <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>
          Update Branch
        </h4>
        <form onSubmit={this.update}>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <label>Branch Type : </label>
            <select name="Br_Type" value={Br_Type} onChange={this.handleChange}>
              <option value={1}>Main Branch</option>
              <option value={2}>Sub Branch</option>
            </select>
          </div>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <label>Street : </label>
            <input
              type="text"
              name="Street"
              value={Street}
              onChange={this.handleChange}
            />
          </div>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <label>City : </label>
            <input
              type="text"
              name="City"
              value={City}
              onChange={this.handleChange}
            />
          </div>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <label>Zip : </label>
            <input
              type="number"
              name="Zip"
              value={Zip}
              onChange={this.handleChange}
            />
          </div>
          <div style={{ margin: "10px" }}>
            <label>Phone No : </label>
            <span onClick={this.addPhone}>
              <a href="#">Add Phone</a>
            </span>
            {Phone_no.map((item, index) => (
              <div>
                <input
                  type="number"
                  name={`Phone_no.${index}`}
                  value={item}
                  onChange={this.handleChange}
                  style={{ margin: "5px" }}
                />
                <span
                  onClick={() => {
                    this.deletePhone(index);
                  }}
                >
                  <a href="#">Delete</a>
                </span>
              </div>
            ))}
          </div>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <button type="submit" className="commonbtn">
              Update
            </button>
          </div>
        </form>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    branches: state.app.branches,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    updateBranch: (data, callback) => {
      dispatch(updateBranch(data, callback));
    },
    getbranchInfo: (data, callback) => {
      dispatch(getbranchInfo(data, callback));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(UpdateBranch);
