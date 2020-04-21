import React, { Component } from "react";
import { addBloodBank } from "./action";
import {connect} from 'react-redux';
import {history} from '../../Routes'
class AddBloodBank extends Component {
  state = {
    data: {
      Name: "",
      Type: "",
      Phone_no: "",
    },
  };

  handleChange = (e) => {
    const key = e.target.name;
    let { data } = this.state;
    data[key] = e.target.value;
    this.setState({ data });
  };
  add = (e) => {
    e.preventDefault();
    const { data } = this.state;
    const { Name, Type, Phone_no } = data;
    if (Name && Type && Phone_no) {
      this.props.addBloodBank(data, () => {
        history.push("/");
      });
    }else{
        alert('Please enter valid data')
    }
  };
  render() {
      const {Name,Type,Phone_no}=this.state.data
    return (
      <div className="card" style={{ textAlign: "left", padding: "10px" }}>
        <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>
          Add Blood bank
        </h4>
        <form onSubmit={this.add}>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <label>Blood Bank Name : </label>
            <input
              type="text"
              name="Name"
              value={Name}
              onChange={this.handleChange}
            />
          </div>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <label>Type : </label>
            <input
              type="text"
              name="Type"
              value={Type}
              onChange={this.handleChange}
            />
          </div>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <label>Phone No : </label>
            <input
              type="number"
              name="Phone_no"
              value={Phone_no}
              onChange={this.handleChange}
            />
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
  return {};
};

const mapDispatchToProps = (dispatch) => {
  return {
    addBloodBank: (data, callback) => {
      dispatch(addBloodBank(data, callback));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(AddBloodBank);
