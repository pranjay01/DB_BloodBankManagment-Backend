import React, { Component } from "react";
import { addBranch } from "./action";
import { connect } from "react-redux";
import { history } from "../../Routes";
class AddBranch extends Component {
  state = {
    data: {
      Br_Type: 1,
      Street: "",
      City: "",
      Zip: "",
      Bbank_id:this.props.Bbank_id,
      Phone_no: [],
    },
  };
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
  add = (e) => {
    e.preventDefault();
    const { data } =this.state;
    const { Br_Type, Street, City, Zip, Phone_no } = data;
    if (Br_Type && Street && City && Zip && Phone_no.length > 0) {
      let obj = {};
      Phone_no.forEach((item, index) => {
        let i = index + 1;
        obj[i + ""] = item;
      });
      
      this.props.addBranch({...data,Phone_no:obj}, () => {
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
        <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>Add Branch</h4>
        <form onSubmit={this.add}>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <label>Branch Type : </label>
            <select
              name="Br_Type"
              value={Br_Type}
              onChange={this.handleChange}
            >
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
              Add
            </button>
          </div>
        </form>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    Bbank_id:state.auth.loginData.Bbank_id
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    addBranch: (data, callback) => {
      dispatch(addBranch(data, callback));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(AddBranch);
