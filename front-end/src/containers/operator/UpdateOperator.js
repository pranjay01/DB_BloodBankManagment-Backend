import React, { Component } from "react";
import { getAllBloodBankInfo } from "../bloodbank/action";
import { updateOperator } from "./action";
import { connect } from "react-redux";
import { history } from "../../Routes";
class UpdateOperator extends Component {
  state = {
    data: {
      Name: "",
      Email: "",
      Password: "",
      Bbank_id: "-1",
      Operator_id: "",
    },
  };
  componentDidMount() {
    const {Operator_id}=this.props.match.params
    const {operatorList}=this.props;
    if (this.props.bloodBanks.length == 0) {
      this.props.getBloodBankList();
    }
    if(this.props.operatorList.length>0){
      let data=operatorList.filter(i=>i.Operator_id==Operator_id)[0];
      data.Password="";
      this.setState({data});
    }

  }
  handleChange = (e) => {
    const key = e.target.name;
    let { data } = this.state;
    data[key] = e.target.value;
    this.setState({ data });
  };
  update = (e) => {
    e.preventDefault();
    const { data } = this.state;
    const { Name, Email, Password, Bbank_id, Operator_id } = data;
    if (Name && Email && Password && Bbank_id != "-1" && Operator_id) {
      this.props.updateOperator(data, () => {
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
        <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>
          Update Operator
        </h4>
        <form onSubmit={this.update}>
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
              {bloodBanks.map((item) => (
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
    operatorList: state.app.allOperators,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    getBloodBankList: () => {
      dispatch(getAllBloodBankInfo());
    },
    updateOperator: (data, callback) => {
      dispatch(updateOperator(data, callback));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(UpdateOperator);
