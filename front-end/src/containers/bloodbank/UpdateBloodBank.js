import React, { Component } from "react";
import { getBloodBankInfo, updateBloodBank } from "./action";
import { connect } from "react-redux";
import { history } from "../../Routes";
class UpdateBloodBank extends Component {
  state = {
    data: {
      Name: "",
      Type: "",
      Phone_no: "",
      Bbank_id: "",
    },
  };
  componentDidMount() {
    const { Bbank_id } = this.props.match.params;
    this.props.getBloodBankInfo(Bbank_id, (data) => {
      this.setState({ data });
    });
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
    const { Name, Type, Phone_no, Bbank_id } = data;
    if (Name && Type && Phone_no && Bbank_id) {
      this.props.updateBloodBank(data, () => {
        history.push("/");
      });
    }
    else{
        alert('Please enter valid data')
    }
  };
  render() {
    const { Name, Type, Phone_no } = this.state.data;
    return (
      <div className="card" style={{ textAlign: "left", padding: "10px" }}>
        <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>
          Update Blood bank

        </h4>
        <form onSubmit={this.update}>
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
              Update
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
    updateBloodBank: (data, callback) => {
      dispatch(updateBloodBank(data, callback));
    },
    getBloodBankInfo: (Bbank_id, callback) => {
      dispatch(getBloodBankInfo(Bbank_id, callback));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(UpdateBloodBank);
