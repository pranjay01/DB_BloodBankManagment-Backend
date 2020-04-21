import React, { Component } from "react";
import { getAllBloodBankInfo } from "../bloodbank/action";
import { addOpeator } from "./action";
import { connect } from "react-redux";
import { history } from "../../Routes";
class AddOperator extends Component {
  state = {
    data: {
      Name: "",
      Email: "",
      Password: "",
      Bbank_id: "-1",
    },
  };
  componentDidMount() {
    if (this.props.bloodBanks.length == 0) {
      this.props.getBloodBankList();
    }
  }
  handleChange = (e) => {
    debugger;
    const key = e.target.name;
    let { data } = this.state;
    data[key] = e.target.value;
    this.setState({ data });
  };
  add = (e) => {
    e.preventDefault();
    const { data } = this.state;
    const { Name, Email, Password, Bbank_id } = data;
    debugger;
    if (Name && Email && Password && Bbank_id != "-1") {
      this.props.addOpeator(data, () => {
        history.push("/");
      });
    } else {
      alert("Please enter valid data");
    }
  };
  render() {
    const { Name, Email, Password, Bbank_id } = this.state.data;
    let { bloodBanks } = this.props;
    // bloodBanks = [
    //   { Bbank_id: 1, Name: "Red cross" },
    //   { Bbank_id: 2, Name: "Prathma" },
    // ];
    return (
      <div className="card" style={{ textAlign: "left", padding: "10px" }}>
        <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>Add Operator</h4>
        <form onSubmit={this.add}>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <label>Name : </label>
            <input
              type="text"
              name="Name"
              value={Name}
              onChange={this.handleChange}
            />
          </div>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <label>Email : </label>
            <input
              type="email"
              name="Email"
              value={Email}
              onChange={this.handleChange}
            />
          </div>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <label>Password : </label>
            <input
              type="text"
              name="Password"
              value={Password}
              onChange={this.handleChange}
            />
          </div>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <label>Blood bank : </label>
            <select
              name="Bbank_id"
              onChange={this.handleChange}
              value={Bbank_id}
            >
              <option value="-1" selected={Bbank_id == "-1"}>
                -- select --
              </option>
              {bloodBanks&&bloodBanks.map((item) => (
                <option value={item.Bbank_id}>{item.Name}</option>
              ))}
            </select>
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
    bloodBanks: state.app.bloodBankList,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    getBloodBankList: () => {
      dispatch(getAllBloodBankInfo());
    },
    addOpeator: (data, callback) => {
      dispatch(addOpeator(data, callback));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(AddOperator);
