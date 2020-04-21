import React, { Component } from "react";
import { addBloodUnit } from "./action";
import { getBranchList } from "../branch/action";
class AddBlooadUnit extends Component {
  state = {
    data: {
      Special_Attributes: "",
      Br_id: "-1",
      Donor_id: this.props.Donor_id,
    },
  };
  componentDidMount() {
    if (this.props.branches.length == 0) {
      this.props.getBranchList();
    }
  }
  handleChange = (e) => {
    const key = e.target.name;
    let { data } = this.state;
    data[key] = e.target.value;
    this.setState({ data });
  };
  add = (e) => {
    e.preventDefault();
    const { data } = this.state;
    if (data.Br_id != "-1") {
      this.props.addBloodUnit(data, () => {});
    } else {
      alert("Select branch");
    }
  };
  render() {
    const { Special_Attributes, Br_id } = this.state.data;
    let { branches } = this.props;
    // branches = [
    //   { Br_id: 1, Br_name: "Main" },
    //   { Br_id: 2, Br_name: "Sub" },
    // ];
    return (
      <div>
        <form onSubmit={this.add}>
          <label>Branch</label>
          <select name="Br_id" onChange={this.handleChange} value={Br_id}>
            <option value="-1">-- select --</option>
            {branches.map((item) => (
              <option value={item.Br_id}>{item.Br_Type}</option>
            ))}
          </select>
          <label>Speacial Attributes</label>
          <input
            type="text"
            name="Special_Attributes"
            value={Special_Attributes}
            onChange={this.handleChange}
          />
          <button className="commonbtn" type="submit">
            Add
          </button>
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
    addBloodUnit: (data, callback) => {
      dispatch(addBloodUnit(data, callback));
    },
    getBranchList: () => {
      dispatch(getBranchList());
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(AddBlooadUnit);
